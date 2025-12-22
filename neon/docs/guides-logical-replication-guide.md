# Get started with logical replication

> The document outlines the steps for setting up logical replication in Neon, detailing how to configure a publisher and subscriber to replicate data changes between databases.

## Source

- [Get started with logical replication HTML](https://neon.com/docs/guides/logical-replication-guide): The original HTML version of this documentation

Neon's logical replication feature, available to all Neon users, allows you to replicate data to and from your Neon Postgres database:

- Stream data from your Neon database to external destinations, enabling Change Data Capture (CDC) and real-time analytics. External sources might include data warehouses, analytical database services, real-time stream processing systems, messaging and event-streaming platforms, and external Postgres databases, among others. See [Replicate data from Neon](guides-logical-replication-guide.md#replicate-data-from-neon).
- Perform live migrations to Neon from external sources such as AWS RDS and Google Cloud SQL &#8212; or any platform that runs Postgres. See [Replicate data to Neon](guides-logical-replication-guide.md#replicate-data-to-neon).
- Replicate data from one Neon project to another for Neon project, account, Postgres version, or region migration. See [Replicate data from one Neon project to another](guides-logical-replication-neon-to-neon.md).



Logical replication in Neon works like it does on any standard Postgres installation. It uses a publisher-subscriber model to replicate data from the source database to the destination database. Neon can act as a publisher or subscriber.

Replication starts by copying a snapshot of the data from the publisher to the subscriber. Once this is done, subsequent changes are sent to the subscriber as they occur in real-time.

To learn more about Postgres logical replication, see the following topics.

## Learn about logical replication

- [Logical replication concepts](guides-logical-replication-concepts.md): Learn about Postgres logical replication concepts
- [Logical replication commands](guides-logical-replication-manage.md): Commands for managing your logical replication configuration
- [Logical replication in Neon](guides-logical-replication-neon.md): Information about logical replication specific to Neon
- [Managing schema changes](guides-logical-replication-schema-changes.md): Learn about managing schema changes in a logical replication setup

To get started, jump into one of our step-by-step logical replication guides.

## Replicate data from Neon

- [Airbyte](guides-logical-replication-airbyte.md): Replicate data from Neon with Airbyte
- [Bemi](guides-bemi.md): Create an automatic audit trail with Bemi
- [ClickHouse](https://docs.peerdb.io/mirror/cdc-neon-clickhouse): Change Data Capture from Neon to ClickHouse with PeerDB (PeerDB docs)
- [Confluent (Kafka)](guides-logical-replication-kafka-confluent.md): Replicate data from Neon with Confluent (Kafka)
- [Decodable](guides-logical-replication-decodable.md): Replicate data from Neon with Decodable
- [Estuary Flow](guides-logical-replication-estuary-flow.md): Replicate data from Neon with Estuary Flow
- [Fivetran](guides-logical-replication-fivetran.md): Replicate data from Neon with Fivetran
- [Materialize](guides-logical-replication-materialize.md): Replicate data from Neon to Materialize
- [Neon to Neon](guides-logical-replication-neon-to-neon.md): Replicate data from Neon to Neon
- [Neon to PostgreSQL](guides-logical-replication-postgres.md): Replicate data from Neon to PostgreSQL
- [Prisma Pulse](guides-logical-replication-prisma-pulse.md): Stream database changes in real-time with Prisma Pulse
- [Sequin](guides-sequin.md): Stream data from platforms like Stripe, Linear, and GitHub to Neon
- [Snowflake](guides-logical-replication-airbyte-snowflake.md): Replicate data from Neon to Snowflake with Airbyte
- [Inngest](guides-logical-replication-inngest.md): Replicate data from Neon to Inngest

## Replicate data to Neon

- [AlloyDB](guides-logical-replication-alloydb.md): Replicate data from AlloyDB to Neon
- [Azure PostgreSQL](import-migrate-from-azure-postgres.md): Replicate data from Azure PostgreSQL to Neon
- [Cloud SQL](guides-logical-replication-cloud-sql.md): Replicate data from Cloud SQL to Neon
- [Neon to Neon](guides-logical-replication-neon-to-neon.md): Replicate data from Neon to Neon
- [PostgreSQL to Neon](guides-logical-replication-postgres-to-neon.md): Replicate data from PostgreSQL to Neon
- [RDS](guides-logical-replication-rds-to-neon.md): Replicate data from AWS RDS PostgreSQL to Neon
- [Supabase](guides-logical-replication-supabase-to-neon.md): Replicate data from Supabase to Neon
