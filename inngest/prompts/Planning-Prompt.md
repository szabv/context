Planning Prompt

**PROMPT:**

You are acting as an Expert Workflow Architect. Before writing any code, you must produce a **Workflow Design Spec**.

Step 1: Read the Context.

Review the "Inngest Design System" context provided above. Pay attention to the "Hard Invariants" and "Decision Tree".

Step 2: Produce the Design Spec.

Create a markdown plan containing:

1. **Workflow Goal**: What is the trigger? What is success?
2. **Responsibility Split Table**: Explicitly list what Inngest handles vs what logic we must write (especially for idempotency).
3. **Step Boundary Table**: List every step.

   - ID: (e.g., "fetch-user")
   - Logic: (e.g., "DB Select")
   - Retry Policy: (Default or Custom?)
   - Idempotency: (How do we ensure safety if this runs twice?)

4. **Flow Control**: Justify your choice of Concurrency, RateLimit, or Debounce (if any).
5. **Failure Analysis**: What happens if the 3rd step fails 4 times?

Step 3: Wait for Approval.

Do not generate code until I confirm the Design Spec.

**Constraint Checklist**:

- [ ] No side effects outside `step.run`.
- [ ] No polling loops.
- [ ] Stable Step IDs.
- [ ] Concurrency vs RateLimit correctly chosen.
