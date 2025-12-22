# Get started with branching

> This document introduces Neon users to the branching feature, detailing how to create and manage branches within their database environments to facilitate development workflows.

## Source

- [Get started with branching HTML](https://neon.com/docs/guides/branching-intro): The original HTML version of this documentation

Find detailed information and instructions about Neon's branching feature and how you can integrate branching with your development workflows.

## What is branching?

Learn about branching and how you can apply it in your development workflows.

- [Learn about branching](introduction-branching.md): Learn about Neon's branching feature and how to use it in your development workflows
- [Database branching for Postgres](https://neon.com/blog/database-branching-for-postgres-with-neon): Blog: Read about how Neon's branching feature works and what it means for your workflows
- [Branch archiving](guides-branch-archiving.md): Learn how Neon automatically archives inactive branches to cost-effective storage
- [Schema-only branches](guides-branching-schema-only.md): Learn how you can protect sensitive data with schema-only branches

## Automate branching

Integrate branching into your CI/CD pipelines and workflows with the Neon API, CLI, GitHub Actions, and Githooks.

- [Branching with the Neon API](guides-branching-neon-api.md): Learn how to instantly create and manage branches with the Neon API
- [Branching with the Neon CLI](guides-branching-neon-cli.md): Learn how to instantly create and manage branches with the Neon CLI
- [Branching with GitHub Actions](guides-branching-github-actions.md): Automate branching with Neon's GitHub Actions for branching
- [Branching with Githooks](https://neon.com/blog/automating-neon-branch-creation-with-githooks): Blog: Learn how to automating branch creation with Githooks

## Preview deployments

Create a branch for each preview deployment with the [Neon-managed Vercel integration](guides-neon-managed-vercel-integration.md).

- [The Neon-Managed Vercel Integration](guides-neon-managed-vercel-integration.md): Connect your Vercel project and create a branch for each preview deployment
- [Preview deployments with Vercel](https://neon.com/blog/neon-vercel-integration): Blog: Read about full-stack preview deployments using the Neon Vercel Integration
- [A database for every preview](https://neon.com/blog/branching-with-preview-environments): Blog: A database for every preview environment with GitHub Actions and Vercel

## Test queries

Test potentially destructive or performance-impacting queries before your run them in production.

- [Branching — Testing queries](guides-branching-test-queries.md): Instantly create a branch to test queries before running them in production

## Data recovery and audits

Recover lost data or track down issues by restoring a branch to its history, or just create a point-in-time branch for historical analysis or any other reason.

- [Instant restore with Time Travel Assist](https://neon.com/docs/guides/branch-restore): Learn how to instantly recover your database to any point in time within your restore window
- [Time Travel](guides-time-travel-assist.md): Query point-in-time connections with Time Travel
- [Schema diff](guides-schema-diff.md): Visualize schema differences between branches to help with troubleshooting

## Example applications

Explore example applications that use Neon's branching feature.

- [Time Travel Demo](https://github.com/kelvich/branching_demo_bisect): Use Neon branching, the Neon API, and a bisect script to recover lost data
- [Neon Twitter app](https://github.com/neondatabase/neon_twitter): Use GitHub Actions to create and delete a branch with each pull request
- [Preview branches app](https://github.com/neondatabase/preview-branches-with-vercel): An application demonstrating using GitHub Actions with preview deployments in Vercel
