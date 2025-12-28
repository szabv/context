# Drizzle cookbook (repo-specific)

## Goal
Use Drizzle Kit to generate and apply SQL migrations for this repo.

## Configuration checklist
- `drizzle.config.ts`
  - `dialect: "postgresql"`
  - `schema: "./src/db/schema.ts"`
  - `out: "./src/db/migrations"`
  - `dbCredentials.url` uses `DATABASE_URL_UNPOOLED` (fallback `DATABASE_URL`)
- `.env` has a valid `DATABASE_URL_UNPOOLED` (or `DATABASE_URL`).

## Commands (npm)
- Generate migrations from schema:
  ```bash
  npx drizzle-kit generate --name <name>
  ```
- Apply migrations:
  ```bash
  npm run db:migrate:drizzle
  ```

## First-time setup on an existing database
If the schema already exists (for example created via `psql`), you still need
Drizzle Kit metadata before `drizzle-kit migrate` will run:

1. Create a baseline entry and journal:
   ```bash
   npx drizzle-kit generate --custom --name baseline
   ```
   This creates `src/db/migrations/0000_baseline.sql` and `src/db/migrations/meta/_journal.json`.
2. Keep `0000_baseline.sql` empty if the schema already exists.
3. Apply migrations so Drizzle can create its log table:
   ```bash
   npm run db:migrate:drizzle
   ```

## First-time setup on a new/empty database
1. Create a baseline migration:
   ```bash
   npx drizzle-kit generate --custom --name init
   ```
2. Paste the initial schema SQL into the generated `0000_init.sql`.
3. Apply it:
   ```bash
   npm run db:migrate:drizzle
   ```

## Adding new schema changes
1. Edit `src/db/schema.ts`.
2. Generate a migration:
   ```bash
   npx drizzle-kit generate --name add-feature-x
   ```
3. Apply it:
   ```bash
   npm run db:migrate:drizzle
   ```

## Troubleshooting
- Error: `Can't find meta/_journal.json file`
  - Run `npx drizzle-kit generate --custom --name baseline` once to create the journal.
- Error: `Either connection "url" or "host", "database" are required`
  - Ensure `drizzle.config.ts` uses `dbCredentials.url` and `.env` has `DATABASE_URL_UNPOOLED`.
- Error: tables already exist
  - Use an empty baseline migration for already-initialized databases.

## References
- https://orm.drizzle.team/docs/kit-overview
- https://orm.drizzle.team/docs/drizzle-kit-generate
- https://orm.drizzle.team/docs/drizzle-kit-migrate
- https://orm.drizzle.team/docs/drizzle-config-file
- https://orm.drizzle.team/docs/migrations
