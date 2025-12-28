# Drizz**l**e ORM Cookbook (Schema + Migrations)

> **Purpose:** This is the “do it the same way every time” workflow for using **Drizzle ORM** as the source of truth for your database schema, with **drizzle-kit** managing migrations.  
> Use this as the execution playbook for a coding agent.

---

## 0) The mental model (how to think about Drizzle)

Drizzle is two things that work together:

1) **Schema in TypeScript = Source of Truth**  
   Your `schema.ts` files are the canonical definition of tables, columns, constraints, relations, indexes, etc. Drizzle’s own docs explicitly frame the TS schema as the source of truth for queries **and** migrations. citeturn1search19

2) **Migrations are a durable history (SQL files + snapshots)**  
   `drizzle-kit generate` diffs “current schema snapshot” vs “last migration snapshot” and writes a new migration folder containing `migration.sql` + `snapshot.json`. citeturn0search1  
   `drizzle-kit migrate` applies new `.sql` migrations and records them in the DB migrations log table. citeturn0search2

**Rule of thumb:**  
- **Design and edit schema in TypeScript.**  
- **Review + commit generated migrations.**  
- **Apply migrations in a controlled order per environment.**  
- **Never hand-edit the DB in prod without also reflecting the change in schema+migrations.**

---

## 1) Standard project layout (recommended)

```
/src
  /db
    schema.ts          # Drizzle schema definitions (tables, enums, etc.)
    index.ts           # DB connection + exported `db`
    migrate.ts         # Optional: runtime migration runner (CI/prod)
/drizzle               # Generated migrations + meta snapshots (committed)
/drizzle.config.ts     # drizzle-kit configuration (committed)
/.env                  # contains DATABASE_URL locally (not committed)
```

> If you split schema across multiple files, ensure drizzle-kit can import everything (see “Foot-guns”). citeturn1search19

---

## 2) Dependencies and setup

### 2.1 Install packages
Install:
- `drizzle-orm`
- `drizzle-kit`
- **one** DB driver package for your dialect (examples: `pg` or `postgres` for Postgres; mysql/sqlite equivalents)

(Driver choice is per Drizzle’s “Get started” guides for your DB.) citeturn1search15turn1search4

### 2.2 Environment variables
Create `.env` at project root:

```
DATABASE_URL=postgresql://user:pass@host:5432/db
```

Drizzle’s Postgres “get started” uses `DATABASE_URL` as the typical pattern. citeturn1search15

---

## 3) drizzle-kit configuration (required)

Create `drizzle.config.ts`:

```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",      // or mysql / sqlite / etc.
  schema: "./src/db/schema.ts",
  out: "./drizzle",           // migrations folder
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
});
```

`drizzle-kit migrate` (and other commands) can read dialect + credentials from this config. citeturn0search2turn0search21

### 3.1 Multiple environments (dev/staging/prod)
Use multiple configs if you have distinct DB URLs or different migration folders:

```bash
npx drizzle-kit migrate --config=drizzle-dev.config.ts
npx drizzle-kit migrate --config=drizzle-prod.config.ts
```

Multiple config files are explicitly supported and documented. citeturn0search21

---

## 4) Canonical workflow (code-first, team-safe)

This is the recommended “normal” workflow for a shared codebase:

### 4.1 Make a schema change (TypeScript)
1) Edit `src/db/schema.ts` (or schema module files).
2) **Make sure all models are exported** from the schema entrypoint (see foot-guns). citeturn1search19

### 4.2 Generate a migration
Run:

```bash
npx drizzle-kit generate
```

What happens: drizzle-kit reads schema, compares to latest snapshot, may prompt for renames, then writes `migration.sql` and `snapshot.json` under a new timestamped folder. citeturn0search1

