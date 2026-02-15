# Open Property Core — Frontend

Vite + React + TypeScript. **Feature-Sliced Design (FSD)** for structure; ESLint and Prettier for code quality. See [docs/FRONTEND_ARCHITECTURE.md](../docs/FRONTEND_ARCHITECTURE.md) for layers and rules.

## Setup

```bash
npm install
```

## Scripts

- `npm run dev` — dev server (port 5173, proxies `/api` to backend)
- `npm run build` — production build
- `npm run preview` — preview production build
- `npm run lint` — ESLint
- `npm run lint:fix` — ESLint with auto-fix
- `npm run format` — Prettier (write)
- `npm run format:check` — Prettier (check only)

Run lint and format before commit: `npm run format:check && npm run lint`.
