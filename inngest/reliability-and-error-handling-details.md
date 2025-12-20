# Reliability & Error Handling
Retries, failures, cancellations, and recovery patterns for durable execution.
Items: 16.

- [`inngest/function.cancelled` {{ className: "not-prose" }}](docs/157-inngest-function-cancelled-classname-not-prose.md) - Reliability: The `inngest/function.cancelled` event is sent whenever any single function is cancelled in your [Inngest environment](/docs/platform/environments).
- [`inngest/function.failed` {{ className: "not-prose" }}](docs/158-inngest-function-failed-classname-not-prose.md) - Reliability: The `inngest/function.failed` event is sent whenever any single function fails in your [Inngest environment](/docs/platform/environments).
- [Bulk Cancellation](docs/057-bulk-cancellation.md) - Reliability: Learn how to cancel long running functions with our API.
- [Cancel on](docs/161-cancel-on.md) - Reliability: Stop the execution of a running function when a specific event is received using `cancelOn`.
- [Cancel on Events](docs/028-cancel-on-events.md) - Reliability: Learn how to cancel long running functions with events.
- [Cancel on timeouts](docs/029-cancel-on-timeouts.md) - Reliability: Learn how to cancel long running functions with events.
- [Cancellation](docs/030-cancellation.md) - Reliability: Cancellation is a useful mechanism for preventing unnecessary actions based on previous actions (ex, skipping a report generation upon an account deletion) or stopping an unwanted function run composed of multiple steps (ex, deployment mistake, duplicates).
- [Cleanup after function cancellation](docs/014-cleanup-after-function-cancellation.md) - Reliability: Create a function that executes after a function run has been cancelled via event, REST API, or bulk cancellation.
- [Errors & Retries](docs/063-errors-and-retries.md) - Reliability: Learn how to handle errors and failures in your Inngest functions.
- [Failure handlers <VersionBadge version="TypeScript only" />](docs/031-failure-handlers.md) - Reliability: If your function exhausts all of its retries, it will be marked as "Failed." You can handle this circumstance by either providing an [`onFailure/on_failure`](/docs/reference/functions/handling-failures) handler when defining your function, or by listening for the [`inngest/function.failed`](/docs/reference/system-events/inngest-function-failed) system event.
- [Function runs Bulk Cancellation](docs/102-function-runs-bulk-cancellation.md) - Reliability: In addition to providing [SDK Cancellation features](/docs/features/inngest-functions/cancellation/cancel-on-events) and a [dedicated REST API endpoint](/docs/guides/cancel-running-functions), the Inngest Platform also features a Bulk Cancellation UI.
- [Handling Failures](docs/118-handling-failures.md) - Reliability: Define any failure handlers for your function with the [`onFailure`](/docs/reference/functions/create#configuration) option.
- [Inngest Errors](docs/032-inngest-errors.md) - Reliability: Inngest automatically handles errors and retries for you.
- [Retries](docs/033-retries.md) - Reliability: By default, in _addition_ to the **initial attempt**, Inngest will retry a function or a step up to 4 times until it succeeds.
- [Rollbacks](docs/034-rollbacks.md) - Reliability: Unlike an error being thrown in the main function's body, a failing step (one that has exhausted all retries) will throw a `StepError`.
- [Track all function failures in Datadog](docs/023-track-all-function-failures-in-datadog.md) - Reliability: Create a function that handles all function failures in an Inngest environment and forwards them to Datadog.