### 4.3 Review the migration SQL (mandatory)
Before applying it anywhere:
- Read `drizzle/<timestamp>_*/migration.sql`
- Confirm it matches intent (no accidental drops, wrong defaults, missing indexes, etc.)
- If it includes destructive operations (drop/alter), confirm you intended them and that you have a rollout plan.

### 4.4 Apply migrations to your dev DB
Run:

```bash
npx drizzle-kit migrate
```

`migrate` reads migration SQL files, checks the DB’s migration log table, runs any missing ones, and records them. citeturn0search2

### 4.5 Validate the migration history integrity (team workflow)
Run:

```bash
npx drizzle-kit check
```

This checks consistency of generated migration history and is designed to help when multiple developers generate migrations in parallel. citeturn0search21

### 4.6 Commit
Commit together:
- Schema changes (`src/db/schema.ts`)
- New migration folder(s) under `/drizzle`
- Any supporting code changes

**Never** commit schema changes without the matching migration, unless explicitly doing a “brownfield baseline” workflow.

---

## 5) “Fast local iteration” workflow (push) — use carefully

`drizzle-kit push` applies schema changes directly to the database without generating migration files. It diffs schema vs DB, generates SQL internally, and applies it. citeturn0search6turn0search7

**Allowed use:** local/dev-only experimentation where you don’t care about preserving a reviewable migration history.

**Foot-gun warning:** If you `push` first and then `generate`, you may end up with migrations that fail locally because the DB already has the changes. This is a common workflow trap discussed by the community. citeturn1search14

**Safe pattern if you must use push:**
- Use `push` only on throwaway DBs, or
- Reset DB and replay migrations after you generate, or
- Prefer `generate` + `migrate` even for local work once you’ve settled the schema shape.

---

## 6) Brownfield workflow (existing DB, adopt Drizzle safely)

When you already have an existing database schema (and likely multiple environments):

### 6.1 Pull / introspect the existing DB into Drizzle schema
Use `drizzle-kit pull` to pull (introspect) schema from the database and generate a Drizzle schema file. citeturn0search28turn1search2

Common pattern for existing projects is:

```bash
npx drizzle-kit pull --init
```

`pull --init` is documented as creating the migrations table and marking the first pulled migration as applied, so you can continue from there. citeturn1search9

> Use your **development** DB as the reference to pull from (it should match prod schema as of now).

### 6.2 Align environments that already contain the schema (no “init” re-create)
If your staging/prod DB already contains the same tables, you must avoid trying to “init” create them again.

Drizzle team guidance (for the “existing DB across envs” situation) includes using:

```bash
npx drizzle-kit migrate --no-init
```

This skips the init step for databases that already have the schema. citeturn0search10turn1search5

### 6.3 After baseline, proceed code-first
Once baseline is established:
- Make changes in TS schema
- `generate`
- review
- `migrate`
- `check`

---

## 7) When drizzle-kit can’t express a change: custom migrations

For complex DDL or for data migrations/seeding that you want in the same pipeline, you can generate an empty migration and write SQL yourself:

```bash
npx drizzle-kit generate --custom --name=seed-users
```

This creates a migration file for you to fill in. citeturn0search11

**Use this for:**
- Backfills / data reshaping
- Multi-step changes where you need staged deployment
- DDL features not supported by the diff engine

---

## 8) Production / CI migration execution (recommended approach)

You have two reliable options:

### Option A — Use drizzle-kit migrate in CI/deploy step
Run, per environment config:

```bash
npx drizzle-kit migrate --config=drizzle-prod.config.ts
```

This is the straightforward “apply migrations” path. citeturn0search2turn0search21

### Option B — Use Drizzle ORM `migrate()` at runtime (app/script)
Drizzle docs note you can apply generated migrations using `drizzle-kit migrate` **or** Drizzle ORM’s `migrate()` function. citeturn1search6

**Why choose runtime migrations:** Some deployments prefer using the ORM migrator with the same driver/runtime constraints as the app.

