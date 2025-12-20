# Integrations & Extensibility
Middleware, webhooks, and integrations with external platforms and services.
Items: 22.

- [Cloudflare Workers environment variables and context](docs/019-cloudflare-workers-environment-variables-and-context.md) - Integration: Cloudflare Workers does not set environment variables a global object like Node.js does with `process.env`.
- [Consuming webhook events](docs/113-consuming-webhook-events.md) - Integration: At its core, Inngest is centered around functions that are triggered by events.
- [Creating middleware](docs/041-creating-middleware.md) - Integration: Creating middleware means defining the lifecycles and subsequent hooks in those lifecycles to run code in.
- [Datadog integration](docs/103-datadog-integration.md) - Integration: Inngest supports exporting metrics to Datadog.
- [Encryption Middleware](docs/043-encryption-middleware.md) - Integration: Encryption middleware provides end-to-end encryption for events, step output, and function output.
- [Example middleware <VersionBadge version="v2.0.0+" />](docs/131-example-middleware.md) - Integration: The following examples show how you might use middleware in some real-world scenarios.
- [Handling Clerk webhook events](docs/058-handling-clerk-webhook-events.md) - Integration: Set up Clerk webhooks with Inngest and use Clerk events within Inngest functions.
- [Instrumenting GraphQL](docs/068-instrumenting-graphql.md) - Integration: When building with GraphQL, you can give your event-driven application a kick-start by instrumenting every query and mutation, sending events when one is successfully executed.
- [Integrate email events with Resend webhooks](docs/077-integrate-email-events-with-resend-webhooks.md) - Integration: Set up Resend webhooks with Inngest and use Resend events within Inngest functions.
- [Middleware](docs/045-middleware.md) - Integration: Middleware allows your code to run at various points in an Inngest client's lifecycle, such as during a function's execution or when sending an event.
- [Middleware <VersionBadge version="v0.3.0+" />](docs/141-middleware.md) - Integration: Middleware allows you to run code at various points in an Inngest function's lifecycle.
- [Middleware lifecycle <VersionBadge version="v2.0.0+" />](docs/132-middleware-lifecycle.md) - Integration: The `init()` function can return functions for two separate lifecycles to hook into.
- [Model Context Protocol (MCP) Integration](docs/001-model-context-protocol-mcp-integration.md) - Integration: Integrate AI development tools with Inngest using Model Context Protocol (MCP).
- [Neon](docs/026-neon.md) - Integration: Inngest allows you to trigger functions from your Neon Postgres database updates.
- [Prometheus metrics export integration](docs/108-prometheus-metrics-export-integration.md) - Integration: Inngest supports exporting [Prometheus](https://prometheus.io/) metrics via scrape endpoints.
- [Python middleware lifecycle](docs/140-python-middleware-lifecycle.md) - Integration: The order of middleware lifecycle hooks is as follows.
- [Sentry Middleware](docs/044-sentry-middleware.md) - Integration: Using the Sentry middleware is useful to.
- [Set up OpenTelemetry with Inngest <VersionBadge version="TypeScript only" />](docs/020-set-up-opentelemetry-with-inngest.md) - Integration: Enrich your Inngest Traces with your application's OpenTelemetry traces.
- [Track all function failures in Datadog](docs/023-track-all-function-failures-in-datadog.md) - Integration: Create a function that handles all function failures in an Inngest environment and forwards them to Datadog.
- [Trigger your code from Retool](docs/083-trigger-your-code-from-retool.md) - Integration: Internal tools are a pain to build and maintain.
- [Using Middleware for Dependency Injection](docs/042-using-middleware-for-dependency-injection.md) - Integration: Inngest Functions running in the same application often need to share common clients instances such as database clients or third-party.
- [Webhook intents: Building a webhook integration](docs/112-webhook-intents-building-a-webhook-integration.md) - Integration: Build webhook integrations with any application using webhook intents.
