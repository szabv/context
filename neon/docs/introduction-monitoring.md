# Monitoring in Neon

> The "Monitoring in Neon" documentation outlines the tools and procedures for tracking database performance and health, enabling users to efficiently manage and troubleshoot their Neon database environments.

## Source

- [Monitoring in Neon HTML](https://neon.com/docs/introduction/monitoring): The original HTML version of this documentation

To find out what's going on with your Neon projects and databases, Neon offers several ways to track metrics and monitor usage.

- [Monitoring dashboard](introduction-monitoring-page.md): View system and database metrics on the Neon Monitoring dashboard
- [Monitor billing and usage](introduction-monitor-usage.md): Monitor billing and usage metrics for your Neon account and projects
- [Autoscaling](guides-autoscaling-guide.md#monitor-autoscaling): Monitor Autoscaling vCPU and RAM usage
- [Neon system operations](manage-operations.md): Monitor Neon project operations from the Neon Console, API, or CLI
- [Active Queries](introduction-monitor-active-queries.md): View and analyze running queries in your database
- [Query performance](introduction-monitor-query-performance.md): View and analyze query performance for your Neon database
- [pg_stat_statements](extensions-pg_stat_statements.md): Monitor query performance and statistics in Postgres with pg_stat_statements

## Datadog integration

- [Datadog](guides-datadog.md): Export Neon Metrics to Datadog with the Neon Datadog Integration

## OpenTelemetry

- [OTel integration](guides-opentelemetry.md): Export Neon metrics to any OpenTelemetry-compatible observability platform
- [Grafana Cloud](guides-grafana-cloud.md): Export Neon metrics and logs to Grafana Cloud with native OTLP integration
- [Better Stack](https://neon.com/guides/betterstack-otel-neon): Monitor Neon with Better Stack using OpenTelemetry integration
- [New Relic](https://neon.com/guides/newrelic-otel-neon): Monitor Neon with New Relic using OpenTelemetry integration
- [Metrics and logs reference](reference-metrics-logs.md): Metrics and logs reference for monitoring

## Other monitoring tools

- [pgAdmin](introduction-monitor-pgadmin.md): Monitor your Neon Postgres database with pgAdmin
- [PgHero](introduction-monitor-pghero.md): Monitor your Neon Postgres database with PgHero

## Feedback and future improvements

At Neon, we understand that observability and monitoring are critical for running successful applications.

If you've got feature requests or feedback about what you'd like to see in Neon monitoring and observability features, let us know via the [Feedback](https://console.neon.tech/app/projects?modal=feedback) form in the Neon Console or our [feedback channel](https://discord.com/channels/1176467419317940276/1176788564890112042) on Discord.
