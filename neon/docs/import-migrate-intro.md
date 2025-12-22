# Neon data migration guides

> The Neon data migration guides offer step-by-step instructions for migrating data to Neon, detailing processes for various data sources and ensuring seamless integration into the Neon database environment.

## Source

- [Neon data migration guides HTML](https://neon.com/docs/import/migrate-intro): The original HTML version of this documentation

Find instructions for migrating data from Postgres, CSV, other Neon projects, and other database providers. For near-zero downtime data migrations from other Postgres providers, consider using logical replication. Additionally, if you're new to Neon and want to try it out, our sample data guide provides datasets for exploration and testing.

## Data migration guides

- [Import Data Assistant](import-import-data-assistant.md): Move your existing database to Neon using our guided migration tool
- [Migrate with pg_dump and pg_restore](import-migrate-from-postgres.md): Migrate data from another Postgres database using pg_dump and pg_restore
- [Migrate from another Neon project](import-migrate-from-neon.md): Migrate data from another Neon project for Postgres version, region, or account migration
- [Migrate schema only](import-migrate-schema-only.md): Migrate only the schema from a Postgres database with pg_dump and pg_restore
- [Import data from CSV](import-import-from-csv.md): Import data from a CSV file using the psql command-line utility
- [Migrate from Firebase Firestore](import-migrate-from-firebase.md): Migrate data from Firebase Firestore to Neon Postgres using a custom Python script
- [Migrate from Heroku](import-migrate-from-heroku.md): Migrate data from a Heroku Postgres database to Neon Postgres using the Heroku CLI
- [Migrate with AWS DMS](import-migrate-aws-dms.md): Migrate data from another database source to Neon using the AWS Data Migration Service
- [Migrate from Azure](import-migrate-from-azure-postgres.md): Migrate from an Azure Database for PostgreSQL to Neon Postgres
- [Migrate from Digital Ocean](import-migrate-from-digital-ocean.md): Migrate data from Digital Ocean Postgres to Neon Postgres with pg_dump and pg_restore
- [Import sample data](import-import-sample-data.md): Import one of several sample datasets for exploration and testing
- [Migrate from MySQL](import-migrate-mysql.md): Migrate your MySQL data to Neon Postgres using pgloader.
- [Migrate from Render](import-migrate-from-render.md): Migrate data from Render to Neon Postgres with pg_dump and pg_restore
- [Migrate from Supabase](import-migrate-from-supabase.md): MIgrate data from Supabase to Neon Postgres with pg_dump and pg_restore
- [Migrate with pgcopydb](import-pgcopydb.md): Migrate data from another Postgres database using pgcopydb for parallel processing

## Use logical replication for near-zero downtime data migrations

Postgres logical replication in Neon provides an efficient way to migrate data from other Postgres providers with minimal downtime. By replicating data in real-time, this method allows you to transition your applications to Neon without interrupting your services. Please refer to our logical replication guides for instructions.

- [AlloyDB](guides-logical-replication-alloydb.md): Replicate data from AlloyDB to Neon
- [Cloud SQL](guides-logical-replication-cloud-sql.md): Replicate data from Cloud SQL to Neon
- [PostgreSQL to Neon](guides-logical-replication-postgres-to-neon.md): Replicate data from PostgreSQL to Neon
- [AWS RDS](guides-logical-replication-rds-to-neon.md): Replicate data from AWS RDS PostgreSQL to Neon
- [Supabase](guides-logical-replication-supabase-to-neon.md): Replicate data from Supabase to Neon
- [Azure PostgreSQL](import-migrate-from-azure-postgres.md): Replicate data from Azure PostgreSQL to Neon
