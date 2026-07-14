from ..decorators import api_method
from ..logger import logger
from ..modeling import decode_model
from ..models.reports import (
    ReportJobList,
    ReportList,
    ReportOrderResponse,
    ReportV1JobList,
    ReportV1OrderResponse,
)
from ..utils import to_json_param


class ReportsMixin:
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
    @api_method(require_session=True, default_version="v2")
    async def get_reports(
        self,
        *,
        api_version: str = "v2",
    ) -> ReportList:
        """
        Получить список доступных отчетов (v2).
        """
        logger.info("Запрос списка доступных отчетов (v2)")
        raw = await self._request(
            "get",
            "reports",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return decode_model(ReportList, raw.get("data", {}))

    @api_method(require_session=True, default_version="v2")
    async def order_report(
        self,
        *,
        report_id: str,
        format: str,
        params: dict,
        emails: str | None = None,
        api_version: str = "v2",
    ) -> ReportOrderResponse:
        """
        Заказать отчет (на email или по ссылке).
        """
        body = {"id": report_id, "format": format, "params": params}
        if emails:
            body["emails"] = emails

        logger.info("Ordering report format=%s delivery=%s", format, bool(emails))

        raw = await self._request(
            "post",
            "reports",
            api_version=api_version,
            headers=self._headers(include_session=True),
            json=body,
        )
        return decode_model(ReportOrderResponse, raw.get("data", {}))

    @api_method(require_session=True, default_version="v2")
    async def get_report_jobs(
        self,
        *,
        api_version: str = "v2",
    ) -> ReportJobList:
        """
        Получить список заказанных отчетов (v2).
        """
        logger.info("Получение списка заказанных отчетов (v2)")
        raw = await self._request(
            "get",
            "reports/jobs",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return decode_model(ReportJobList, raw.get("data", {}))

    @api_method(require_session=True, default_version="v2")
    async def download_report_file(
        self,
        *,
        job_id: str,
        api_version: str = "v2",
    ) -> bytes:
        """
        Скачать файл отчета (по job_id).

        ⚠️ Важно: успешный запрос возможен только спустя ~300 секунд
        после заказа отчета.
        """
        logger.info("Downloading report version=%s", api_version)

        content = await self.transport.request_stream(
            "get",
            f"/vip/{api_version}/reports/jobs/{job_id}",
            headers=self._headers(include_session=True),
        )

        logger.info("Report downloaded bytes=%s", len(content))
        return content

    # -------- v1 --------
    @api_method(require_session=True, default_version="v1")
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
        api_version: str = "v1",
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

        logger.info("Ordering report version=v1 format=%s", report_format)

        raw = await self._request(
            "get",
            "reports",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return decode_model(ReportV1OrderResponse, {"report_ids": raw.get("data", [])})

    @api_method(require_session=True, default_version="v1")
    async def get_report_job_list_v1(
        self,
        *,
        api_version: str = "v1",
    ) -> ReportV1JobList:
        """
        Получить список заказанных отчетов (v1).
        """
        logger.info("Получение списка заказанных отчетов (v1)")
        raw = await self._request(
            "get",
            "getReportJobList",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return decode_model(ReportV1JobList, {"jobs": raw.get("data", [])})

    @api_method(require_session=True, default_version="v1")
    async def download_report_file_v1(
        self,
        *,
        job_id: str,
        archive: bool = False,
        api_version: str = "v1",
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

        logger.info("Downloading report version=v1 archive=%s", archive)

        content = await self.transport.request_stream(
            "get",
            f"/vip/{api_version}/getReportFile",
            headers=self._headers(include_session=True),
            params=params,
        )

        logger.info("Report downloaded version=v1 bytes=%s", len(content))
        return content
