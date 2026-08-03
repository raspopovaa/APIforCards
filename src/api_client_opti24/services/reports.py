from pathlib import Path
from typing import Any

from ..decorators import api_method
from ..modeling import decode_model
from ..models.reports import (
    ReportJobListResponse,
    ReportListResponse,
    ReportOrderResponse,
    ReportV1JobListResponse,
    ReportV1OrderResponse,
)
from ..service_base import _BaseService
from ..utils import to_json_param


class ReportsService(_BaseService):
    """
    Методы для работы с отчетами (v1 и v2)
    Будет возвращен транзакционный отчет, относящийся к указанному договору.
    Дата начала периода должна быть меньше или равна дате окончания периода.
    В противном случае сервер автоматически выставит дату окончания периода равной дате начала.
    Длина периода не должна превышать 3 календарных месяцев.
    Если длина периода будет превышена, то он автоматически будет сокращен до 3 календарных месяцев с указанной даты начала периода.
    Карты и группы карт, указанные в запросе, должны принадлежать указанному договору.
    Ограничения отправки отчетов на Email составляет 15мб.
    Длительность формирования отчетов за период 1 месяц составляет порядка 300 секунд, при выборе периода более 1 месяца, время формирования отчета может занять до 15 минут.
    Теперь отчет можно заказать и скачать по ссылке. Заказ производится стандартным образом, только не нужно указывать email, иначе прийдет на email..
    """

    # -------- v2 --------
    @api_method
    async def get_reports(
        self,
        *,
        api_version: str | None = None,
    ) -> ReportListResponse:
        """
        Получить список доступных отчетов (v2).
        """
        self.logger.info("Запрос списка доступных отчетов (v2)")
        raw = await self._request(
            "get_reports",
            api_version=api_version,
        )
        return decode_model(ReportListResponse, raw)

    @api_method
    async def order_report(
        self,
        *,
        report_id: str,
        format: str,
        params: dict[str, Any],
        emails: str | None = None,
        api_version: str | None = None,
    ) -> ReportOrderResponse:
        """
        Заказать отчет (на email или по ссылке).

        Типовой сценарий:
            Сначала получить идентификатор отчёта через ``get_reports``, затем
            заказать формирование и отслеживать задачу через ``get_report_jobs``.

        Пример вызова:
        ```python
        job = await client.reports.order_report(
            report_id="report-id",
            format="xlsx",
            params={
                "contract_id": "contract-id",
                "date_from": "2026-01-01",
                "date_to": "2026-01-31",
            },
        )
        ```

        Пример payload:
        ```json
        {
          "id": "report-id",
          "format": "xlsx",
          "params": {
            "contract_id": "contract-id",
            "date_from": "2026-01-01",
            "date_to": "2026-01-31"
          }
        }
        ```
        """
        body = {"id": report_id, "format": format, "params": params}
        if emails:
            body["emails"] = emails

        self.logger.info("Ordering report format=%s delivery=%s", format, bool(emails))

        raw = await self._request(
            "order_report",
            api_version=api_version,
            json=body,
        )
        return decode_model(ReportOrderResponse, raw)

    @api_method
    async def get_report_jobs(
        self,
        *,
        api_version: str | None = None,
    ) -> ReportJobListResponse:
        """
        Получить список заказанных отчетов (v2).
        """
        self.logger.info("Получение списка заказанных отчетов (v2)")
        raw = await self._request(
            "get_report_jobs",
            api_version=api_version,
        )
        return decode_model(ReportJobListResponse, raw)

    @api_method
    async def download_report_file(
        self,
        *,
        job_id: str,
        api_version: str | None = None,
    ) -> bytes:
        """
        Скачать файл отчета (по job_id).

        ⚠️ Важно: успешный запрос возможен только спустя ~300 секунд
        после заказа отчета.
        """
        self.logger.info("Downloading report version=%s", api_version)

        content = await self._request_stream(
            "download_report_file",
            api_version=api_version,
            path_params={"job_id": job_id},
        )

        self.logger.info("Report downloaded bytes=%s", len(content))
        return content

    async def download_report_file_to(
        self,
        *,
        job_id: str,
        destination: str | Path,
        api_version: str | None = None,
    ) -> Path:
        """Потоково скачать отчёт v2 в файл без накопления содержимого в памяти."""
        return await self._request_stream_to_file(
            "download_report_file",
            destination,
            api_version=api_version,
            path_params={"job_id": job_id},
        )

    # -------- v1 --------
    @api_method
    async def order_report_v1(
        self,
        *,
        contract_id: str,
        start: str,
        end: str,
        report_format: str,
        email: str | None = None,
        cards_list: list[str] | None = None,
        group_id: list[str] | None = None,
        archive: bool = False,
        api_version: str | None = None,
    ) -> ReportV1OrderResponse:
        """
        Заказ отчета (v1) – email или файл.
        """
        params = {
            "contract_id": contract_id,
            "start": start,
            "end": end,
            "report_format": report_format,
        }

        if email:
            params["email"] = email
        if cards_list:
            params["cards_list"] = to_json_param(cards_list)
        if group_id:
            params["group_id"] = to_json_param(group_id)
        if archive:
            params["archive"] = "true"

        self.logger.info("Ordering report version=v1 format=%s", report_format)

        raw = await self._request(
            "order_report_v1",
            api_version=api_version,
            params=params,
        )
        return decode_model(ReportV1OrderResponse, raw)

    @api_method
    async def get_report_job_list_v1(
        self,
        *,
        api_version: str | None = None,
    ) -> ReportV1JobListResponse:
        """
        Получить список заказанных отчетов (v1).
        """
        self.logger.info("Получение списка заказанных отчетов (v1)")
        raw = await self._request(
            "get_report_job_list_v1",
            api_version=api_version,
        )
        return decode_model(ReportV1JobListResponse, raw)

    @api_method
    async def download_report_file_v1(
        self,
        *,
        job_id: str,
        archive: bool = False,
        api_version: str | None = None,
    ) -> bytes:
        """
        Скачать файл отчета (v1)
        После того как вы узнали Job_ID своего заказанного отчета по ссылке, его содержимое нужно получить и сформировать файл.
        Формирование файла вы занимаетесь на своей стороне,
        выставить имя файла, формат файл, содержимое и размер, получив от нас данные в виде потока application/octet-stream.
        Если заказывать отчет с параметром archive=true, то нужно выставить формат zip и данные прийдут в виде application/zip.
        Внутри архива будет находится отчет в заказанном формате (pdf, xlsx, csv, xml и другие)..
        """
        params = {"job_id": job_id}
        if archive:
            params["archive"] = "true"

        self.logger.info("Downloading report version=v1 archive=%s", archive)

        content = await self._request_stream(
            "download_report_file_v1",
            api_version=api_version,
            params=params,
        )

        self.logger.info("Report downloaded version=v1 bytes=%s", len(content))
        return content

    async def download_report_file_v1_to(
        self,
        *,
        job_id: str,
        destination: str | Path,
        archive: bool = False,
        api_version: str | None = None,
    ) -> Path:
        """Потоково скачать отчёт v1 в файл без накопления содержимого в памяти."""
        params = {"job_id": job_id}
        if archive:
            params["archive"] = "true"
        return await self._request_stream_to_file(
            "download_report_file_v1",
            destination,
            api_version=api_version,
            params=params,
        )
