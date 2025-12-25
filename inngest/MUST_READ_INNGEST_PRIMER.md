# Workflow Design System: Orchestrating Durable Execution with Inngest

## A) Source Index (Auditable)

The following index serves as the foundational truth for the design system. Every behavioral claim and architectural constraint detailed in this report is derived from these official Inngest documentation sources. This ensures that the guidance provided is not merely theoretical but grounded in the verified mechanics of the Inngest execution engine.

1. **Inngest LLM Context & Functions**

   - **URL:** `https://www.inngest.com/llms.txt`
   - **Supports:** `exec-model`, `steps`, `flow-control`, `middleware`, `sdk`
   - **Relevance:** This is the primary definition of the SDK surface area, listing available step primitives (`step.run`, `step.sleep`, `step.invoke`, `waitForEvent`) and configuration options. It establishes the baseline vocabulary for the design system.1

2. **How Functions Are Executed**

   - **URL:** `https://www.inngest.com/docs/learn/how-functions-are-executed`
   - **Supports:** `exec-model`, `memoization`, `determinism`, `step.run`
   - **Relevance:** Defines the mechanics of the execution engine, specifically the necessity of `step.run` for non-deterministic logic and the HTTP request/response cycle that underpins the "sleep" and "resume" functionality.2

3. **Principles of Durable Execution**

   - **URL:** `https://www.inngest.com/blog/principles-of-durable-execution`
   - **Supports:** `exec-model`, `durability`, `retries`
   - **Relevance:** Articulates the core philosophy of durable execution—externalizing memory and scheduling to ensure fault tolerance. This supports the "Anti-Microservice" stance by demonstrating how Inngest replaces custom scaffolding.3

4. **Inngest Steps Guide**

   - **URL:** `https://www.inngest.com/docs/learn/inngest-steps`
   - **Supports:** `steps`, `step.invoke`, `waitForEvent`, `sleep`
   - **Relevance:** Provides detailed behavioral rules and constraints for critical primitives, including the behavior of `step.run`, the non-blocking nature of `step.sleep`, and the composition capabilities of `step.invoke`.4

5. **Flow Control Guides (Concurrency, Throttling, Debounce)**

   - **URL:** `https://www.inngest.com/docs/guides/flow-control`
   - **Supports:** `flow-control`, `concurrency`, `throttling`, `rate-limit`
   - **Relevance:** Establishes the definitions and distinct behaviors of concurrency (queueing), rate limiting (dropping), and debouncing (deduplicating), which are crucial for correct tool selection.5

6. **Rate Limiting vs. Throttling**

   - **URL:** `https://www.inngest.com/docs/guides/rate-limiting`
   - **Supports:** `flow-control`, `rate-limit`
   - **Relevance:** Clarifies the specific v3 SDK nomenclature change where "throttle" was renamed to "rateLimit" and confirms the behavioral difference (skipping events vs. queueing), preventing data loss due to misconfiguration.6

7. **Debounce Guide**

   - **URL:** `https://www.inngest.com/docs/guides/debounce`
   - **Supports:** `flow-control`, `debounce`
   - **Relevance:** Defines the timing constraints (max 7 days, min 1 second) and the sliding window behavior of the debounce primitive.8

8. **Handling Failures & Retries**

   - **URL:** `https://www.inngest.com/docs/reference/functions/handling-failures`
   - **Supports:** `retries`, `errors`, `failure-modes`
   - **Relevance:** details the default retry policies (4 retries), the implementation of `onFailure` handlers, and the usage of `NonRetriableError` to short-circuit retry loops.9

9. **Inngest Errors**

   - **URL:** `https://www.inngest.com/docs/features/inngest-functions/error-retries/inngest-errors`
   - **Supports:** `errors`, `retries`
   - **Relevance:** Technical documentation on standard error handling and the specific `NonRetriableError` class required for control flow in failure scenarios.10

10. **Versioning & Deployment**

    - **URL:** `https://www.inngest.com/docs/learn/versioning`
    - **Supports:** `versioning`, `deployment`, `determinism`
    - **Relevance:** Outlines safety rules for adding/removing steps, the importance of step ID stability for replayability, and the implications of strict mode for determinism.11

