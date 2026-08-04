# Changelog

## 3.0.0 — unreleased

### Changed

- `APIClient.session_id` и `APIClient.contract_id` стали read-only;
- добавлены `select_contract()`, `restore_session()` и `clear_session()`;
- retry ограничен общим deadline и единым attempt budget;
- retry backoff использует full jitter;
- публичные сервисы раньше отклоняют пустые ID, списки и неверную пагинацию.

### Fixed

- batch-операции лимитов и ограничений больше не допускают смешанные договоры;
- timeout попытки не может превышать оставшееся время общей операции.

