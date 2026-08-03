from ..modeling import BaseModel, Field


class ResponseStatus(BaseModel):
    """Статус ответа API из общего envelope."""

    code: int = Field(..., description="Код выполнения API-операции")


__all__ = ["ResponseStatus"]
