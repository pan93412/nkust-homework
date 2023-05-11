# Futtes – A basic template of a test

## Tech stack

- TypeScript
- Web Component (`lit`)
- Vite
- UnoCSS

For testing:

- Vitest for Unit Test
- Playwright for E2E Test

For code quality assuring:

- ESLint
- Prettier

## Workflow

```bash
# lint and format code
pnpm lint && pnpm fmt

# run tests
pnpm test:unit
pnpm test:e2e

# remember to commit the changes
git commit -am "..."

# build
pnpm build

# copy the source to the dist folder
name=$(jq -r ".name" package.json)
git archive HEAD --format=zip --output answers/$name-src.zip
cp README.md answers/$name/README.md
# the answers folder is the artifact.
```
