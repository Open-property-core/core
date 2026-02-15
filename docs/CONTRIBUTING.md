# Contributing to Open Property Core

Thank you for your interest in Open Property Core. Below is how to propose changes and what we expect from you.

---

## CLA (Contributor License Agreement)

**You must sign the CLA before your first PR is accepted.**

- Without a signed CLA we cannot safely relicense code (including BSL → Apache 2.0 conversion).
- CLA text: [docs/CLA.md](CLA.md).
- Sign once (state in the PR description "I agree to the CLA in docs/CLA.md") — you can then send patches without signing again (unless CLA terms change).

**PRs without CLA agreement are not accepted.** In your first PR, include in the description: "I agree to the CLA in docs/CLA.md".

---

## How to propose a change

1. **Fork** the repository.
2. Create a **branch** from `main` (or the current development branch):
   - `feature/short-description` — new feature
   - `fix/short-description` — bug fix
   - `docs/short-description` — documentation only
3. Make changes following the project's code style and conventions.
4. Add/update tests if logic is changed.
5. Ensure linters and tests pass (see README or CI).
6. Create a **Pull Request** to `main` (or the target branch from the repo description).
7. In the PR description include:
   - what was done and why;
   - link to issue (if any);
   - that you have signed the CLA.

We review PRs in a reasonable timeframe; revisions based on feedback are possible.

---

## Code standards

- Style and formatting — per project rules (e.g. ESLint/Prettier for JS/TS; configs in the repo).
- Commits — meaningful messages; use English where possible for consistency.
- One PR — one logical change; split large features into multiple PRs.

Details (formatting, tests, types) are in README and root configs as the codebase evolves.

---

## Questions and discussion

- **Bug reports and feature requests** — via GitHub Issues (or the channel indicated in README).
- **Architecture and roadmap questions** — also via Issues or repository discussions.

We aim to respond in a reasonable time; delays may occur under high load.

---

## License of your contribution

By submitting code or documentation, you agree that your contribution will be distributed under the same license as the project (BSL with future conversion to Apache 2.0), in accordance with the signed CLA.