11. **Idempotency Guide**

    - **URL:** `https://www.inngest.com/docs/guides/handling-idempotency`
    - **Supports:** `idempotency`, `deduplication`
    - **Relevance:** Explains the built-in event deduplication mechanisms (24h window), function-level idempotency keys, and strategies for ensuring safe fan-out execution.12

12. **Cancellation**

    - **URL:** `https://www.inngest.com/docs/features/inngest-functions/cancellation`
    - **Supports:** `cancellation`, `control-flow`
    - **Relevance:** Documents the `cancelOn` configuration for event-driven cancellation, bulk cancellation APIs, and timeout-based cancellation strategies.13

13. **Invoking Functions**

    - **URL:** `https://www.inngest.com/docs/reference/functions/step-invoke`
    - **Supports:** `invoke`, `composition`
    - **Relevance:** details the syntax and behavior for `step.invoke`, including timeout handling and the serialization of payloads between parent and child workflows.15

14. **Batching Events**

    - **URL:** `https://www.inngest.com/docs/guides/batching`
    - **Supports:** `batching`, `triggers`
    - **Relevance:** Provides configuration guidance for batching multiple events into single function executions to optimize throughput and cost.16

15. **SDK Migration (v2 to v3)**

    - **URL:** `https://www.inngest.com/docs/sdk/migration`
    - **Supports:** `sdk`, `changes`
    - **Relevance:** Highlights critical changes like the rename of `throttle` to `rateLimit` and updates to top-level `await` restrictions, ensuring the design system uses current best practices.6

16. **AI Agents & Patterns**

    - **URL:** `https://www.inngest.com/docs/examples/ai-agents-and-rag`
    - **Supports:** `patterns`, `ai`, `agents`
    - **Relevance:** Offers reference architectures for RAG, autonomous agents, and long-running AI processes, serving as the basis for the agentic patterns in this report.17

---

## B) Hard Invariants: "Paint Inside the Lines"

The Inngest execution model relies on specific physical laws of serverless and durable execution. These are not merely suggestions; they are constraints enforced by the runtime. Violating these invariants will result in non-deterministic behavior, data corruption, infinite loops, or silent failures.

### 1. The Step Isolation Rule

- **Rule:** Every interaction with the outside world (DB, API, external service) or non-deterministic operation (random number generation, date instantiation) MUST be wrapped in `step.run()`.
- **Why It Exists:** Inngest functions execute repeatedly via a replay mechanism. When a function "sleeps" or "waits," the underlying compute is terminated. When it resumes, the function re-runs from the very beginning. `step.run` acts as a memoization boundary: if a step has already completed, Inngest injects the stored result instead of re-executing the code.
- **Failure Modes:** If `Math.random()` or a database `INSERT` is placed outside a step, it will execute _every single time_ the function wakes up for a subsequent step. This leads to duplicate database records, different random values on each replay (breaking logic), and "phantom" API calls.
- **Citations:** "Any non-deterministic logic (such as DB calls or API calls) must be placed within a step.run() call to ensure it executes efficiently and correctly.".2

### 2. The Step ID Stability Rule

- **Rule:** The `id` string passed to `step.run("my-step-id",...)` MUST remain constant across deployments unless re-execution is explicitly desired.
- **Why It Exists:** Inngest uses this string ID to create a deterministic hash for looking up memoized results in its state store. If you change "fetch-user" to "get-user", the hash changes. Inngest treats this as a completely new step and will execute it, even if the logical intent was the same.
- **Failure Modes:** Changing an ID during a refactor can cause active functions to re-run expensive or dangerous operations (e.g., charging a credit card twice) because the system no longer recognizes the step as having been completed.
- **Citations:** "Internally, the step's ID is hashed as the state identifier... If you need to force a step to re-evaluate... you can change its step ID.".11

### 3. The Serialization Boundary Rule

