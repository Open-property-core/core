# Open Property Core

**Фреймворк для управления недвижимостью (Property / Facility Management).**  
Self-hosted, open-core, с моделью «бесплатно до $100K выручки».

---

## Что это

Open Property Core — это не «ещё один CRM для риелторов», а **ядро цифровой платформы** для:

- **Управляющих компаний** — объекты, договоры, платежи, учёт
- **Коммерческой аренды** — офисы, склады, коворкинги
- **Коливингов и хостелов** — бронирования, доступ, биллинг
- **Proptech** — интеграция с умными замками, датчиками, биллингом

Модель как у GitLab: один код, разные «роли» — бесплатное ядро для малого бизнеса, платные возможности для масштаба и комплаенса.

---

## Лицензия и модель

| Уровень | Кто | Условия |
|--------|-----|--------|
| **Community** | Все | Бесплатно навсегда при выручке &lt; $100K/год |
| **Enterprise** | Крупный бизнес, комплаенс | Лицензия + поддержка, SLA, юридическая ответственность |

- **Ядро:** [Business Source License (BSL)](LICENSE) с автоматической конвертацией в Apache 2.0 через 4 года.
- **Детали:** [docs/LICENSE.md](docs/LICENSE.md).

---

## Стек

- **Backend:** Django 5 + Django REST Framework + Celery
- **Frontend:** Vite + React + TypeScript (ESLint, Prettier)
- **БД:** PostgreSQL
- **Очереди:** Redis (Celery broker)
- **Self-hosted:** Docker Compose из коробки

---

## Документация

| Документ | Описание |
|----------|----------|
| [Первые шаги](docs/FIRST_STEPS.md) | Что сделать в первую очередь: репозиторий, лицензия, каркас |
| [Архитектура](docs/ARCHITECTURE.md) | Модули, границы, API, интеграции |
| [Дорожная карта](docs/ROADMAP.md) | Community vs Enterprise, фазы развития |
| [Лицензия](docs/LICENSE.md) | BSL, пороги, коммерческое использование |
| [Участие](docs/CONTRIBUTING.md) | CLA, ветки, код-ревью |

---

## Быстрый старт

```bash
git clone https://github.com/your-org/openpropertycore.git
cd openpropertycore
cp .env.example .env
docker compose up -d
```

**Локальная разработка (backend):** зависимости ставим через [uv](https://docs.astral.sh/uv/) по умолчанию:

```bash
cd backend
uv sync
source .venv/bin/activate   # или на Windows: .venv\Scripts\activate
python manage.py runserver
```

С dev-инструментами (Black, isort, flake8, mypy, pytest): `uv sync --extra dev`, затем `make format`, `make lint`, `make typecheck`, `make test` (или `make check` — всё сразу). Тесты используют SQLite in-memory (`opc.settings_test`), без PostgreSQL. Либо классически: `uv pip install -r requirements.txt` в своём venv. В Docker образе сборка уже идёт через uv.

Порты на хосте (не дефолтные, чтобы не конфликтовать с другими проектами):

- **API:** http://localhost:8080/api/v1/ (JWT: `POST /api/v1/token/` с `username`/`password`)
- **OpenAPI schema:** http://localhost:8080/api/schema/
- **Django Admin:** http://localhost:8080/admin/ (создайте суперпользователя: `docker compose run --no-deps backend python manage.py createsuperuser`)
- **Проверка Celery:** `POST http://localhost:8080/api/v1/trigger-hello-celery/`
- **PostgreSQL:** localhost:5433 (логин/пароль из `.env`)
- **Redis:** localhost:6380

Контейнеры без `restart: always` — останавливаются по `docker compose down`.

**Тесты (backend):** `cd backend && uv sync --extra dev && uv run pytest`. **Frontend:** в `frontend/` — `npm install && npm run dev`. Линт и формат: `npm run lint`, `npm run format` / `npm run format:check`. См. [frontend/README.md](frontend/README.md).

**CI:** на push/PR запускается [.github/workflows/ci.yml](.github/workflows/ci.yml) (backend: pytest, black, isort, flake8; frontend: eslint, prettier).

---

## Контакты

- Issues / обсуждение: GitHub Issues (после создания репозитория)
- Документация и решения по продукту — в папке `docs/`
