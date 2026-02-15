# Open Property Core Architecture

This document describes the high-level architecture: modules, boundaries, technologies, and principles. Implementation details — in code and ADRs (Architecture Decision Records) when they appear.

- **Frontend:** [Feature-Sliced Design](FRONTEND_ARCHITECTURE.md) — layers app → pages → widgets → features → entities → shared.
- **Backend (DRF):** [DDD Django-style](BACKEND_ARCHITECTURE.md) — bounded contexts (Django apps), services, thin API layer.

---

## Goals and constraints

- **Self-hosted first** — deploy at the customer or in your own cloud without vendor lock-in.
- **Open core** — core under BSL, transparent Community / Enterprise boundary.
- **Proptech-ready** — properties, contracts, payments; room for integrations (IoT, smart locks, billing).
- **Compliance** — in Enterprise: audit, document flow, reporting (NIS2, etc.).

---

## High-level diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     Clients / Integrations                        │
└─────────────────────────────────────────────────────────────────┘
                    │                    │                    │
                    ▼                    ▼                    ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Admin UI   │  │ Tenant Portal│  │  REST API    │  │  Webhooks /  │
│  (React/Vue) │  │ (optional)   │  │(Django/Nest) │  │  Integrations │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │                 │
       └─────────────────┴────────┬────────┴─────────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │      Application Core     │
                    │  (Domain + Use Cases)     │
                    └─────────────┬─────────────┘
                                  │
       ┌─────────────────────────┼─────────────────────────┐
       │                         │                         │
       ▼                         ▼                         ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  PostgreSQL  │  │    Redis     │  │   Queues     │  │  File Store  │
│  (primary    │  │  (cache,     │  │  (background │  │  (S3-compat) │
│   data)      │  │   sessions)  │  │   tasks)     │  │              │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
```

---

## Backend stack choice: Django vs NestJS

Both suit Open Property Core. Summary below; the choice can be recorded in an ADR on first commit.

| Criterion | Django (Python) | NestJS (Node.js/TypeScript) |
|-----------|-----------------|-----------------------------|
| **Speed to MVP** | Higher: Django Admin out of the box, DRF, migrations, admin in hours | Need separate admin (React/Vue) or use AdminJS |
| **Admin UI** | Built-in, extensible (custom forms, actions, permissions) | Separate SPA or third-party (AdminJS, React-Admin) |
| **API** | DRF: serializers, ViewSet, OpenAPI via drf-spectacular | Controllers, DTO, Swagger built-in, strong typing |
| **Queues/background** | Celery + Redis — standard, mature | Bull/BullMQ — native for Node, single runtime easier |
| **Typing** | Optional (type hints, mypy) | TypeScript by default, stricter at compile time |
| **B2B/ERP ecosystem** | Closer: ERPNext (Frappe), reporting/integrations in Python | Many SaaS/APIs on Node; heavy logic often uses Python |
| **Single runtime** | No: API in Python, frontend in JS — two stacks | Yes: backend and frontend on JS/TS, shared types in monorepo |
| **Proptech / IoT** | Good: asyncio, protocol libraries, scripts | Good: event model, streams, real-time |
| **Hosting** | Any VPS with Python; less memory per process than Node at similar load | Same; Node scales well by instance count |

**When Django makes more sense:**

- You want to reach production faster with a working admin and CRUD without separate frontend work.
- You plan heavy reporting, 1C/accounting integrations, scripts — Python ecosystem often simplifies this.
- You or your team are stronger in Python.

**When NestJS makes more sense:**

- You want one language (TypeScript) for API and frontend, shared types and monorepo.
- Focus on modern SPA (React/Vue) from the start, custom admin.
- Experience and preference for Node/TS.

**Recommendation for Open Property Core:** if priority is fast start and "admin out of the box", **Django + DRF** wins on time. If unified TypeScript stack and custom UI matter more — **NestJS**. Both stacks allow the same domain model and module boundaries from this document.

---

## Target stack

Below — two viable backends; pick one for implementation.

| Layer | Option A (Django) | Option B (NestJS) | Common |
|-------|-------------------|-------------------|--------|
| Backend | Python 3.11+, Django 5.x, Django REST Framework | Node.js 20+, NestJS, TypeScript | — |
| API | REST, drf-spectacular (OpenAPI 3) | REST, Swagger/OpenAPI | Versioning `/api/v1/...` |
| Admin UI | Django Admin (extensible) or separate SPA | React/Vue + component library | — |
| Database | PostgreSQL (Django ORM, migrations) | PostgreSQL (TypeORM/Prisma/Drizzle) | Same domain schema |
| Queues | Celery + Redis | Bull/BullMQ + Redis | Background, deferred tasks |
| Files | django-storages (S3-compatible) | Multer + S3 SDK or similar | MinIO / AWS S3 |
| Deployment | Docker, docker-compose | Docker, docker-compose | Self-hosted out of the box |

---

## Domain modules (core)

Module boundaries follow the domain, not technical layers.

### 1. Property (Real estate objects)

- **Entities:** Property, Unit (room/unit in a property), Building (if needed).
- **Responsibility:** catalog of properties and units, types, statuses, area, address.
- **Integrations (Enterprise):** geocoding, cadastre (if needed).

### 2. Party (Counterparties)

- **Entities:** Party (individual or legal entity), contacts, roles (tenant, landlord, property manager).
- **Responsibility:** unified counterparty catalog for contracts and payments.

### 3. Contract (Contracts)

- **Entities:** Contract, terms (dates, amount, frequency), statuses (draft, active, terminated).
- **Responsibility:** contract lifecycle for leases/services.
- **Enterprise:** legally binding document flow, templates, signing.

### 4. Billing & Payments

- **Entities:** Invoice, Payment, rates, charges.
- **Responsibility:** invoicing and payment tracking, link to contracts.
- **Enterprise:** bank integration, cash register, reporting.

### 5. Integrations

- **Responsibility:** webhooks, outbound APIs, adapters for external systems (1C, smart locks, billing).
- **Enterprise:** priority for IoT and compliance reporting.

Modules communicate via domain events and application services; direct dependencies between aggregates are minimized.

---

## API

- **REST** with versioning in URL or header (`/api/v1/...`).
- **OpenAPI 3** — description required, client and docs generation.
- **Authentication:** JWT or sessions; for Enterprise — SSO/SAML.
- **Multi-tenancy:** at first — one tenant per instance; later — tenant_id in context (organization).

---

## Security and compliance (Enterprise)

- Audit of changes to critical entities (who, when, what).
- Roles and permissions (RBAC) — basic model in core, detailed for NIS2/compliance in Enterprise.
- Encryption of sensitive data (as needed).
- SBOM and dependency transparency — for enterprise customers.

---

## Scaling (later)

- Horizontal scaling of API behind a load balancer.
- Queues — dedicated workers.
- Database — replication; at scale — partitioning by tenant_id or time.

Current focus — correct domain model and first working scenario; scaling is designed in without premature complexity.