- **Rule:** Data returned from `step.run` must be strictly JSON-serializable. Complex types like `Date` objects, `Map`, `Set`, and custom classes will be lost or converted to strings/arrays.
- **Why It Exists:** The results of steps are persisted to Inngest's cloud state (internally using Postgres/Redis) via HTTP JSON bodies. The serialization process strips non-JSON data types.
- **Failure Modes:** A `Date` object returned from a step will become an ISO string in subsequent steps. Logic expecting `date.getTime()` will throw a runtime error ("not a function"), causing the workflow to crash on replay.
- **Citations:** "Code wrapped in step.run() is automatically retried... response is saved in the function's run state.".4 _Inferred Best Practice_: Always cast dates back to objects immediately after retrieval if prototype methods are needed.

### 4. The "Sleep is a Stop" Rule

- **Rule:** `step.sleep()` does not block a thread; it completely terminates the function execution and schedules a future trigger.
- **Why It Exists:** Inngest operates on a serverless model. You do not pay for compute time while a function is sleeping. The runtime snapshots the state (memoized steps) and kills the process, scheduling a wake-up event for the future.
- **Failure Modes:** Any local variables that are not derived from `step.run` results or `event` data will be lost when the function resumes. Stateful in-memory accumulators (e.g., `let count = 0`) will reset to their initial value on every wake-up.
- **Citations:** "When a function is sleeping, it does not use any compute; Inngest handles the scheduling of the resumption.".4

### 5. The 24-Hour Event Idempotency Limit

- **Rule:** Inngest's built-in event deduplication using the event `id` or specific `idempotency` keys only guarantees uniqueness for a window of 24 hours.
- **Why It Exists:** This is a documented platform constraint designed to manage storage and performance of the deduplication index.
- **Failure Modes:** Relying on Inngest to prevent a "User Welcome" workflow from running twice for the same user will fail if the duplicate `user.created` events are separated by more than 24 hours.
- **Citations:** "This id acts as an idempotency key over a 24 hour period... After 24 hours, a new event... will trigger another function execution.".12

### 6. The "No Promise Leaks" Rule

- **Rule:** Do not create fire-and-forget Promises (e.g., `db.save()`) without `await` inside the main handler or a step.
- **Why It Exists:** The runtime environment (often Lambda or similar serverless containers) may freeze or recycle the environment immediately after the function returns its response or suspends for a step. Un-awaited promises will be terminated mid-execution.
- **Failure Modes:** Data loss where logs or database updates "sometimes" happen and sometimes don't, leading to distinct non-determinism and debugging nightmares.
- **Citations:** _Confirmed constraint of the underlying serverless compute models Inngest relies on (e.g., Vercel/Lambda)._

### 7. The Event Payload Size Cap

- **Rule:** Event payloads should be kept small, typically under 512KB to 1MB depending on the specific plan and integration.
- **Why It Exists:** Large payloads increase latency, storage costs, and risk hitting API gateway limits of the underlying infrastructure.
- **Failure Modes:** Events failing to ingest entirely, or function triggers failing silently if payloads exceed the hard limits of the Inngest API or the user's server.
- **Citations:** _Inferred Best Practice based on standard webhook and serverless constraints referenced in general documentation._

### 8. The "Rate Limit Skips, Throttle Queues" Rule

- **Rule:** If you use `rateLimit`, excess events are **dropped**. If you use `concurrency` (or the older `throttle` concept in some contexts), excess events are **queued**.
- **Why It Exists:** These primitives serve different purposes. Rate limiting is for abuse protection (preventing system overload by rejecting traffic). Concurrency is for load management (processing everything, but at a controlled pace).
- **Failure Modes:** Selecting `rateLimit` for a payment processing workflow will result in lost revenue because valid payment events will be deleted if they arrive in a burst, rather than being processed slowly.
- **Citations:** "Rate limiting ensures that a function runs once... skipping any events that exceed a specific limit... while [Concurrency] manages concurrent work.".5

### 9. The Deterministic Replay Rule

- **Rule:** Logic outside `step.run` must be strictly idempotent and deterministic.
- **Why It Exists:** The function handler runs from the top _every time_ a step completes. The code between steps is re-executed to reconstruct the state of the workflow.
- **Failure Modes:** If you define `const timestamp = Date.now()` at the top of your function scope, `timestamp` will have a different value on every step completion. Logic that relies on this timestamp remaining constant (e.g., checking if a timeout has passed) will break.
- **Citations:** "Placing business logic outside of a step.run() call is a bad idea, as this will be run every time.".18

