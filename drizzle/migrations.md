# Drizzle migrations (drizzle-kit)

## Sources
- https://orm.drizzle.team/docs/kit-overview
- https://orm.drizzle.team/docs/drizzle-kit-generate
- https://orm.drizzle.team/docs/drizzle-kit-migrate
- https://orm.drizzle.team/docs/drizzle-config-file
- https://orm.drizzle.team/docs/kit-custom-migrations
- https://orm.drizzle.team/docs/migrations
- https://orm.drizzle.team/docs/drizzle-kit-push

## How drizzle-kit migrate works (summary)
- Reads the migrations folder and SQL files.
- Reads applied migrations from the database log table.
- Applies unapplied migrations and records them in `__drizzle_migrations` (configurable).

## Recommended flow (code-first SQL migrations)
1. Configure `drizzle.config.ts` with `dialect`, `schema`, `out`, and `dbCredentials.url`.
2. Generate SQL migrations from the schema:
   ```bash
   npx drizzle-kit generate --name init
   ```
   This creates `<out>/0001_init.sql` (numbered) and `<out>/meta/_journal.json`.
3. Apply migrations:
   ```bash
   npx drizzle-kit migrate
   ```

## Custom SQL migrations
If you need custom SQL (or data seeding), generate an empty migration and edit it:
```bash
npx drizzle-kit generate --custom --name seed-users
```
Then edit `<out>/000x_seed-users.sql`, and run:
```bash
npx drizzle-kit migrate
```

## Direct schema push (no SQL files)
For rapid prototyping, you can push schema changes directly:
```bash
npx drizzle-kit push
```

## Repo-specific notes
- `drizzle.config.ts` uses:
  - `schema: ./src/db/schema.ts`
  - `out: ./src/db/migrations`
  - `dbCredentials.url` from `DATABASE_URL_UNPOOLED` (fallback `DATABASE_URL`)
- Ensure `.env` has a valid DB URL before running migrations.
- To run migrations via npm:
  ```bash
  npm run db:migrate:drizzle
  ```

## Important gotcha for manual SQL files
`drizzle-kit migrate` requires a `meta/_journal.json` that lists numbered migration files.
If you already have a standalone SQL file (for example `src/db/migrations/0001_initial.sql`),
generate a custom migration with `drizzle-kit generate --custom` and move the SQL into the
generated `000x_name.sql` so it is tracked in the journal.
