# Observability & Operations
Monitoring, metrics, traces, performance, and operational controls.
Items: 14.

- [Datadog integration](docs/103-datadog-integration.md) - Ops/observability: Inngest supports exporting metrics to Datadog.
- [Function Replay](docs/110-function-replay.md) - Ops/observability: Functions will fail.
- [Function runs Bulk Cancellation](docs/102-function-runs-bulk-cancellation.md) - Ops/observability: In addition to providing [SDK Cancellation features](/docs/features/inngest-functions/cancellation/cancel-on-events) and a [dedicated REST API endpoint](/docs/guides/cancel-running-functions), the Inngest Platform also features a Bulk Cancellation UI.
- [Improve Performance](docs/087-improve-performance.md) - Ops/observability: Solutions to reduce latency.
- [Insights](docs/104-insights.md) - Ops/observability: Query and analyze event data with SQL in the Inngest platform.
- [Inspecting a Function run](docs/106-inspecting-a-function-run.md) - Ops/observability: You identified a failed Function run and want to identify the root cause?
- [Inspecting an Event](docs/105-inspecting-an-event.md) - Ops/observability: The Event details will provide all the information to understand how this event was received, which data it contained and the tools to reproduce it locally.
- [Logging in Inngest](docs/070-logging-in-inngest.md) - Ops/observability: Log handling can have some caveats when working with serverless runtimes.
- [Observability & Metrics](docs/107-observability-and-metrics.md) - Ops/observability: With hundreds to thousands of events going through your Inngest Apps, triggering multiple Function runs, getting a clear view of what is happening at any time is crucial.
- [Platform Guides](docs/100-platform-guides.md) - Ops/observability: Learn how to use the Inngest platform.
- [Prometheus metrics export integration](docs/108-prometheus-metrics-export-integration.md) - Ops/observability: Inngest supports exporting [Prometheus](https://prometheus.io/) metrics via scrape endpoints.
- [Providers' Usage Limits](docs/179-providers-usage-limits.md) - Ops/observability: As your functions' code runs on the hosting provider of your choice, you will be subject to provider or billing plan.
- [Traces](docs/109-traces.md) - Ops/observability: Inngest provides multiple levels of tracing to monitor your functions, from built-in execution traces to AI-specific instrumentation and comprehensive OpenTelemetry-powered distributed tracing.
- [Usage Limits](docs/178-usage-limits.md) - Ops/observability: We have put some limits on the service to make sure we provide you a good default to start with, while also keeping it a good experience for all other users using Inngest.