### 10. The Max Sleep Duration Rule

- **Rule:** `step.sleep` supports a maximum duration of 1 year on Standard plans, and 7 days on the Free tier.
- **Why It Exists:** Platform resource constraints and storage limits.
- **Failure Modes:** Workflows effectively crashing or throwing validation errors if logic attempts to schedule a sleep for `5y`.
- **Citations:** "Functions can sleep for a maximum of one year.".4

### 11. The Step Retry Independence Rule

- **Rule:** Retries configured at the function level apply to _each step individually_, not to the function execution as a single unit.
- **Why It Exists:** Inngest treats steps as atomic units of execution. If `retries: 3` is set, Step A can fail 3 times and succeed, and then Step B can fail 3 times.
- **Failure Modes:** Underestimating the total possible execution time of a workflow. A 5-step workflow with 3 retries per step could theoretically experience 15 failures and significant backoff delays while still eventually succeeding.
- **Citations:** "Each step.run() has its own independent retry counter... not as a shared pool.".19

### 12. The "Strict Mode" Deployment Rule

- **Rule:** If you change the order of existing steps or insert new steps in the middle of a sequence, you must handle versioning or accept warnings/failures unless you use a new function ID.
- **Why It Exists:** When replaying an existing run on new code, Inngest expects the sequence of step hashes to match the history. If they diverge, the replay cannot guarantee correctness.
- **Failure Modes:** "Step mismatch" errors during deployment if active runs are in-flight, potentially causing those runs to fail permanently.
- **Citations:** "When you add a new step Z in-between... the executor will run steps... caveat here is that you must take care to ensure that the new step can run out-of-order.".11

---

## C) Capability Map: "What Inngest Provides" vs "What You Must Design"

This map delineates the boundary between the platform's responsibility and the agent's design duties. It is crucial to understand that Inngest provides the _mechanism_ for reliability, but the _logic_ of reliability remains an application concern.

| **Feature Area**  | **Inngest Provides (Do NOT Rebuild)**                                                           | **Agent Must Design (Requires Decisions)**                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **State**         | **Step Memoization**: `step.run` output is persisted automatically and injected on replay. 4    | **State Model**: Defining exactly what data to return from steps and how to pass it to subsequent steps.                                           |
| **Retries**       | **Automatic Retries**: Exponential backoff (default) or custom policies applied to errors. 19   | **Failure Classification**: Deciding which errors are `NonRetriableError` (e.g., 400 Bad Request) vs retryable (e.g., 503 Service Unavailable). 10 |
| **Scheduling**    | **Durable Timers**: `step.sleep`, `step.sleepUntil` manage long waits without compute cost. 1   | **Business Timing**: Calculating _when_ to wake up (e.g., computing "3 days before subscription end").                                             |
| **Concurrency**   | **Global/Keyed Locking**: `concurrency` key ensures limited parallel execution. 20              | **Granularity**: Choosing the correct key (e.g., `user_id` vs `account_id`) to avoid starving users while protecting resources.                    |
| **Events**        | **Buffering & Triggering**: Ingests events, buffers them, and triggers matching functions. 16   | **Event Schema**: Defining the JSON contract for `event.data` and ensuring payloads are efficient.                                                 |
| **Orchestration** | **Wait for Event**: `step.waitForEvent` pauses execution until a specific signal arrives. 4     | **Timeout Logic**: Defining what to do if the expected event _doesn't_ arrive (escalation paths, fallback logic).                                  |
| **Idempotency**   | **Deduplication**: 24h window based on event ID or `idempotency` key. 12                        | **Side Effect Safety**: Ensuring the _code inside_ `step.run` handles partial failures (e.g., checking if a record exists before inserting).       |
| **Flow Control**  | **Throttling/Rate Limiting**: Mechanisms to queue or drop excess load based on configuration. 5 | **Policy Selection**: Deciding whether to Drop (`rateLimit`) or Queue (`concurrency`) based on business criticality.                               |
| **Cleanup**       | **Cancellation**: `cancelOn` automatically kills runs when specific events occur. 14            | **Compensation**: Writing the logic to undo previous steps if a workflow is cancelled (using `onFailure` or manual checks).                        |

