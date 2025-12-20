# TypeScript SDK & Reference
TypeScript and JavaScript SDKs, step APIs, serve handler, and Workflow Kit reference.
Items: 34.

- [`inngest/function.cancelled` {{ className: "not-prose" }}](docs/157-inngest-function-cancelled-classname-not-prose.md) - TypeScript: The `inngest/function.cancelled` event is sent whenever any single function is cancelled in your [Inngest environment](/docs/platform/environments).
- [`inngest/function.failed` {{ className: "not-prose" }}](docs/158-inngest-function-failed-classname-not-prose.md) - TypeScript: The `inngest/function.failed` event is sent whenever any single function fails in your [Inngest environment](/docs/platform/environments).
- [Cancel on](docs/161-cancel-on.md) - TypeScript: Stop the execution of a running function when a specific event is received using `cancelOn`.
- [Components API (React)](docs/164-components-api-react.md) - TypeScript: The [`@inngest/workflow-kit`](https://npmjs.com/package/@inngest/workflow-kit) package provides a set of React components, enabling you to build a workflow editor UI in no time!
- [Create Function](docs/116-create-function.md) - TypeScript: Define your functions using the `createFunction` method on the [Inngest client](/docs/reference/client/create).
- [Create the Inngest Client](docs/114-create-the-inngest-client.md) - TypeScript: The `Inngest` client object is used to configure your application, enabling you to create functions and send events.
- [Creating workflow actions](docs/163-creating-workflow-actions.md) - TypeScript: The [`@inngest/workflow-kit`](https://npmjs.com/package/@inngest/workflow-kit) package provides a [workflow engine](/docs/reference/workflow-kit/engine), enabling you to create workflow actions on the back end.
- [Debounce functions <VersionBadge version="v3.1.0+" />](docs/117-debounce-functions.md) - TypeScript: Debounce delays a function run for the given `period`, and reschedules functions for the given `period` any time new events are received while the debounce is active.
- [Ensure exclusive execution of a function](docs/121-ensure-exclusive-execution-of-a-function.md) - TypeScript: Ensure that only a single run of a function (_or a set of specific functions, based on specific event properties_) is running at a time.
- [Environment Variables](docs/169-environment-variables.md) - TypeScript: You can set environment variables to change various parts of Inngest's configuration.
- [ESLint Plugin](docs/170-eslint-plugin.md) - TypeScript: An ESLint plugin is available at [@inngest/eslint-plugin](https://www.npmjs.com/package/@inngest/eslint-plugin), providing rules to enforce best practices when writing Inngest functions.
- [Example middleware <VersionBadge version="v2.0.0+" />](docs/131-example-middleware.md) - TypeScript: The following examples show how you might use middleware in some real-world scenarios.
- [Function run priority <VersionBadge version="v3.2.1+" />](docs/120-function-run-priority.md) - TypeScript: You can prioritize specific function runs above other runs **within the same function**.
- [Handling Failures](docs/118-handling-failures.md) - TypeScript: Define any failure handlers for your function with the [`onFailure`](/docs/reference/functions/create#configuration) option.
- [Installing the SDK](docs/172-installing-the-sdk.md) - TypeScript: The Inngest SDK allows you to write reliable, durable functions in your existing projects incrementally.
- [Invoke <VersionBadge version="v3.7.0+" />](docs/122-invoke.md) - TypeScript: Use `step.invoke()` to asynchronously call another function and handle the result.
- [Middleware lifecycle <VersionBadge version="v2.0.0+" />](docs/132-middleware-lifecycle.md) - TypeScript: The `init()` function can return functions for two separate lifecycles to hook into.
- [Rate limit function execution](docs/119-rate-limit-function-execution.md) - TypeScript: Set a _hard limit_ on how many function runs can start within a time period.
- [Reference](docs/130-reference.md) - TypeScript: Learn about our SDKs.
- [Run](docs/123-run.md) - TypeScript: Use `step.run()` to run synchronous or asynchronous code as a retriable step in your function.
- [Send Event](docs/124-send-event.md) - TypeScript: Use to send event(s) reliably within your function.
- [Send events](docs/115-send-events.md) - TypeScript: Send events to Inngest.
- [Serve](docs/156-serve.md) - TypeScript: The `serve()` API handler is used to serve your application's [functions](/docs/reference/functions/create) via HTTP.
- [Sleep `step.sleep()`](docs/126-sleep-step-sleep.md) - TypeScript: The ID of the step.
- [Sleep until `step.sleepUntil()`](docs/125-sleep-until-step-sleepuntil.md) - TypeScript: The ID of the step.
- [Testing](docs/159-testing.md) - TypeScript: To test your Inngest functions programmatically, use the `@inngest/test.
- [TypeScript](docs/177-typescript.md) - TypeScript: `Learn the Inngest SDK's type safe features with TypeScript.
- [TypeScript SDK](docs/162-typescript-sdk.md) - TypeScript: Our TypeScript SDK and its related packages are open source and available on Github: [<GithubIcon className="ml-2 inline-flex"/> inngest/inngest-js](https://github.com/inngest/inngest-js).
- [Upgrading from Inngest SDK v2 to v3](docs/171-upgrading-from-inngest-sdk-v2-to-v3.md) - TypeScript: How to migrate your code to the latest version of the Inngest TS SDK.
- [Usage](docs/160-usage.md) - TypeScript: Inngest supports OpenTelemetry for distributed tracing and observability.
- [Using the workflow engine](docs/165-using-the-workflow-engine.md) - TypeScript: The workflow `Engine` is used to run a given [workflow instance](/docs/reference/workflow-kit/workflow-instance) within an Inngest Function.
- [Wait for event](docs/127-wait-for-event.md) - TypeScript: The ID of the step.
- [Workflow instance](docs/167-workflow-instance.md) - TypeScript: A workflow instance represents a user configuration of a sequence of [workflow actions](/docs/reference/workflow-kit/actions), later provided to the [workflow engine](/docs/reference/workflow-kit/engine) for execution.
- [Workflow Kit](docs/166-workflow-kit.md) - TypeScript: Workflow Kit enables you to build [user-defined workflows](/docs/guides/user-defined-workflows) with Inngest by providing a set of workflow actions to the **[Workflow Engine](/docs/reference/workflow-kit/engine)** while using the **[pre-built React components](/docs/reference/workflow-kit/components-api)** to build your Workflow Editor UI.
