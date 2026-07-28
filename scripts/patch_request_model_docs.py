from __future__ import annotations

from pathlib import Path


def main() -> None:
    renderer_path = Path("scripts/pydantic_docs.py")
    renderer = renderer_path.read_text(encoding="utf-8")
    old = '''    model_kind = "request" if issubclass(model, StrictRequestModel) else "response/data"

    lines = [
        f"# `{model.__name__}`",
        "",
        description,
        "",
        '!!! info "Назначение Pydantic"',
        f"    Тип модели: **{model_kind}**. Данные проверяются вызовом "
        f"`{model.__name__}.model_validate(payload)`. При несовпадении типов или отсутствии "
        "обязательного поля Pydantic формирует `ValidationError`.",
'''
    new = '''    is_request_model = issubclass(model, StrictRequestModel)
    model_kind = "request" if is_request_model else "response/data"
    if is_request_model:
        validation_notice = (
            f"    Тип модели: **{model_kind}**. Правила ниже применяются, когда вызывающий код "
            f"явно создаёт `{model.__name__}` или вызывает "
            f"`{model.__name__}.model_validate(payload)`. Наличие request-модели не означает, "
            "что каждый метод SDK автоматически создаёт её: фактический входной контракт "
            "определяется сигнатурой соответствующего сервисного метода."
        )
    else:
        validation_notice = (
            f"    Тип модели: **{model_kind}**. Ответ API проверяется этой моделью напрямую "
            "или рекурсивно как часть родительской response-модели. При несовпадении типов "
            "или отсутствии обязательного поля Pydantic формирует `ValidationError`."
        )

    lines = [
        f"# `{model.__name__}`",
        "",
        description,
        "",
        '!!! info "Назначение Pydantic"',
        validation_notice,
'''
    if old not in renderer:
        raise RuntimeError("Expected model validation notice was not found")
    renderer_path.write_text(renderer.replace(old, new), encoding="utf-8")

    test_path = Path("tests/test_documentation_generator.py")
    tests = test_path.read_text(encoding="utf-8")
    test_name = "test_request_models_do_not_claim_automatic_sdk_validation"
    if test_name not in tests:
        tests += '''


def test_request_models_do_not_claim_automatic_sdk_validation() -> None:
    generator = load_generator()
    output = generator.build_all()
    request_page = output[
        generator.DATA_TYPES_PATH / "final_prices" / "CheckPurchaseRequest.md"
    ]

    assert "явно создаёт `CheckPurchaseRequest`" in request_page
    assert "не означает, что каждый метод SDK автоматически создаёт её" in request_page
    assert "фактический входной контракт" in request_page
'''
        test_path.write_text(tests, encoding="utf-8")


if __name__ == "__main__":
    main()
