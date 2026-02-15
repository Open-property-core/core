# E2E Tests

Run the core flow e2e test with Playwright.

## Prerequisites

1. Start the backend: `docker compose up -d` (from project root)
2. Create a superuser: `docker compose run --no-deps backend python manage.py createsuperuser` (e.g. username: admin, password: admin)
3. Start the frontend: `npm run dev` (in frontend/)
4. Run e2e: `npm run e2e` (in frontend/)

## Environment

- `E2E_BASE_URL` — frontend URL (default: http://localhost:5173)
- `E2E_API_BASE` — API base URL (default: http://localhost:8080/api/v1)
- `E2E_USER` / `E2E_PASSWORD` — login credentials (default: admin/admin)
