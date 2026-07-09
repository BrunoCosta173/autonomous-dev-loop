# Frontend Playbooks

Use this reference for frontend-heavy objectives after reading `stack-detection.md` and `command-discovery.md`.

## General Frontend Flow

1. Inspect package scripts and framework config.
2. Identify package manager from lockfiles.
3. Identify app/workspace boundaries.
4. Run targeted validation first.
5. Run build only when relevant and available.

## React / Vite

Signals:

- `package.json`
- `vite.config.*`
- React dependencies
- `tsconfig.json`

Likely validation:

- package script for `lint`
- package script for `typecheck`
- package script for `test`
- package script for `build`

Prefer scripts such as `npm run build`, `pnpm build`, or the project equivalent over raw `vite build`.

## Next.js

Signals:

- `next.config.*`
- Next dependencies
- `app/` or `pages/`

Likely validation:

- `lint` script, if present
- `typecheck` script, if present
- `test` script, if present
- `build` script for routing/rendering confidence

Do not assume `next lint` exists. Prefer package scripts.

## Vue / Nuxt

Signals:

- `vue.config.*`
- `nuxt.config.*`
- Vue or Nuxt dependencies

Likely validation:

- `lint`
- `typecheck`
- `test`
- `build`

Use project scripts before raw framework commands.

## Angular

Signals:

- `angular.json`
- Angular dependencies

Likely validation:

- `lint`, if configured
- `test`, if configured
- `build`

Prefer package scripts or documented workspace commands.

## Svelte / SvelteKit

Signals:

- `svelte.config.*`
- Svelte/SvelteKit dependencies

Likely validation:

- `check`
- `lint`
- `test`
- `build`

Prefer project scripts.

## Astro

Signals:

- `astro.config.*`
- Astro dependencies

Likely validation:

- `check`, if present
- `lint`, if present
- `test`, if present
- `build`

## UI Change Validation

For UI/UX objectives, prefer:

- Typecheck or framework check
- Component/unit tests when available
- Lint when relevant
- Build for route, bundling, or SSR confidence
- Manual validation notes when no automated command exists

Do not claim visual correctness unless it was actually inspected or validated.
