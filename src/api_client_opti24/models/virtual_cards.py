from typing import Optional

from ..modeling import BaseModel, Field

# ======== Общие структуры ========


class StatusModel(BaseModel):
    code: int = Field(..., description="Код статуса ответа (200 — успешно, иное — ошибка)")


# ======== Модели данных виртуальной карты ========


class VirtualCardData(BaseModel):
    id: str = Field(..., description="ID виртуальной карты")
    number: str = Field(..., description="Номер виртуальной карты")
    carrier: str = Field(..., description="Тип носителя, обычно 'Virtual Card'")
    product: str = Field(..., description="Тип продукта карты ('wallet' или 'limit')")
    status: str = Field(..., description="Статус карты (например, 'Active', 'Blocked', 'Pending')")


class VirtualCardResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус ответа от сервера")
    data: VirtualCardData = Field(..., description="Информация о выпущенной виртуальной карте")
    timestamp: int = Field(..., description="Время ответа сервера в формате Unix Timestamp")


# ======== Упрощённый ответ с булевым результатом ========


class SimpleActionResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус выполнения операции")
    data: bool = Field(..., description="Результат операции (True — успешно)")
    timestamp: int = Field(..., description="Время выполнения запроса (Unix Timestamp)")


# ======== Подтверждение выпуска ВК (через СМС) ========


class ConfirmVirtualCardRequest(BaseModel):
    card_id: str = Field(..., description="ID виртуальной карты для подтверждения выпуска")
    code: str = Field(..., description="Код подтверждения из СМС")


class ConfirmVirtualCardResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус подтверждения выпуска")
    data: bool = Field(..., description="Результат подтверждения (True — успешно)")
    timestamp: int = Field(..., description="Время выполнения запроса (Unix Timestamp)")


# ======== Повторная отправка СМС-кода ========


class ResendSMSRequest(BaseModel):
    card_id: str = Field(
        ...,
        description="ID виртуальной карты, для которой нужно повторно отправить СМС-код",
    )


class ResendSMSResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус запроса на повторную отправку СМС-кода")
    data: bool = Field(..., description="Результат операции (True — СМС отправлено успешно)")
    timestamp: int = Field(..., description="Время выполнения запроса (Unix Timestamp)")


# ======== Удаление МПК ========


class DeleteMPCResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус удаления мобильного профиля карты (МПК)")
    data: bool = Field(..., description="Результат удаления (True — успешно)")
    timestamp: int = Field(..., description="Время выполнения запроса (Unix Timestamp)")


# ======== Сброс МПК ========


class ResetMPCRequest(BaseModel):
    type: str = Field(..., description="Тип операции сброса ('ResetCounterCode' и т.п.)")


class ResetMPCResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус выполнения операции сброса")
    data: bool = Field(..., description="Результат операции (True — успешно)")
    timestamp: int = Field(..., description="Время выполнения запроса (Unix Timestamp)")


# ======== Перезапуск выпуска (повторная генерация ВК) ========


class RerunVirtualCardReleaseRequest(BaseModel):
    card_id: str = Field(..., description="ID виртуальной карты для перезапуска выпуска")
    reason: Optional[str] = Field(None, description="Причина перезапуска выпуска (опционально)")


class RerunVirtualCardReleaseResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус перезапуска выпуска карты")
    data: VirtualCardData = Field(..., description="Обновлённая информация о виртуальной карте")
    timestamp: int = Field(..., description="Время выполнения запроса (Unix Timestamp)")


# ======== Удаление виртуальной карты ========


class DeleteVirtualCardResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус удаления виртуальной карты")
    data: bool = Field(..., description="Результат удаления карты (True — успешно)")
    timestamp: int = Field(..., description="Время выполнения запроса (Unix Timestamp)")


# ======== Общая модель успешного действия ========


class MPCActionResponse(BaseModel):
    status: StatusModel = Field(..., description="Статус выполнения операции с МПК")
    data: bool = Field(..., description="Результат выполнения операции (True — успешно)")
    timestamp: int = Field(..., description="Время выполнения запроса (Unix Timestamp)")
