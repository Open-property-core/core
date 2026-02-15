# Frontend: Feature-Sliced Design (FSD)

Фронтенд строится по [Feature-Sliced Design](https://feature-sliced.design/): слои, слайсы, сегменты и правило изолированности слоёв.

---

## Слои (сверху вниз)

Зависимости идут только **вниз**: слой может импортировать только из нижележащих слоёв.

| Слой | Назначение | Пример |
|------|------------|--------|
| **app** | Инициализация приложения: провайдеры, роутер, глобальные стили | `App.tsx`, `router`, `providers` |
| **processes** | (опционально) Сложные межстраничные сценарии | Онбординг, многошаговая форма |
| **pages** | Страницы приложения; композиция виджетов и фич | `HomePage`, `PropertyListPage` |
| **widgets** | Составные блоки UI из фич и сущностей | `Header`, `PropertyCard` |
| **features** | Действия пользователя, интерактивность | `createContract`, `filterProperties` |
| **entities** | Бизнес-сущности: типы, API, отображение сущности | `Property`, `Contract`, `Party` |
| **shared** | Переиспользуемый код без бизнес-логики: UI-kit, API-клиент, lib | `Button`, `api`, `utils` |

---

## Структура папок (`frontend/src/`)

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
  widgets/             # (по мере появления)
  features/            # (по мере появления)
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

В каждом слайсе (например `entities/property/`): **api**, **model**, **ui**, при необходимости **config**; снаружи импортируется только через **public API** (`index.ts`).

---

## Правила

1. **Публичный API слайса** — один вход: `entities/property/index.ts` реэкспортирует только то, что разрешено использовать выше. Внутренности слайса не импортируются с других слоёв.
2. **Сегменты внутри слайса:** `ui` (компоненты), `model` (состояние, типы), `api` (запросы), `lib` (вспомогательное). Не все сегменты обязательны.
3. **Один уровень вложенности внутри слоя** — слайс один уровень (например `entities/property`), внутри него сегменты `ui`, `model`, `api`.
4. **Shared** — без импортов из `entities`, `features`, `pages`, `app`. Только нейтральные компоненты и утилиты.

---

## Импорты

- Разрешено: из нижележащего слоя и из текущего слайса.
- Запрещено: из вышележащего слоя; обход public API слайса (импорт из `entities/property/ui` из `pages` вместо `entities/property`).

---

## Ссылки

- [Feature-Sliced Design — официальная документация](https://feature-sliced.design/)
- Структура репозитория: `frontend/src/` — соответствие слоям FSD.
