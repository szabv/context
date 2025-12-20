# Flow Control & Concurrency
Rate limiting, batching, concurrency, debounce, and other execution control patterns.
Items: 20.

- [Batching events](docs/056-batching-events.md) - Flow control: Handle high load by processing events in batches.
- [Concurrency management](docs/059-concurrency-management.md) - Flow control: Limiting concurrency in systems is an important tool for correctly managing computing resources and scaling workloads.
- [Crons (Scheduled Functions)](docs/078-crons-scheduled-functions.md) - Flow control: You can create scheduled jobs using cron schedules within Inngest natively.
- [Debounce](docs/060-debounce.md) - Flow control: Avoid unnecessary function invocations by de-duplicating events over a sliding time window.
- [Debounce functions <VersionBadge version="v3.1.0+" />](docs/117-debounce-functions.md) - Flow control: Debounce delays a function run for the given `period`, and reschedules functions for the given `period` any time new events are received while the debounce is active.
- [Delayed Functions](docs/061-delayed-functions.md) - Flow control: You can easily enqueue jobs in the future with Inngest.
- [Ensure exclusive execution of a function](docs/121-ensure-exclusive-execution-of-a-function.md) - Flow control: Ensure that only a single run of a function (_or a set of specific functions, based on specific event properties_) is running at a time.
- [Flow Control](docs/065-flow-control.md) - Flow control: Learn how to manage how functions are executed with flow control.
- [Function Pausing](docs/074-function-pausing.md) - Flow control: Learn how to pause an Inngest function.
- [Function run priority <VersionBadge version="v3.2.1+" />](docs/120-function-run-priority.md) - Flow control: You can prioritize specific function runs above other runs **within the same function**.
- [Handling idempotency](docs/066-handling-idempotency.md) - Flow control: Ensuring that your code is idempotent is foundational to building reliable systems.
- [Managing concurrency](docs/050-managing-concurrency.md) - Flow control: Limit the number of concurrently running steps for your function with the [`concurrency`](/docs/reference/functions/create#configuration) configuration options.
- [Priority](docs/075-priority.md) - Flow control: Dynamically adjust the execution order of functions based on any data.
- [Rate limit function execution](docs/119-rate-limit-function-execution.md) - Flow control: Set a _hard limit_ on how many function runs can start within a time period.
- [Rate limiting](docs/076-rate-limiting.md) - Flow control: Prevent excessive function runs over a given time period by skipping events beyond a specific limit.
- [Singleton Functions <VersionBadge version="TypeScript v3.39.0+" /> <VersionBadge version="Go SDK v0.12.0+" /> <VersionBadge version="Python v0.5+" />](docs/080-singleton-functions.md) - Flow control: Singleton Functions enable you to ensure that only a single run of your function (_or a set of specific function runs, based on specific event properties_) is happening at a time.
- [Step parallelism](docs/081-step-parallelism.md) - Flow control: If you're using a serverless platform to host, code will run in true parallelism similar to multi-threading (without shared state).
- [Throttling](docs/082-throttling.md) - Flow control: Limit the throughput of function execution over a period of time.
- [Working with Loops in Inngest](docs/085-working-with-loops-in-inngest.md) - Flow control: Implement loops in your Inngest functions and avoid common pitfalls.
- [Writing expressions](docs/086-writing-expressions.md) - Flow control: Expressions are used in a number of ways for configuring your functions.