---

## D) Tool Selection System: Swiss-Army-Knife Chooser

### D1) Decision Tree

**1. Do you need to run code?**

- **Yes, and it has side effects (DB, API) or is non-deterministic (Time, Random):** Use **`step.run`**.
- **Yes, but it is purely creating a derived variable (e.g., `const x = event.data.amount * 2`):** Plain code is acceptable (Conf: 21), but using `step.run` is safer if you want visibility of the input/output in the Inngest dashboard logs.

**2. Do you need to wait?**

- **For a specific duration?**: Use **`step.sleep`**.
- **Until a specific timestamp?**: Use **`step.sleepUntil`**.
- **For an external signal (user clicked link, webhook arrived)?**: Use **`step.waitForEvent`**.
  - _Warning_: Do NOT build a `while` loop with `step.run` checking a DB. That is "polling" and is a severe anti-pattern. Use `waitForEvent`.

**3. Do you need to trigger another process?**

- **Do you need the result back immediately (in the same workflow)?**: Use **`step.invoke`**.
  - _Note_: This tightly couples the workflows.
- **Do you just want to kick it off and forget it?**: Use **`step.sendEvent`**.
  - _Note_: This is "Fire and Forget" decoupling.
- **Do you need to run the SAME logic for many items (Fan-out)?**:
  - Use **`step.sendEvent`** (sending a batch of events, one per item).
  - _Then_ have a separate function trigger off that event.

**4. How do you handle high load?**

- **Must process every request eventually (e.g., payments)?**: Use **`concurrency`** (queues them).
- **Can drop excess requests (e.g., "user is typing" notifications)?**: Use **`rateLimit`** (drops them).
- **Want to process only the latest request in a window (e.g., "save settings")?**: Use **`debounce`**.

### D2) Comparison Matrix

| **Primitive A**   | **Primitive B**         | **Decision Rule**                                                                                            | **Failure Mode if Wrong**                                                | **Citation** |
| ----------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------ |
| **`step.run`**    | **Raw Code**            | Use `step.run` for **any** I/O, random, or time-based logic. Use Raw Code only for pure variable assignment. | Duplicate API calls (e.g., charging $10 twice) if function replays.      | 2            |
| **`step.sleep`**  | **`step.waitForEvent`** | Use `sleep` for time. Use `waitForEvent` for signals.                                                        | `sleep` + polling loops waste retries, money, and compute.               | 4            |
| **`step.invoke`** | **`step.sendEvent`**    | Use `invoke` when you need the _return value_. Use `send` for async fan-out.                                 | `invoke` on 1000 items sequentially will timeout the parent function.    | 22           |
| **`concurrency`** | **`rateLimit`**         | `concurrency` = Queue (FIFO). `rateLimit` = Drop (Reject).                                                   | `rateLimit` on a payment webhook causes lost revenue (dropped events).   | 5            |
| **`onFailure`**   | **`try/catch`**         | Use `try/catch` inside `step.run` for _recoverable_ logic. Use `onFailure` for final alerting/cleanup.       | `try/catch` wrapping the whole handler breaks Inngest's retry mechanism. | 9            |

---

## E) Workflow Design Method (The Planning Algorithm)

**Role:** You are the Architect. You must produce a spec before writing code.

### E0) Responsibility Split (ANTI-MICROSERVICE ANCHOR) — REQUIRED

_Instructions for Agent:_ You must explicitly list this section in your plan.

**Inngest Handles (CONFIRMED):**

- **Durability**: If the server crashes, Inngest resumes the function at the last successful step.2
- **Retries**: Inngest retries failed steps automatically with backoff.19
- **State**: Inngest stores the return value of every `step.run`.4
- **Queuing**: Inngest manages the queue for `concurrency` limits.5

**We Handle (Design Decisions):**