**Example (Node + Postgres driver)**  
(Adjust imports for your chosen driver; this shows the typical “db + migrate” shape.)

```ts
// src/db/migrate.ts
import "dotenv/config";
import { drizzle } from "drizzle-orm/node-postgres";
import { migrate } from "drizzle-orm/node-postgres/migrator";
import { Pool } from "pg";

const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const db = drizzle(pool);

await migrate(db, { migrationsFolder: "drizzle" });
await pool.end();
```

---

## 9) Verification checklist (definition of “done”)

A schema change is complete only when all of the following are true:

1) **Schema compiles** (TypeScript)
2) **Migration generated** and reviewed (`drizzle-kit generate`) citeturn0search1
3) **Migrations apply cleanly** to a fresh DB (ideal) and to your dev DB (`drizzle-kit migrate`) citeturn0search2
4) **Migration history is consistent** (`drizzle-kit check`) citeturn0search21
5) **App-level checks pass** (unit/integration tests, lint, typecheck)
6) **No drift**: schema + migration intent match; no manual DB edits left untracked

**Optional but strong:**  
- Spin up a blank DB, run migrations from zero, run tests. This catches “works on my DB” drift.

---

## 10) Foot-guns to avoid (high-signal)

### 10.1 Forgetting to export schema models
If using drizzle-kit, you must export all models so the CLI can import and diff them. citeturn1search19

### 10.2 Editing old migrations after they ran anywhere
Once a migration is applied to any shared environment, treat it as immutable.  
Make a new migration to fix issues.

### 10.3 Using `push` and then trying to `generate` + `migrate` on the same DB
This can produce migrations that fail because changes were already applied. citeturn1search14  
Prefer `generate` + `migrate` once changes are real.

### 10.4 Brownfield baseline mistakes
If the DB already contains the schema, do **not** re-run init migrations that create tables; use the baseline pattern (`pull --init` on the baseline DB, `migrate --no-init` on envs that already have the schema). citeturn1search9turn0search10turn1search5

### 10.5 Permissions / migrations table location
Drizzle stores migration execution info in `__drizzle_migrations` by default (and for Postgres, commonly in the `drizzle` schema unless configured). citeturn0search9turn1search16  
In locked-down DBs, ensure the migration table/schema is writable, or configure accordingly (and verify in the target environment).

### 10.6 MySQL / SQLite transactional quirks (breakpoints)
Drizzle kit uses `--> statement-breakpoint` to handle DBs that can’t run multiple DDL statements in one transaction; config has a `breakpoints` option. citeturn0search3  
Don’t disable it unless you understand your dialect’s DDL behavior.

---

## 11) Task planning template (what the coding agent should do)

When asked to “change the DB schema”, follow this exact plan:

1) **Identify dialect + environment:** Postgres/MySQL/SQLite? dev/staging/prod?  
2) **Confirm baseline state:**  
   - Greenfield: migrations start empty.  
   - Brownfield: establish baseline with `pull --init`, and confirm whether `--no-init` is needed. citeturn1search9turn1search5
3) **Edit schema in TS:** minimal, intentional change set.
4) **Generate migration:** `npx drizzle-kit generate` citeturn0search1
5) **Review SQL:** validate safety + correctness.
6) **Apply locally:** `npx drizzle-kit migrate` citeturn0search2
7) **Run `check`:** `npx drizzle-kit check` citeturn0search21
8) **Run test suite / verification:** ensure app behavior matches.
9) **Commit & PR:** include schema + migrations as an atomic change.
10) **Deploy:** apply migrations in CI or via runtime migrator, then verify.

---

## Appendix: Suggested package.json scripts

```json
{
  "scripts": {
    "db:generate": "drizzle-kit generate",
    "db:migrate": "drizzle-kit migrate",
    "db:check": "drizzle-kit check",
    "db:push": "drizzle-kit push"
  }
}
```

> If you use multiple configs, add `--config=...` to these scripts. citeturn0search21
