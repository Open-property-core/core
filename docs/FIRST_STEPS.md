# First Steps — Open Property Core

A step-by-step plan to go from "empty repository" to a first working scaffold in 2–4 weeks.

---

## Phase 0: Legal and organizational foundation (1–3 days)

### 1. Repository and visibility

- [ ] Create a Git repository (GitHub/GitLab).
- [ ] Add description and tags: `property-management`, `proptech`, `open-core`, `bsl`, `self-hosted`.
- [ ] Decide: public from day one or private until first release (recommended: public — faster trust and contributors).

### 2. License

- [ ] Add a `LICENSE` file in the root with BSL text (see [docs/LICENSE.md](LICENSE.md)).
- [ ] Clearly state in README: "Community is free when revenue < $100K/year".
- [ ] Optional: fix the BSL → Apache 2.0 conversion date (e.g., "4 years from the date of first public release").

### 3. CLA (Contributor License Agreement)

- [ ] Choose a CLA template (e.g., Harmony CLA or similar).
- [ ] Add `CLA.md` or `docs/CLA.md` in the repository with text and instructions to "sign before first merge".
- [ ] Set up verification (bot or manual): do not merge PRs without signed CLA.

Without CLA you cannot safely relicense code for Enterprise.

---

## Phase 1: Product scaffold (1–2 weeks)

### 4. Stack and repository structure

- [ ] Document in `docs/ARCHITECTURE.md` (and ADR if needed) the backend choice:
  - **Django** — faster MVP with Django Admin and DRF; good for reporting and integrations (1C, Python ecosystem).
  - **NestJS** — unified TypeScript stack with frontend; custom admin from scratch.
  - Frontend: with Django — built-in admin or separate SPA; with NestJS — React/Vue + UI library.
  - DB: PostgreSQL. Queues: Celery (Django) or Bull/BullMQ (NestJS).
- [ ] Create monorepo or separate repositories:
  - `apps/api` — REST/GraphQL API.
  - `apps/admin` — admin UI.
  - `apps/tenant-portal` (optional) — tenant portal.
  - `packages/shared` — shared types, constants, utilities.

### 5. Minimal API and DB

- [ ] Set up the project (e.g. `nest new`, or a Docker template).
- [ ] Add Docker/docker-compose: API + PostgreSQL (and Redis for queues if needed).
- [ ] Design and implement the first domain entities:
  - **Property** (real estate object): id, name, address, type, status.
  - **Unit** (unit/room within a property): id, property_id, name, area, status.
  - **Party** (counterparty: tenant/landlord): id, name, type, contacts.
  - **Contract**: id, unit_id, party_id, dates, amount, status.
- [ ] Migrations (TypeORM/Prisma/Drizzle — as preferred), schema only, no heavy business logic.

### 6. First end-to-end scenario

- [ ] Implement: create property → create unit → create party → create contract (CRUD via API).
- [ ] Add tests (unit + at least one e2e for this scenario).
- [ ] Document in README or `docs/GETTING_STARTED.md`: how to run the environment and execute the scenario via curl/Postman.

Goal: any developer can clone the repository and see a working flow in 15 minutes.

---

## Phase 2: Documentation and packaging (3–5 days)

### 7. Public documentation

- [ ] `docs/ARCHITECTURE.md` — modules, boundaries, key decisions (started above).
- [ ] `docs/ROADMAP.md` — what's in Community, what's planned for Enterprise, by phase.
- [ ] `docs/API.md` or OpenAPI/Swagger — endpoint description (can be generated from code).
- [ ] `CONTRIBUTING.md` — how to fork, branches, code review, CLA (see [docs/CONTRIBUTING.md](CONTRIBUTING.md)).

### 8. "Zero" release

- [ ] Versioning: semantic versioning (SemVer), Git tag (e.g. `v0.1.0`).
- [ ] Changelog: `CHANGELOG.md` with section for v0.1.0 ("Initial skeleton: properties, units, contracts").
- [ ] One-command build and run: `docker-compose up` or `make up` — no manual steps for the basic scenario.

---

## "First commit" checklist

Before considering "first steps" complete:

| # | Action | Done |
|---|--------|------|
| 1 | Repository created, README and docs in place | ☐ |
| 2 | LICENSE (BSL) and $100K threshold documented | ☐ |
| 3 | CLA chosen and added to repo | ☐ |
| 4 | Stack documented in ARCHITECTURE.md | ☐ |
| 5 | API + DB scaffold (properties, units, contracts) | ☐ |
| 6 | One end-to-end scenario working and documented | ☐ |
| 7 | Docker/docker-compose runs the project | ☐ |
| 8 | ROADMAP and CONTRIBUTING filled out | ☐ |

---

## What to do after first steps

- Start attracting first users/contributors (communities, proptech chats).
- Collect 2–3 implementation cases ("on ourselves" or pilot clients).
- Introduce Enterprise features only after Community stabilizes (see [ROADMAP.md](ROADMAP.md)).

Next — [Architecture](ARCHITECTURE.md) and [Roadmap](ROADMAP.md).
