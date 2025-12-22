# Neon feature guides

> The Neon feature guides document details the functionalities and usage of Neon's platform features, assisting users in effectively managing and optimizing their database operations within the Neon environment.

## Source

- [Neon feature guides HTML](https://neon.com/docs/guides/neon-features): The original HTML version of this documentation

## Autoscaling

Automatically scale compute resources up and down based on demand.

- [Learn about autoscaling](introduction-autoscaling.md): Find out how autoscaling can reduce your costs.
- [Enable autoscaling](guides-autoscaling-guide.md): Enable autoscaling to automatically scale compute resources on demand

## Scale to zero

Enable or disable scale to zero for your Neon computes.

- [Learn about scale to zero](introduction-scale-to-zero.md): Discover how Neon can reduce your compute to zero when not in use
- [Configure scale to zero](guides-scale-to-zero-guide.md): Enable or disable scale to zero to control if your compute suspends due to inactivity

## Branching

Branch data the same way you branch your code.

- [Learn about branching](introduction-branching.md): With Neon, you can instantly branch your data in the same way that you branch your code
- [Instant restore](https://neon.com/docs/guides/branching-pitr): Restore your data to a past state with database branching
- [Test queries on a branch](guides-branching-test-queries.md): Use branching to test queries before running them in production
- [Branching with the CLI](guides-branching-neon-cli.md): Create and manage branches with the Neon CLI
- [Branching with the API](guides-branching-neon-api.md): Create and manage branches with the Neon API
- [Branching with GitHub Actions](guides-branching-github-actions.md): Automate branching with GitHub Actions
- [Refresh a branch](https://neon.com/docs/guides/branch-refresh): Refresh a development branch with the Neon API

## Logical replication

Replicate data from Neon to external data platforms and services.

- [Logical replication guide](guides-logical-replication-guide.md): Get started with logical replication in Neon
- [Logical replication concepts](guides-logical-replication-concepts.md): Learn about Postgres logical replication concepts
- [Logical replication commands](guides-logical-replication-manage.md): Commands for managing your logical replication configuration
- [Logical replication in Neon](guides-logical-replication-neon.md): Information about logical replication specific to Neon

## Read replicas

Learn how Neon read replicas can help you scale and manage read-only workloads.

- [Learn about read replicas](introduction-read-replicas.md): Learn how Neon maximizes scalability and more with read replicas
- [Create and manage Read Replicas](guides-read-replica-guide.md): Learn how to create, connect to, configure, delete, and monitor read replicas
- [Scale your app with Read Replicas](guides-read-replica-integrations.md): Scale your app with read replicas using built-in framework support
- [Run analytics queries with Read Replicas](guides-read-replica-data-analysis.md): Leverage read replicas for running data-intensive analytics queries
- [Run ad-hoc queries with Read Replicas](guides-read-replica-adhoc-queries.md): Leverage read replicas for running ad-hoc queries
- [Provide read-only access with Read Replicas](guides-read-only-access-read-replicas.md): Leverage read replicas to provide read-only access to your data

## Time Travel

Travel back in time to view your database's history.

- [Learn about Time Travel](guides-time-travel-assist.md): Learn how to query point-in-time connections against your data's history
- [Time Travel tutorial](guides-time-travel-tutorial.md): Use Time Travel to analyze changes made to your database over time

## Schema Diff

Compare your database branches.

- [Learn about Schema Diff](guides-schema-diff.md): Learn how to use Neon's Schema Diff tool to compare branches of your database
- [Schema Diff tutorial](guides-schema-diff-tutorial.md): Step-by-step guide showing you how to compare two development branches using Schema Diff

## Project collaboration

Invite other users to collaborate on your Neon project.

- [Collaborate on your Neon project](guides-project-collaboration-guide.md): Give other users access to your project from the Neon Console, API, and CLI

## IP Allow

Limit access to trusted IP addresses.

- [Define your IP allowlist](introduction-ip-allow.md): Learn how to limit database access to trusted IP addresses

## Protected branches

Protect your production or sensitive data.

- [Configure protected branches](guides-protected-branches.md): Learn how to use Neon's protected branches feature to secure access to critical data

## Private Networking

Secure your database connections with private access.

- [Private Networking](guides-neon-private-networking.md): Learn how to connect your application to a Neon database via AWS PrivateLink, bypassing the open internet
