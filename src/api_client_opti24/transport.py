from __future__ import annotations

import asyncio
from typing import Any

import httpx

from .errors import NotAuthenticatedError, build_api_error
from .logger import logger
from .utils import sanitize_for_logging


class AsyncTransport:
    def __init__(self, base_url: str, client, default_timeout: float = 30.0):
        self.base_url = base_url.rstrip("/") + "/"
        self.client = httpx.AsyncClient(timeout=default_timeout)
        self._parent = client
        self._rate_limit_attempts = 3
        self._rate_limit_backoff_seconds = 0.5
        self._network_attempts = 5
        self._network_backoff_min_seconds = 2.0
        self._network_backoff_max_seconds = 60.0

    def _build_url(self, api_version: str, endpoint: str) -> str:
        return f"{self.base_url}{api_version}/{endpoint.lstrip('/')}"

    async def aclose(self) -> None:
        await self.client.aclose()

    def _safe_json(self, resp: httpx.Response) -> Any:
        try:
            return resp.json()
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not parse JSON for %s: %s", resp.request.url, exc)
            return resp.text

    def _handle_response(
        self,
        resp: httpx.Response,
        endpoint: str,
        *,
        method_name: str | None = None,
    ) -> Any:
        body = self._safe_json(resp)
        payload_status_code = None
        if isinstance(body, dict) and isinstance(body.get("status"), dict):
            raw_payload_status = body["status"].get("code")
            if isinstance(raw_payload_status, int):
                payload_status_code = raw_payload_status

        if 200 <= resp.status_code < 300 and (
            payload_status_code is None or 200 <= payload_status_code < 300
        ):
            return body

        if (
            payload_status_code is not None
            and not (200 <= resp.status_code < 300)
            and 200 <= payload_status_code < 300
        ):
            logger.warning(
                "API returned non-2xx HTTP status %s for %s, but payload status.code=%s; treating response as successful",
                resp.status_code,
                endpoint,
                payload_status_code,
            )
            return body

        logger.error(
            "API error http=%s api=%s on %s: %s",
            resp.status_code,
            payload_status_code,
            endpoint,
            sanitize_for_logging(body),
        )
        raise build_api_error(
            status_code=payload_status_code if payload_status_code is not None else resp.status_code,
            body=body,
            endpoint=endpoint,
            method_name=method_name,
            http_status_code=resp.status_code,
        )

    async def request(
        self,
        method: str,
        endpoint: str,
        api_version: str = "v1",
        headers=None,
        retry_auth: bool = True,
        timeout: float | None = None,
        method_name: str | None = None,
        **kwargs,
    ) -> Any:
        url = self._build_url(api_version, endpoint)
        network_backoff = self._network_backoff_min_seconds

        for network_attempt in range(1, self._network_attempts + 1):
            try:
                for rate_attempt in range(1, self._rate_limit_attempts + 1):
                    resp = await self.client.request(
                        method,
                        url,
                        headers=headers,
                        timeout=timeout,
                        **kwargs,
                    )
                    logger.info("HTTP %s %s → %s", method.upper(), endpoint, resp.status_code)

                    if resp.status_code in {429, 509} and rate_attempt < self._rate_limit_attempts:
                        backoff_seconds = self._rate_limit_backoff_seconds * rate_attempt
                        logger.warning(
                            "Rate limit on %s %s, attempt %s/%s; backing off for %.2fs",
                            method,
                            url,
                            rate_attempt,
                            self._rate_limit_attempts,
                            backoff_seconds,
                        )
                        await asyncio.sleep(backoff_seconds)
                        continue

                    try:
                        return self._handle_response(resp, endpoint, method_name=method_name)
                    except NotAuthenticatedError:
                        if not retry_auth:
                            raise

                        self._parent.session_manager.invalidate()
                        await self._parent.session_manager.ensure_authenticated(self._parent.auth_user)
                        refreshed_headers = self._parent._headers(include_session=True)
                        return await self.request(
                            method,
                            endpoint,
                            api_version=api_version,
                            headers=refreshed_headers,
                            retry_auth=False,
                            timeout=timeout,
                            method_name=method_name,
                            **kwargs,
                        )

                raise RuntimeError("Rate limit retry loop exhausted unexpectedly")

            except httpx.RequestError:
                if network_attempt >= self._network_attempts:
                    raise

                logger.warning(
                    "Network error on %s %s, attempt %s/%s; backing off for %.2fs",
                    method,
                    url,
                    network_attempt,
                    self._network_attempts,
                    network_backoff,
                )
                await asyncio.sleep(network_backoff)
                network_backoff = min(
                    network_backoff * 2,
                    self._network_backoff_max_seconds,
                )

    async def request_stream(self, method: str, url: str, headers=None, **kwargs) -> bytes:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = url.lstrip("/")
            url = f"{self.base_url}{url}"
        async with self.client.stream(method, url, headers=headers, **kwargs) as resp:
            resp.raise_for_status()
            return await resp.aread()
