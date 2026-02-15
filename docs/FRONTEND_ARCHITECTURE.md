# Frontend: Feature-Sliced Design (FSD)

The frontend follows [Feature-Sliced Design](https://feature-sliced.design/): layers, slices, segments, and the rule of layer isolation.

---

## Layers (top to bottom)

Dependencies go only **downward**: a layer may import only from lower layers.

| Layer | Purpose | Example |
|-------|---------|---------|
| **app** | Application init: providers, router, global styles | `App.tsx`, `router`, `providers` |
| **processes** | (optional) Complex cross-page flows | Onboarding, multi-step form |
| **pages** | Application pages; composition of widgets and features | `HomePage`, `PropertyListPage` |
| **widgets** | Composite UI blocks from features and entities | `Header`, `PropertyCard` |
| **features** | User actions, interactivity | `createContract`, `filterProperties` |
| **entities** | Business entities: types, API, entity display | `Property`, `Contract`, `Party` |
| **shared** | Reusable code without business logic: UI kit, API client, lib | `Button`, `api`, `utils` |

---

## Folder structure (`frontend/src/`)

```
src/
  app/                 # app layer
    App.tsx
    index.css
    providers.tsx
    router.tsx
  pages/               # pages layer
    home/
      ui/
      index.ts
  widgets/             # (as needed)
  features/            # (as needed)
  entities/            # entities layer
    property/
      api/
      model/
      ui/
      index.ts
    contract/
    party/
  shared/
    api/               # base client, types from OpenAPI
    ui/                # Button, Input, Layout...
    lib/               # utils, constants
```

In each slice (e.g. `entities/property/`): **api**, **model**, **ui**, and **config** if needed; externally imported only via **public API** (`index.ts`).

---

## Rules

1. **Slice public API** — single entry: `entities/property/index.ts` re-exports only what other layers may use. Internal parts of the slice are not imported from other layers.
2. **Segments inside a slice:** `ui` (components), `model` (state, types), `api` (requests), `lib` (helpers). Not all segments are required.
3. **One nesting level per layer** — slice is one level (e.g. `entities/property`), inside it segments `ui`, `model`, `api`.
4. **Shared** — no imports from `entities`, `features`, `pages`, `app`. Only neutral components and utilities.

---

## Imports

- Allowed: from a lower layer and from the current slice.
- Forbidden: from an upper layer; bypassing the slice public API (e.g. importing from `entities/property/ui` from `pages` instead of `entities/property`).

---

## References

- [Feature-Sliced Design — official documentation](https://feature-sliced.design/)
- Repository structure: `frontend/src/` — follows FSD layers.
