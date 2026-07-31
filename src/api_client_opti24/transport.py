from __future__ import annotations

import asyncio
import ipaddress
import time
from collections.abc import Awaitable, Callable, Mapping
from contextlib import AbstractAsyncContextManager
from typing import Any, Protocol
from urllib.parse import urlsplit

import httpx

from .logger import LoggerLike
from .logger import logger as default_logger
from .policies import (
    IDEMPOTENT_HTTP_METHODS,
    SAFE_HTTP_METHODS,
    RateLimitPolicy,
    RetryClass,
    RetryPolicy,
)
from .response import DecodedPayload, ResponseDecoder
from .runtime import Clock


class AsyncHTTPClient(Protocol):
    async def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response: ...

    def stream(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> AbstractAsyncContextManager[httpx.Response]: ...

    async def aclose(self) -> None: ...


AsyncSleep = Callable[[float], Awaitable[None]]
SendOnce = Callable[[], Awaitable[httpx.Response]]


class AsyncTransport:
    def __init__(
        self,
        base_url: str,
        default_timeout: float = 30.0,
        *,
        http_client: AsyncHTTPClient | None = None,
        retry_policy: RetryPolicy | None = None,
        rate_limit_policy: RateLimitPolicy | None = None,
        allow_insecure_http: bool = False,
        response_decoder: ResponseDecoder | None = None,
        logger: LoggerLike | None = None,
        clock: Clock | None = None,
        sleep: AsyncSleep = asyncio.sleep,
        monotonic: Callable[[], float] = time.monotonic,
    ) -> None:
        self.base_url = self._normalize_base_url(
            base_url,
            allow_insecure_http=allow_insecure_http,
        )
        self.client = http_client or httpx.AsyncClient(timeout=default_timeout)
        self._owns_http_client = http_client is None
        self.logger: LoggerLike = logger or default_logger
        self.response_decoder = response_decoder or ResponseDecoder(logger=self.logger)
        self.retry_policy = retry_policy or RetryPolicy()
        self.rate_limit_policy = rate_limit_policy or RateLimitPolicy()
        self._sleep = clock.sleep if clock is not None else sleep
        self._monotonic = clock.monotonic if clock is not None else monotonic
        self._rate_limit_lock = asyncio.Lock()
        self._auth_limit_lock = asyncio.Lock()
        self._last_request_started_at: float | None = None
        self._last_auth_request_started_at: float | None = None

    @staticmethod
    def _normalize_base_url(
        base_url: str,
        *,
        allow_insecure_http: bool = False,
    ) -> str:
        normalized = base_url.strip()
        if not normalized:
            raise ValueError(
                "base_url is empty; set API_BASE_URL in .env or pass base_url explicitly"
            )

        parsed = urlsplit(normalized)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(
                "base_url must be an absolute URL starting with http:// or https://; "
                f"got {base_url!r}"
            )

        if (
            parsed.scheme == "http"
            and not allow_insecure_http
            and not AsyncTransport._is_loopback_host(parsed.hostname)
        ):
            raise ValueError(
                "base_url must use https:// for remote hosts; "
                "set allow_insecure_http=True only for controlled test environments"
            )

        return normalized.rstrip("/") + "/"

    @staticmethod
    def _is_loopback_host(hostname: str | None) -> bool:
        if hostname is None:
            return False
        if hostname.lower() == "localhost":
            return True
        try:
            return ipaddress.ip_address(hostname).is_loopback
        except ValueError:
            return False

    def _build_url(self, api_version: str, endpoint: str) -> str:
        return f"{self.base_url}{api_version}/{endpoint.lstrip('/')}"

    async def aclose(self) -> None:
        if self._owns_http_client:
            await self.client.aclose()

    async def _wait_for_rate_limit(self) -> None:
        minimum_interval = self.rate_limit_policy.minimum_interval_seconds
        if minimum_interval <= 0:
            return

        async with self._rate_limit_lock:
            now = self._monotonic()
            if self._last_request_started_at is not None:
                wait_seconds = self._last_request_started_at + minimum_interval - now
                if wait_seconds > 0:
                    await self._sleep(wait_seconds)
                    now = self._monotonic()
            self._last_request_started_at = now

    async def _wait_for_auth_limit(self, retry_class: str | RetryClass) -> None:
        if RetryClass.normalize(retry_class) is not RetryClass.NETWORK_ONLY:
            return

        minimum_interval = self.retry_policy.auth_retry_min_interval_seconds
        if minimum_interval <= 0:
            return

        async with self._auth_limit_lock:
            now = self._monotonic()
            if self._last_auth_request_started_at is not None:
                wait_seconds = self._last_auth_request_started_at + minimum_interval - now
                if wait_seconds > 0:
                    await self._sleep(wait_seconds)
                    now = self._monotonic()
            self._last_auth_request_started_at = now

    def _safe_json(self, resp: httpx.Response) -> DecodedPayload:
        return self.response_decoder.parse(resp)

    def _handle_response(
        self,
        resp: httpx.Response,
        endpoint: str,
        *,
        method_name: str | None = None,
    ) -> DecodedPayload:
        return self.response_decoder.decode(
            resp,
            endpoint,
            method_name=method_name,
        )

    async def _execute_with_policy(
        self,
        *,
        method: str,
        retry_class: str | RetryClass | None,
        idempotent: bool | None,
        method_name: str | None,
        send_once: SendOnce,
    ) -> httpx.Response:
        normalized_method = method.upper()
        resolved_retry_class = retry_class or (
            RetryClass.SAFE.value
            if normalized_method in SAFE_HTTP_METHODS
            else RetryClass.NEVER.value
        )
        resolved_idempotent = (
            normalized_method in IDEMPOTENT_HTTP_METHODS if idempotent is None else idempotent
        )
        network_attempts = self.retry_policy.network_attempt_count(
            resolved_retry_class,
            normalized_method,
            idempotent=resolved_idempotent,
        )
        rate_limit_attempts = self.retry_policy.rate_limit_attempt_count(
            resolved_retry_class,
            normalized_method,
            idempotent=resolved_idempotent,
        )
        network_backoff = self.retry_policy.initial_network_backoff(resolved_retry_class)

        for network_attempt in range(1, network_attempts + 1):
            try:
                for rate_attempt in range(1, rate_limit_attempts + 1):
                    await self._wait_for_rate_limit()
                    await self._wait_for_auth_limit(resolved_retry_class)
                    response = await send_once()
                    self.logger.info(
                        "HTTP method=%s operation=%s status=%s",
                        normalized_method,
                        method_name or "unregistered",
                        response.status_code,
                    )

                    if response.status_code in {429, 509} and rate_attempt < rate_limit_attempts:
                        backoff_seconds = (
                            self.retry_policy.rate_limit_backoff_seconds * rate_attempt
                        )
                        self.logger.warning(
                            "Rate limit method=%s operation=%s attempt=%s/%s backoff=%.2fs",
                            normalized_method,
                            method_name or "unregistered",
                            rate_attempt,
                            rate_limit_attempts,
                            backoff_seconds,
                        )
                        await self._sleep(backoff_seconds)
                        continue

                    return response

                raise RuntimeError("Rate limit retry loop exhausted unexpectedly")

            except httpx.RequestError:
                if network_attempt >= network_attempts:
                    raise

                self.logger.warning(
                    "Network error method=%s operation=%s attempt=%s/%s backoff=%.2fs",
                    normalized_method,
                    method_name or "unregistered",
                    network_attempt,
                    network_attempts,
                    network_backoff,
                )
                await self._sleep(network_backoff)
                network_backoff = min(
                    network_backoff * 2,
                    self.retry_policy.network_backoff_max_seconds,
                )

        raise RuntimeError("Network retry loop exhausted unexpectedly")

    async def request(
        self,
        method: str,
        endpoint: str,
        api_version: str = "v1",
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
        method_name: str | None = None,
        retry_class: str | RetryClass | None = None,
        idempotent: bool | None = None,
        **kwargs: Any,
    ) -> DecodedPayload:
        url = self._build_url(api_version, endpoint)

        async def send_once() -> httpx.Response:
            return await self.client.request(
                method,
                url,
                headers=headers,
                timeout=timeout,
                **kwargs,
            )

        response = await self._execute_with_policy(
            method=method,
            retry_class=retry_class,
            idempotent=idempotent,
            method_name=method_name,
            send_once=send_once,
        )
        return self._handle_response(response, endpoint, method_name=method_name)

    async def request_stream(
        self,
        method: str,
        endpoint: str,
        api_version: str = "v1",
        headers: Mapping[str, str] | None = None,
        timeout: float | None = None,
        *,
        method_name: str | None = None,
        retry_class: str | RetryClass | None = None,
        idempotent: bool | None = None,
        **kwargs: Any,
    ) -> bytes:
        parsed = urlsplit(endpoint)
        if parsed.scheme or parsed.netloc:
            raise ValueError("stream endpoint must be relative to the configured base_url")
        url = self._build_url(api_version, endpoint)

        async def send_once() -> httpx.Response:
            async with self.client.stream(
                method,
                url,
                headers=headers,
                timeout=timeout,
                **kwargs,
            ) as response:
                await response.aread()
                return response

        response = await self._execute_with_policy(
            method=method,
            retry_class=retry_class,
            idempotent=idempotent,
            method_name=method_name,
            send_once=send_once,
        )
        return self.response_decoder.decode_bytes(
            response,
            response.content,
            url,
            method_name=method_name,
        )
