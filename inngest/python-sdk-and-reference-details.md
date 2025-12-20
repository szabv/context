# Python SDK & Reference
Python SDK reference for clients, functions, steps, and migration notes.
Items: 22.

- [Create Function](docs/135-create-function.md) - Python: Define your functions using the `create_function` decorator.
- [Environment variables](docs/145-environment-variables.md) - Python: You can use environment variables to control some configuration.
- [Inngest client](docs/133-inngest-client.md) - Python: The Inngest client is used to configure your application and send events outside of Inngest functions.
- [Invoke <VersionBadge version="v0.3.0+" />](docs/147-invoke.md) - Python: Calls another Inngest function, waits for its completion, and returns its output.
- [Invoke by ID <VersionBadge version="v0.3.0+" />](docs/148-invoke-by-id.md) - Python: Calls another Inngest function, waits for its completion, and returns its output.
- [Middleware <VersionBadge version="v0.3.0+" />](docs/141-middleware.md) - Python: Middleware allows you to run code at various points in an Inngest function's lifecycle.
- [Modal](docs/136-modal.md) - Python: This guide will help you use setup an Inngest app in [Modal](https://modal.com), a platform for building and deploying serverless Python applications.
- [Parallel <VersionBadge version="v0.3.0+" />](docs/149-parallel.md) - Python: Run steps in parallel.
- [Production mode](docs/146-production-mode.md) - Python: When the SDK is in production mode it will try to connect to Inngest Cloud instead of the Inngest Dev Server.
- [Pydantic](docs/137-pydantic.md) - Python: This guide will help you use Pydantic to perform runtime type validation when sending and receiving events.
- [Python middleware lifecycle](docs/140-python-middleware-lifecycle.md) - Python: The order of middleware lifecycle hooks is as follows.
- [Python SDK](docs/139-python-sdk.md) - Python: Read the Python [quick start guide](/docs/getting-started/python-quick-start) to learn how to add Inngest to a FastAPI app and run an Inngest function.
- [Python SDK migration guide: v0.3 to v0.4](docs/143-python-sdk-migration-guide-v0-3-to-v0-4.md) - Python: This guide will help you migrate your Inngest Python SDK from v0.3 to v0.4 by providing a summary of the breaking changes.
- [Python SDK migration guide: v0.4 to v0.5](docs/144-python-sdk-migration-guide-v0-4-to-v0-5.md) - Python: This guide will help you migrate your Inngest Python SDK from v0.4 to v0.5.
- [Run](docs/150-run.md) - Python: Turn a normal function into a durable function.
- [Send event](docs/151-send-event.md) - Python: Note: This guide is for sending events from *inside* an Inngest function.
- [Send events](docs/134-send-events.md) - Python: Note: This guide is for sending events from *outside* an Inngest function.
- [Sleep](docs/153-sleep.md) - Python: Sleep for a period of time.
- [Sleep until](docs/152-sleep-until.md) - Python: Sleep until a specific time.
- [Testing](docs/138-testing.md) - Python: If you'd like to unit test without an Inngest server, the `mocked` (requires `v0.4.14+`)  library can simulate much of the Inngest server's behavior.
- [undefined](docs/142-undefined.md) - Python: undefined.
- [Wait for event](docs/154-wait-for-event.md) - Python: Wait until the Inngest server receives a specific event.
