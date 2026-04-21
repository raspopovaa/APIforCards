# APIClient OPTI24

Async Python SDK for the Opti24 fuel cards API.

The repository is prepared as a standalone demo-ready SDK project:
- packaged with `pyproject.toml`
- runnable through a local `.venv`
- configured for the demo environment
- includes an executable async example

## What Is Included

- `APIClient` with async lifecycle support
- service mixins for auth, cards, transactions, reports, users, limits and other domains
- typed response models on top of `dataclasses` with manual validation
- retry-enabled transport based on `httpx` + built-in async backoff
- demo launcher in [examples/demo_async.py](/Users/andrejraspopov/Documents/New project/api-pro-sdk/examples/demo_async.py)

## Data Description

Each SDK model stores field-level descriptions inside the stdlib-only modeling layer.
You can inspect them programmatically:

```python
from api_client_opti24.models.auth import AuthUserResponse

print(AuthUserResponse.describe())
```

## Demo Configuration

The repo already contains a local `.env` for the demo stand.

Base URL:
- `https://api-demo.opti-24.ru/vip/`

Environment template:
- [`.env.example`](/Users/andrejraspopov/Documents/New project/api-pro-sdk/.env.example)

Local demo config:
- [`.env`](/Users/andrejraspopov/Documents/New project/api-pro-sdk/.env)

## Quick Start

```bash
cd "/Users/andrejraspopov/Documents/New project/api-pro-sdk"
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

Run tests:

```bash
.venv/bin/pytest -q
```

Run the demo script:

```bash
.venv/bin/python examples/demo_async.py
```

## Demo Script Flow

The demo script does the following:
- loads `.env`
- authenticates with the demo user
- prints available contracts
- requests API usage info
- loads the first page of cards
- loads a page of transactions
- logs off cleanly

## Notes

- Use `API_BASE_URL=https://api-demo.opti-24.ru/vip/` in config. The client appends API version paths itself.
- The SDK now auto-closes its underlying `httpx.AsyncClient` via `async with APIClient(...)`.
- Default contract selection after auth uses the first returned contract instead of assuming a second item exists.
