# Open Property Core

**Property and facility management framework.**  
Self-hosted, open-core, with a "free until $100K revenue" model.

---

## What it is

Open Property Core is not "another real estate CRM" — it's the **core of a digital platform** for:

- **Property management companies** — properties, contracts, payments, accounting
- **Commercial real estate** — offices, warehouses, coworking spaces
- **Colivings and hostels** — bookings, access, billing
- **Proptech** — integration with smart locks, sensors, billing systems

The model is like GitLab: one codebase, different "tiers" — free core for small business, paid features for scale and compliance.

---

## License and model

| Tier | Who | Terms |
|------|-----|-------|
| **Community** | Everyone | Free forever when revenue &lt; $100K/year |
| **Enterprise** | Large business, compliance | License + support, SLA, legal liability |

- **Core:** [Business Source License (BSL)](LICENSE) with automatic conversion to Apache 2.0 after 4 years.
- **Details:** [docs/LICENSE.md](docs/LICENSE.md).

---

## Stack

- **Backend:** Django 5 + Django REST Framework + Celery
- **Frontend:** Vite + React + TypeScript (ESLint, Prettier)
- **Database:** PostgreSQL
- **Queues:** Redis (Celery broker)
- **Self-hosted:** Docker Compose out of the box

---

## Documentation

| Document | Description |
|----------|-------------|
| [First Steps](docs/FIRST_STEPS.md) | What to do first: repository, license, scaffolding |
| [Architecture](docs/ARCHITECTURE.md) | Modules, boundaries, API, integrations |
| [Roadmap](docs/ROADMAP.md) | Community vs Enterprise, development phases |
| [License](docs/LICENSE.md) | BSL, thresholds, commercial use |
| [Contributing](docs/CONTRIBUTING.md) | CLA, branches, code review |

---

## Quick start

```bash
git clone https://github.com/Open-property-core/core.git
cd openpropertycore
cp .env.example .env
docker compose up -d
```

**Local development (backend):** dependencies via [uv](https://docs.astral.sh/uv/) by default:

```bash
cd backend
uv sync
source .venv/bin/activate   # or on Windows: .venv\Scripts\activate
python manage.py runserver
```

With dev tools (Black, isort, flake8, mypy, pytest): `uv sync --extra dev`, then `make format`, `make lint`, `make typecheck`, `make test` (or `make check` — all at once). Tests use SQLite in-memory (`opc.settings_test`), no PostgreSQL needed. Alternatively: `uv pip install -r requirements.txt` in your venv. Docker build already uses uv.

Host ports (non-default to avoid conflicts with other projects):

- **API:** http://localhost:8080/api/v1/ (JWT: `POST /api/v1/token/` with `username`/`password`)
- **OpenAPI schema:** http://localhost:8080/api/schema/
- **Django Admin:** http://localhost:8080/admin/ (create superuser: `docker compose run --no-deps backend python manage.py createsuperuser`)
- **Celery test:** `POST http://localhost:8080/api/v1/trigger-hello-celery/`
- **PostgreSQL:** localhost:5433 (credentials in `.env`)
- **Redis:** localhost:6380

Containers run without `restart: always` — they stop with `docker compose down`.

**Tests (backend):** `cd backend && uv sync --extra dev && uv run pytest`. **Frontend:** in `frontend/` — `npm install && npm run dev`. Lint and format: `npm run lint`, `npm run format` / `npm run format:check`. See [frontend/README.md](frontend/README.md).

**CI:** on push/PR, [.github/workflows/ci.yml](.github/workflows/ci.yml) runs (backend: pytest, black, isort, flake8; frontend: eslint, prettier).

**E2E tests:** see [frontend/e2e/README.md](frontend/e2e/README.md). Run `npm run e2e` in `frontend/` (requires backend + frontend running).

---

## Contact

- Issues / discussion: GitHub Issues
- Documentation and product decisions — in the `docs/` folder
