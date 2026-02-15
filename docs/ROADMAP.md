# Open Property Core Roadmap

Split between Community (free when revenue < $100K/year) and Enterprise (license + support). Features in Community are **never** moved to paid — only new capabilities are added on top.

---

## Phase 0: Kickoff (current)

**Goal:** legal foundation, repository scaffold, first end-to-end scenario.

| Task | Assignment | Status |
|------|------------|--------|
| Repository, README, documentation | — | Done |
| LICENSE (BSL), $100K threshold | Community | Done |
| CLA for contributors | — | Done (docs/CLA.md) |
| Stack: Django, DRF, Celery, PostgreSQL, Docker | — | Done |
| Entities: Property, Unit, Party, Contract | Community | Done |
| CRUD API + one end-to-end scenario | Community | Done |
| Basic launch via docker-compose | Community | Done |
| First e2e scenario (optional) | — | Done (Playwright) |

---

## Phase 1: Community MVP (1–3 months)

**Goal:** a product you can deploy and use for properties and contract management.

| Feature | Description | Module | Status |
|---------|-------------|--------|--------|
| Properties and units | Full CRUD, types, statuses, area | Property | Done |
| Counterparties | Individuals and legal entities, contacts, roles | Party | Done |
| Contracts | Create, dates, amount, statuses | Contract | Done |
| Simple invoicing and payments | Record payment against contract | Billing | Done (Invoice, Payment) |
| Basic admin UI | Lists and forms for above entities | Admin UI | Django Admin + React Properties, Parties, Contracts |
| Authentication and roles | Login, roles (admin, manager), basic RBAC | Core | Done (JWT, login page) |
| DB migrations | Versioned migrations | Core | Done |
| API documentation | OpenAPI/Swagger | Core | Done |

All above — **in Community forever**, free under BSL terms.

---

## Phase 2: Stability and expansion (3–6 months)

| Feature | Description | Community / Enterprise |
|---------|-------------|------------------------|
| Tenant portal | View contract, invoices, requests | Community |
| Notifications | Email/system notifications (email on contract created; deadlines and payments next) | Community |
| Basic reports | Exports, simple reports on properties and payments | Community |
| File storage | Documents for properties and contracts (S3-compatible) | Community |
| Webhooks | Outbound events (contract created, payment received) | Community |
| Advanced RBAC | Flexible roles and permissions | Enterprise |
| Change audit | Log who/when/what changed for key entities | Enterprise |

---

## Phase 3: Proptech and compliance (6–12 months)

| Feature | Description | Community / Enterprise |
|---------|-------------|------------------------|
| Integrations: smart locks, sensors | Adapters for access and monitoring | Enterprise |
| Legally binding document flow | Templates, signing, storage | Enterprise |
| 1C / bank integration | Exports, reconciliation, payments | Enterprise |
| Regulatory reporting (NIS2, etc.) | Reports and exports for compliance | Enterprise |
| SLA and priority support | Contract, uptime guarantees | Enterprise |

---

## Principles

1. **Never take from Community** — paid features are only additions.
2. **Boundary by "role"** — what developers/small business need → Community; what legal, security, scale need → Enterprise.
3. **Self-hosted first** — cloud SaaS (if any) is built on top of the same code.
4. **Transparency** — roadmap and handbook are public; license changes — announced in advance with BSL → Apache 2.0 conversion preserved.

Current priority: finish Phase 0 and solidify Phase 1 in code and documentation.