- **Step Granularity**: Breaking code into atomic `step.run` blocks.
- **Idempotency**: Ensuring `step.run` logic can run twice safely (in case of failure _during_ the step but before Inngest records success).
- **Non-Retriable Errors**: deciding when to `throw new NonRetriableError()`.10
- **Data Contracts**: Ensuring step outputs are JSON serializable.

### E1) The Method (Steps)

1. **Define the Trigger**:

   - Is it an Event (`user.signup`), Cron (`0 9 * * *`), or Webhook?
   - _Constraint Check_: If Event, is the payload < 512KB?

2. **Define the Goal & Completion**:

   - What constitutes "Success"? (e.g., "User is in Stripe AND Database AND Email sent").

3. **Sketch the Steps (The Graph)**:

   - Draft the sequence: A -> B -> Wait -> C.
   - _Heuristic_: Any API call, DB write, or significant wait MUST be a step.

4. **Apply Hard Invariants**:

   - Wrap all side effects in `step.run`.
   - Give every step a stable, descriptive string ID (e.g., `"create-stripe-customer"` not `"step-1"`).

5. **Select Flow Control**:

   - Does this need `concurrency` (to protect my DB)?
   - Does this need `idempotency` (to prevent double-runs)?
   - _Citation_: "Idempotency keys... prevents duplicate execution of the function".12

6. **Plan Failure Handling**:

   - What if Step B fails? (Default: Retry 4 times).
   - Is that acceptable? If not, add `retries: 0` to the step option.
   - What if it fails permanently? Define `onFailure` handler (e.g., alert Slack).

7. **Data Flow Check**:

   - Step A returns X. Step B needs X.
   - _Constraint_: Is X JSON serializable? (No raw Dates/Classes).

8. **Wait Strategy**:

   - Are we polling? -> **STOP**. Change to `waitForEvent`.
   - Are we waiting for a human? -> Use `waitForEvent` with a long timeout (e.g., 7 days).

9. **Test Plan**:

   - How to test? (Use Inngest Dev Server).
   - Mocking? (Mock `step.run` outputs).

10. **Versioning Strategy**:

    - Will this change often?
    - _Rule_: If changing logic, consider a new function version or strictly appending steps.

### E2) Design Artifacts (Output Templates)

#### **Artifact 1: Workflow Design Spec**

# Workflow: [Name]

Trigger:

Goal: [One sentence objective]

**Responsibility Split**:

- Inngest: Retries, State, Sleep.
- App: Logic, Idempotency, Data Validation.

**Flow Control**:

- Concurrency: [Key | Limit | None] (Reasoning:...)
- Idempotency: [Key | None] (Reasoning:...)
- Rate Limit: [Limit | None] (Reasoning:...)

**Steps Plan**:

1. `step.run("validate-input")`: Checks payload.
2. `step.run("charge-card")`: Calls Stripe. (Idempotency: Stripe Idempotency-Key header).
3. `step.sleep("wait-for-settlement")`: Sleeps 10m.
4. `step.run("send-email")`: Calls Resend.

#### **Artifact 2: Step Boundary Table**

