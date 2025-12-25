Context Pack

**PASTE THE FOLLOWING INTO YOUR CONTEXT:**

### **Inngest Design System: Compressed Context**

**1. The Mental Model**

- Inngest is **Durable Execution**. It is NOT a standard queue.
- Functions "sleep" by suspending compute. They "resume" by re-running from the top.
- **Memoization**: `step.run("id", fn)` stores results. On replay, it returns the stored result instead of running `fn`.

**2. Hard Rules (Violations = Failure)**

- **Isolation**: ALL side effects (DB, API) & Non-Determinism (Date, Random) MUST be in `step.run`.
- **Stability**: Step IDs MUST be static strings. Do not generate them dynamically.
- **Serialization**: Step outputs must be JSON-safe. Dates becoming strings.
- **Durability**: Un-awaited Promises are killed. Await everything.

**3. Decision Tree**

- Need to run code? -> `step.run`
- Need to wait for time? -> `step.sleep`
- Need to wait for signal? -> `step.waitForEvent`
- Need to call another function? -> `step.invoke` (Wait for result) OR `step.sendEvent` (Async).
- Need to limit load? -> `concurrency` (Queue).
- Need to stop abuse? -> `rateLimit` (Drop).

**4. Anti-Patterns**

- **No Polling**: Use `waitForEvent`, not `while(checkDB) sleep`.
- **No Microservice bloat**: Do not build custom worker queues. Use Inngest.
- **No Global State**: Pass data via step returns.

**5. Responsibility Split**

- **Inngest**: Retries, State Persistence, Sleep/Wake, Queuing.
- **You**: Business Logic, Idempotency (External), Data Validation, Handling `NonRetriableError`.