| **Step ID**   | **Action**    | **Side Effect?** | **Idempotency Strategy**                     | **Retry Policy** |
| ------------- | ------------- | ---------------- | -------------------------------------------- | ---------------- |
| `charge-card` | POST /charges | YES (Money)      | Pass `event.id` as Idempotency Key to Stripe | Default (4)      |
| `update-db`   | UPDATE users  | YES (Data)       | UPSERT or Check-then-Write                   | Default (4)      |
| `send-email`  | POST /emails  | YES (Comms)      | None (Duplicate email is acceptable risk)    | 2 (Don't spam)   |

---

## F) Patterns, Anti-Patterns, and Planning Templates

### F1) Patterns (Proven Designs)

**1. The "Standard Async" Pattern**

- **Context**: A linear sequence of tasks that must happen in order.
- **How**: `step.run` -> `step.run` -> `step.run`.
- **Why**: Basic durability. If Step 2 fails, Step 1 is not repeated.
- **Failure Mode**: If steps are not atomic, partial failures inside a step can cause issues on retry.

**2. The "Human-in-the-Loop" Pattern**

- **Context**: Pausing a workflow to wait for user approval (e.g., Expense Report).
- **How**:
  1. Send Email (`step.run`).
  2. `step.waitForEvent("wait-approval", { event: "approval.received", timeout: "7d" })`.
  3. Check result. If timeout, escalate. If approved, proceed.
- **Why**: Replaces polling loops or complex state machines in DB.
- **Citation**:.4

**3. The "Fan-Out/Fan-In" Pattern**

- **Context**: Processing a large batch of items (e.g., 1000 items from a CSV).
- **How**:
  1. `step.run`: Parse CSV, return array of IDs.
  2. `step.sendEvent`: Send a `process.item` event for each ID (use batching).
  3. (Separate Function): Triggers on `process.item` to handle each item.
- **Why**: Avoids function timeout on large batches. "Parallel" steps (`step.run` with `Promise.all`) are also possible but limited by the single function's timeout and memory.

**4. The "Saga" Pattern (Compensation)**

- **Context**: Step 3 fails, and you need to undo the effects of Step 1.
- **How**: Inngest does not have native "Saga" rollback syntax.
  - _Best Practice_: If critical, build a "Compensator" function triggered on the `inngest/function.failed` event that examines the run state and reverses actions. Alternatively, handle specific known errors in `step.run` with try/catch to run compensation logic immediately.

**5. The "Sleep-Check-Escalate" Pattern**

- **Context**: Reminding a user if they haven't finished onboarding.
- **How**:
  1. `step.waitForEvent` (wait for completion signal).
  2. If `event` is null (timeout) -> Send Reminder (`step.run`).
  3. `step.waitForEvent` (wait again).
  4. If null -> Mark churned.

**6. The "Buffering" Pattern (Batching)**

- **Context**: Don't run the function for _every_ event; process them in groups to save API calls.
- **How**: Configure `batchEvents` in `createFunction` (e.g., `maxSize: 100`, `timeout: "5s"`).
- **Citation**:.16

**7. The "Debounced Update" Pattern**

- **Context**: User is typing settings; save draft only after 5s of silence.
- **How**: Configure `debounce: { period: '5s', key: 'event.data.userId' }`.
- **Citation**:.8

**8. The "Rate Limited Webhook" Pattern**

- **Context**: Sending data to a fragile 3rd party API that crashes if hit too fast.
- **How**: Configure `rateLimit: { limit: 10, period: '1m' }` on the _sender_ function.
- **Citation**:.7

**9. The "External Idempotency" Pattern**

- **Context**: `step.run` calling a payment API (Stripe).
- **How**: Generate a unique key _outside_ the API call (or use `event.id`). Pass it to the API in the request (e.g., `Idempotency-Key` header).
- **Why**: If `step.run` crashes _after_ Stripe replies but _before_ Inngest saves the success state, the step will retry. Stripe needs to see the same key to say "Already done" instead of charging again.

**10. The "Wait for Duration" Pattern**

- **Context**: Free trial expiration.
- **How**: `step.sleepUntil(event.data.trialEndsAt)`.
- **Why**: Much more efficient than checking a DB every hour.

**11. The "Dynamic Step" Pattern**

- **Context**: Looping over an array to run steps sequentially.
- **How**:
  JavaScript
  ```
  for (const item of items) {
     await step.run(`process-${item.id}`, () => process(item));
  }
  ```
- **Constraint**: Step IDs must be deterministic and unique (using `item.id`).

**12. The "Singleton" Pattern**

- **Context**: Only one import job per account allowed at a time.
- **How**: `concurrency: { limit: 1, key: 'event.data.accountId' }`.

### F2) Anti-Patterns (The "Don't Do This" List)

**1. The "Microservice Instinct" (Manual Queues)**

- **Bad:** Creating a `jobs` table in Postgres and writing a separate worker poller to pick up jobs.
- **Good:** Just use `step.run`. Inngest _is_ the queue and the state manager.
- **Why:** Reimplementing queues adds maintenance burden and lacks the integrated observability Inngest provides.

**2. The "Polling Loop"**

- **Bad:** `while (!complete) { await checkDB(); await step.sleep('1m'); }`
- **Good:** `step.waitForEvent`.
- **Why:** Polling wastes cycles, money, and pollutes logs. Inngest's event-driven architecture is designed to avoid this.

**3. The "Unstable ID"**

- **Bad:** `step.run("step-" + Math.random(),...)`
- **Good:** `step.run("step-user-123",...)`
- **Why:** Breaks recovery. Inngest cannot resume execution if the ID changes on replay, leading to re-execution of logic that should have been skipped.

**4. The "Global State" Assumption**

- **Bad:** Setting a global variable `let counter = 0` outside the handler and expecting it to persist between steps.
- **Good:** Passing state through step returns or storing in an external DB.
- **Why:** Functions are stateless. The environment is torn down during sleep. Global variables are reset on new instances.

**5. The "Try/Catch Wrapper"**

- **Bad:** Wrapping the entire handler in a generic `try/catch`.
- **Good:** Let errors bubble up so Inngest can handle retries and observability. Use `onFailure` for final handling.
- **Why:** Catching all errors hides them from Inngest, preventing automatic retries and backoff.

**6. The "Big Ball of Mud" Step**

- **Bad:** One huge `step.run("do-everything",...)` with 5 distinct API calls inside.
- **Good:** Break into 5 distinct steps.
- **Why:** If call 5 fails, the "Mud" step retries calls 1-4 again, which causes dangerous side effects (e.g., sending 4 emails before crashing on the 5th).

**7. The "Fire-and-Forget Promise"**

- **Bad:** Calling `email.send()` without `await`.
- **Good:** `await step.run('send', () => email.send())`.
- **Why:** The runtime freezes background work immediately upon return or sleep. The promise will likely never complete.

**8. The "Date Object" Return**

- **Bad:** Returning `{ date: new Date() }` from a step and expecting `result.date.getTime()` to work in the next step.
- **Good:** `new Date(result.date).getTime()`.
- **Why:** Serialization converts Dates to ISO strings. Attempting to call methods on the string will crash the workflow..23

**9. The "Rate Limit Confusion"**

- **Bad:** Using `rateLimit` when you meant `concurrency`.
- **Result:** Users get "silently ignored" (Data Loss) instead of "processed slowly" (Queued).

**10. The "Infinite Recursive" Loop**

- **Bad:** Function A triggers Event A, which triggers Function A... forever, without exit conditions.
- **Good:** Check recursion depth or use strict termination conditions.
- **Why:** This consumes infinite budget and quota.

**11. The "Deployment Surprise"**

- **Bad:** Inserting a step in the middle of a live function without changing the function ID or handling versioning.
- **Result:** "Step Mismatch" errors for currently running functions..11

**12. The "Heavy Payload"**

- **Bad:** Passing a 5MB base64 image in `event.data`.
- **Good:** Upload to S3, pass the URL.
- **Why:** large payloads degrade performance and reliability.

### F3) Planning Templates

**Template 1: The Automation Pipeline**

- **Use Case**: User Uploads CSV -> Parse -> Enrich -> Save -> Email.
- **Key Primitive**: `step.run` sequence.
- **Failure**: Retry enrichment, alert on Save fail.

**Template 2: The Agentic Loop**

- **Use Case**: AI Agent receives goal -> Thinks -> Calls Tool -> Repeats.
- **Key Primitive**: `step.invoke` (calling tools) or `step.run` (calling LLM).
- **Looping**: `for` loop with `max_iterations` check to prevent runaways.

**Template 3: The Durable Async Service**

- **Use Case**: Generate PDF (takes 4 mins).
- **Key Primitive**: `concurrency` (limit PDF generation load), `step.run` (generate), `step.sendEvent` (notify completion).

**Template 4: The Fan-Out**

- **Use Case**: Send newsletter to 10k users.
- **Key Primitive**: `step.run` (get list) -> `step.sendEvent` (batch events to trigger worker functions).

**Template 5: The Human Gate**

- **Use Case**: Deploy to Prod -> Wait for Manual Approval.
- **Key Primitive**: `step.waitForEvent`.

**Template 6: The Long Wait**

- **Use Case**: Send follow-up email 30 days later.
- **Key Primitive**: `step.sleep('30d')`.
