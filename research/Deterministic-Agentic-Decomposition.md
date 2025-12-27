# Protocol for Deterministic Agentic Decomposition and Verification Standards

## 1. Introduction: The Agentic Paradigm Shift

The transition from human-centric software development to agentic coding represents a fundamental discontinuity in the history of software engineering. For decades, development methodologies—from Waterfall to Agile to DevOps—have been predicated on the cognitive flexibility of the human engineer. Humans possess an innate ability to navigate ambiguity, bridge semantic gaps in requirements, and intuitively manage the scope of a task based on implicit context. However, as we integrate Large Language Models (LLMs) and autonomous agents into the build loop, these human-centric assumptions become liabilities. Agents are not engineers; they are probabilistic inference engines operating on distinct token-based cognitive architectures. They do not "understand" system architecture in the semantic sense; they predict the next plausible sequence of code based on the limited context provided in their active window.

This fundamental difference necessitates a new architectural standard for defining work. We can no longer rely on vague, semantic task definitions like "Update the user profile page." Such instructions, while sufficient for a human who knows where the profile component lives and how it interacts with the database, act as "poison pills" for agents. They invite "Context Mud"—a state where the agent, seeking to resolve ambiguity, ingests massive amounts of irrelevant codebase context, degrading its signal-to-noise ratio and increasing the probability of hallucination.

This report defines the Task Definition Standard (TDS) and the Mechanical Decomposition Decision System (MDDS). These are not project management guidelines; they are rigorous, schema-driven protocols designed to bridge the "Determinism Gap" between the probabilistic nature of AI agents and the binary, deterministic requirements of compilers and infrastructure. The objective is to industrialize the decomposition of software features into atomic, verifiable units of work—TaskCards—that can be executed by agents with a mathematical probability of success approaching 100%.

### 1.1 The Determinism Gap and Context Economics

The core friction in agentic workflows lies in the "Determinism Gap." Enterprise environments, compilers, and infrastructure states are deterministic: inputs produce predictable outputs. A syntax error is a hard stop; a failed migration is a binary state. Conversely, agents are probabilistic. When a probabilistic agent interacts with a deterministic compiler, the interface must be rigid to prevent the agent from "hallucinating success." If an agent is tasked broadly with "checking if the code works," it may probabilistically interpret a warning as a success or overlook a silent failure. The TDS requires that all success criteria be reduced to hard interfaces—explicit states, allowed actions, and tool schemas—where the agent’s judgment is replaced by mechanical verification.

Furthermore, we must operate under the constraints of "Context Economics." Agent capability in completing long-horizon tasks is improving, yet agents still struggle with context saturation. The MDDS treats "tokens" as a finite, expensive currency. Every file, every line of log output, and every instruction added to a TaskCard context reduces the statistical probability of correct code generation. Decomposition, therefore, is not merely an organizational preference; it is a mathematical necessity. By mechanically restricting the scope of each task, we maintain the context complexity below the threshold where "Context Mud" begins to degrade the agent's reasoning capabilities.

## 2. The Task Definition Standard (TDS)

The Task Definition Standard (TDS) provides the rigid, machine-readable schema that governs the communication between the high-level Decomposition Layer (the "Breakdown Agent") and the low-level Execution Layer (the "Executor Agents"). It replaces the ambiguity of natural language tickets with invariant-heavy JSON structures. This standard draws architectural inspiration from Amazon ECS Task Definitions and Microsoft's Declarative Agent Manifests, adapting their rigid structure for the ephemeral, iterative nature of coding tasks.

### 2.1 The TaskPlan Topology

The TaskPlan acts as the parent container for a specific feature request or architectural refactor. It serves as the immutable "Constitution" for the lifecycle of that feature's implementation, enforcing global constraints and defining the Directed Acyclic Graph (DAG) of dependent tasks. Unlike a simple list of to-dos, the TaskPlan is a state machine that tracks the integrity of the repository throughout the build process.

#### 2.1.1 TaskPlan Schema Specification

The schema is designed to enforce "Intent Lock," preventing the common drift where agents wander into refactoring unrelated code or upgrading dependencies without authorization.

```json
{
  "plan_id": "TP_UUID_v4_SHA256",
  "meta": {
    "generated_at": "ISO_8601_TIMESTAMP",
    "generator_version": "MDDS_v2.1",
    "intent_checksum": "sha256_of_original_user_query"
  },
  "intent_lock": {
    "primary_objective": "Implement JWT Authentication Middleware",
    "anti_patterns":,
    "global_context_limit": 32000,
    "strategy_mode": "ATOMIC_VERTICAL_SLICE"
  },
  "repository_state": {
    "branch": "feature/auth-middleware-implementation",
    "base_commit": "git_sha_at_start",
    "locked_paths": [
      "package.json",
      "pnpm-lock.yaml",
      "infra/terraform/modules/vpc/*"
    ],
    "protected_regions": {
      "src/shared/kernel": "READ_ONLY"
    }
  },
  "execution_graph": {
    "nodes":,
    "edges":
  },
  "verification_protocol": {
    "global_gate": "npm run build && npm run test:unit",
    "failure_policy": "ROLLBACK_TO_BASE_COMMIT"
  }
}
```

#### 2.1.2 Schema Component Analysis

**The Intent Lock and Anti-Patterns:** The intent_lock object specifically addresses the risk of context poisoning and scope creep. By explicitly listing anti_patterns, we utilize negative constraints, which research suggests are critical for bounding LLM behavior in security-sensitive contexts. For instance, prohibiting changes to tsconfig.json prevents the agent from resolving a type error by relaxing the compiler rules—a common "lazy" failure mode in agentic coding.

**Repository State and Immutable Infrastructure:** The locked_paths array enforces the principle of "Immutable Infrastructure" within the codebase. Agents are often tempted to modify configuration files to bypass build errors. By mechanically locking package.json or Terraform modules, we force the agent to solve the problem within the application logic, ensuring the build environment remains deterministic. The protected_regions feature allows for fine-grained access control, designating core kernel logic as "Read Only" to prevent accidental destabilization of the system architecture.

**The Execution Graph:** The execution_graph does not merely list tasks; it defines dependency types. A HARD_BLOCKER relationship implies that if the source task fails verification, the target task must not even be instantiated, saving token costs and preventing cascading failures. This graph structure is essential for managing the complexity of multi-agent orchestration, mirroring the dependency resolution strategies found in modern build systems like Bazel or Turborepo.

### 2.2 The TaskCard Unit

The TaskCard is the atomic unit of work in this architecture. It is the packet of information delivered to an Executor Agent. A TaskCard must satisfy the "Single Verifiable Change" principle: it is not sufficient for a task to be small; it must be verifiable in isolation. If a task cannot be verified without subsequent tasks being completed, it is a malformed task under this standard.

#### 2.2.1 TaskCard Schema Definition

This schema acts as the "Contract" for the executor agent, enforcing strict boundaries on context and action space.

```json
{
  "task_id": "TC_UUID_v4",
  "parent_plan_id": "TP_UUID_v4",
  "type": "ATOMIC_BUILD",
  "metadata": {
    "complexity_score": 0.45,
    "estimated_token_load": 2400,
    "timeout_seconds": 300
  },
  "context_provisioning": {
    "read_access": [
      "src/types/auth.ts",
      "src/utils/validation.ts"
    ],
    "write_access": [
      "src/middleware/jwt.ts"
    ],
    "tool_whitelist": [
      "file_system_write",
      "terminal_execute_vitest",
      "terminal_execute_tsc"
    ],
    "context_budget_tokens": 4096
  },
  "invariants": {
    "pre_condition": "File src/middleware/jwt.ts does not exist OR is empty",
    "post_condition": "File src/middleware/jwt.ts exists and exports function 'verifyToken'",
    "existential_checks": [
      "src/types/auth.ts"
    ]
  },
  "instructions": {
    "primary_directive": "Implement the JWT verification middleware using the 'AuthPayload' interface.",
    "constraint_checklist":
  },
  "verification_strategy": {
    "tool": "vitest",
    "command": "npx vitest run src/middleware/jwt.ts --typecheck",
    "success_signal": {
      "type": "EXIT_CODE",
      "value": 0,
      "timeout_behavior": "FAIL"
    },
    "failure_signal": {
      "std_err_pattern": "ReferenceError|SyntaxError|TypeError",
      "retry_allowance": 2
    }
  },
  "output_contract": {
    "artifacts": ["src/middleware/jwt.ts"],
    "signature_hash": "REQUIRED"
  }
}
```

#### 2.2.2 Context Provisioning and Least Privilege

The context_provisioning section implements the "Least Privilege" principle for agents. Instead of giving the agent access to the entire repository (a "Flat Context"), we explicitly whitelist read_access (reference material) and write_access (mutable scope). This drastically reduces "Context Mud" by forcing the Breakdown Agent to curate the input token stream.

**The Write Access Constraint:** The write_access field is not just a hint; it is a permission boundary. The Executor Agent's file system tool must be wrapped in a middleware that checks every write operation against this list. If the agent attempts to modify a file not in write_access, the operation is rejected at the system level. This prevents the "Sprawl" anti-pattern where an agent, unable to fix a bug in the target file, attempts to modify distant utilities or configuration files to suppress the error.

#### 2.2.3 Invariants and Formal Verification

Borrowed from formal verification methods, the invariants section defines binary checks performed before (pre) and after (post) the agent's execution.

- **Pre-Condition:** "File src/middleware/jwt.ts does not exist." This ensures the agent is starting from a clean state. If the file exists (perhaps from a failed previous run), the system must reset the state before invoking the agent.
- **Existential Checks:** This prevents "Ghost Dependencies." If src/types/auth.ts does not exist (perhaps the previous task failed to generate it), this task fails immediately before consuming any LLM tokens. This saves cost and prevents the agent from hallucinating the content of the missing file.

#### 2.2.4 The Verification Strategy

This is the critical innovation of the TDS. Unlike human tasks where "test it" is sufficient, the TaskCard requires a precise shell command and a deterministic success signal. Note the use of vitest --typecheck—this allows for compilation-level verification even before runtime logic is fully implemented, providing a robust, fast feedback loop. The failure_signal definition allows the Breakdown Agent to differentiate between "Syntax Errors" (which the agent can likely fix) and "Logic Errors" (which might require replanning), enabling smarter retry strategies.

### 2.3 Interface Standardization and Interoperability

To ensure interoperability between the Breakdown Agent and various Executor implementations (e.g., GitHub Copilot Agent, custom CLI agents using LangChain), the TDS mandates that all TaskCards be serialized as strictly typed JSON files stored in a hidden .agent/tasks/ directory within the repository. This file-based interface allows for independent auditing of the build plan before execution.

**Table 1: TaskCard Field Constraints and Rationales**

| Field                 | Type    | Constraint  | Rationale                                                                                                                          |
| --------------------- | ------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| task_id               | UUID    | Immutable   | Unique references are required for dependency graphing and persistent logging.                                                     |
| write_access          | Array   | Max 5 items | Mechanical Sizing: If a task needs to touch >5 files, it is too complex for a single agent session and risks partial application.  |
| context_budget_tokens | Integer | < 12,000    | Context Economics: Keeping the token count low ensures the LLM's attention mechanism remains focused on the instructions.          |
| verification_command  | String  | Non-empty   | Determinism: A task without a mechanical verification method is considered malformed and rejected by the schema validator.         |
| retry_policy          | Object  | { max: 3 }  | Defines how many times the agent can self-correct upon verification failure before escalating to human intervention or replanning. |
| tool_whitelist        | Array   | Explicit    | Security: Prevents the agent from executing dangerous system commands (e.g., rm -rf /) by restricting the available toolset.       |

## 3. The Mechanical Decomposition Decision System (MDDS)

The MDDS is the deterministic logic engine used by the Breakdown Agent to slice a broad Feature Request into the rigid TaskCards defined above. It rejects semantic intuition (e.g., "This looks hard") in favor of count-based heuristics (e.g., "Import graph depth > 2"). This approach aligns with the industry trend of moving from deterministic code to probabilistic agents, but it inverts the relationship: we use deterministic decomposition to manage probabilistic execution.

### 3.1 The Decomposition Algorithm

The breakdown process follows a strict recursive loop until all leaf nodes in the task graph satisfy the Complexity Thresholds. This is not an art; it is a recursive function.

#### 3.1.1 Step 1: The Dependency Topology Map

Before creating any tasks, the Breakdown Agent must generate an Abstract Syntax Tree (AST) or file-dependency graph of the target area in the codebase.

- **Input:** "Update the User Profile schema."
- **Analysis:** The agent identifies schema.prisma, types.ts, userController.ts, and profileComponent.tsx.
- **Graphing:**
  - `schema.prisma` (Root Dependency)
  - `types.ts` (Depends on Schema)
  - `userController.ts` (Depends on Types)
  - `profileComponent.tsx` (Depends on Types, Controller)

This mapping is critical because it identifies the "Blast Radius" of the change. A change to schema.prisma is not just one file; it invalidates the integrity of three other files.

#### 3.1.2 Step 2: The Vertical Slice Heuristic

The MDDS prohibits "Horizontal Slicing" (e.g., Task 1: "Write all tests," Task 2: "Write all code"). This creates "Dependency Hell" where Task 1 fails because the code doesn't exist to test against, and Task 2 fails because the tests aren't updated to match the new code. Rule: Every TaskCard must be a "Vertical Slice" that leaves the system in a compilable, verifiable state.

**Correct Decomposition:**

- Task A: Update schema.prisma + Run Migration. Verify: prisma migrate status.
- Task B: Regenerate types.ts. Verify: tsc --noEmit.
- Task C: Update userController.ts to use new types. Verify: Unit Test.
- Task D: Update profileComponent.tsx. Verify: Component Test.

In this sequence, the system is green after every single task. If Task C fails, we know exactly where the breakage occurred, and the repository is still valid up to Task B.

### 3.2 Count-Based Sizing Constraints: The "Rule of 5"

To avoid "Context Mud", the MDDS enforces hard limits on the scope of a single TaskCard. These limits are derived from software complexity metrics like Cyclomatic Complexity and Halstead Complexity, adapted for the constraints of LLM context windows.

**Table 2: MDDS Complexity Thresholds**

| Metric                  | Threshold (Soft) | Threshold (Hard) | Action on Breach                                                                                                                     |
| ----------------------- | ---------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Write File Count        | 3 files          | 5 files          | Split: Separate logic from types, or split by architectural layer (e.g., Data Layer vs. Presentation Layer).                         |
| Read Context Token Est. | 4,000 tokens     | 12,000 tokens    | Prune: Remove unrelated reference files. If a single file >12k tokens, trigger a "Refactor" task first.                              |
| Public Exports Modified | 2 exports        | 5 exports        | Split: If modifying >5 API endpoints, split the task by endpoint grouping (e.g., "Auth Endpoints" vs "User Endpoints").              |
| Existing LOC in File    | 200 lines        | 500 lines        | Refactor: If a file is >500 LOC, the first task must be "Extract Module" to reduce the file size before logic changes are attempted. |
| Import Depth            | 2 levels         | 4 levels         | Isolate: If dependencies are too deep, mock the lower levels to reduce context loading.                                              |

Reasoning Behind the Thresholds:

- **Write File Count:** Limiting write access to 3-5 files prevents the agent from attempting sweeping cross-cutting changes. Research shows that as the number of modified files increases, the likelihood of an agent introducing a regression in an unmonitored file increases exponentially.
- **LOC Limits:** LLMs struggle with "Needle in a Haystack" retrieval in large files. If a file exceeds 500 lines, the probability of the agent hallucinating the location of the edit or overwriting the wrong function increases. The MDDS mandates a preparatory refactor task to reduce file size before logic changes are attempted.

### 3.3 The Decomposition Decision Tree (Logic Flow)

The Breakdown Agent must follow this decision tree for every requested feature:

1. Isolate Entry Point: Identify the primary file to be changed.
2. Calculate Complexity: Run cyclomatic_complexity and import_depth on the target.
3. Check Thresholds:
   - IF imports > 5 OR LOC > 500: TRIGGER REFACTOR SPLIT.
   - Create Task 1: "Abstract internal logic to helper.ts."
   - Create Task 2: "Implement feature in trimmed file."
4. IF dependency is a "Root" (e.g., Database Schema, Terraform State): TRIGGER SERIALIZATION.
   - The Schema change becomes a "Blocking Task." No other tasks can be scheduled in parallel until the Blocking Task passes its verification (e.g., successful migration).
5. Identify "Ghost" Dependencies:
   - Scan the proposed read_access list.
   - IF a file does not exist yet: TRIGGER DEPENDENCY ORDERING.

Ensure the task creating that file is strictly strictly antecedent in the Execution Graph.

**Anti-Pattern Check:** Does the task rely on a file implied to be created by a sibling task? If so, merge them or serialize them.

### 3.4 Handling "Ghost" Dependencies

A common anti-pattern in agentic coding is the "Ghost Dependency"—where code relies on a variable or file that will be created by another agent but doesn't exist yet. The MDDS strictly forbids this via the "Existential" Rule.

**The Existential Rule:** A TaskCard cannot reference a file or export in its read_access unless that artifact currently exists in the base_commit OR is the explicit output of a strictly preceding parent node in the TaskGraph.

This forces the Breakdown Agent to linearize tasks that might otherwise appear parallelizable. For example, you cannot write the Controller and the Service in parallel if the Controller imports the Service. You must write the Service Interface first, then you can parallelize the Controller (using the Interface) and the Service Implementation.

## 4. Deterministic Verification Strategies

The success of an agentic workflow hinges entirely on the quality of its verification. If the verification is "Ask the LLM if it looks good," the system is circular and prone to failure. The TDS mandates Deterministic Verification: utilizing external, non-AI compilers, linters, and runtime environments to generate objective truth signals.

### 4.1 The Verification Hierarchy of Truth

Verification methods are ranked by their deterministic reliability. The Breakdown Agent must always select the highest available rank for a TaskCard.

**Table 3: The Verification Hierarchy**

| Rank | Method               | Reliability | Example Tool                   | Use Case                                                        |
| ---- | -------------------- | ----------- | ------------------------------ | --------------------------------------------------------------- |
| 1    | Infrastructure State | Absolute    | terraform plan, prisma migrate | Confirming resource existence or DB schema state.               |
| 2    | Static Analysis      | Very High   | tsc --noEmit, eslint, mypy     | Verifying type safety, syntax validity, and import correctness. |
| 3    | Isolated Unit Test   | High        | vitest, jest (Mocked)          | Verifying logic of a single function with controlled inputs.    |
| 4    | Integration Test     | Medium      | cypress, playwright            | Verifying component interaction. Prone to flakiness.            |
| 5    | Heuristic Scan       | Low         | LLM Code Review                | PROHIBITED as primary verifier. Only for style/comments.        |

### 4.2 Handling Specific Tool Nuances

The MDDS includes a knowledge base of tool behaviors to prevent false positives. Many standard developer tools are designed for human consumption (informative output) rather than machine consumption (binary signal). We must coerce them into determinism.

#### 4.2.1 Infrastructure Verification (Terraform)

Standard terraform plan returns exit code 0 even if there are changes. This is insufficient for verifying that an agent successfully implemented a change.

**Standard:** Use `-detailed-exitcode`.

- Exit Code 0: No changes. (Failure: The agent did not do its job).
- Exit Code 1: Error. (Failure: The agent broke the configuration).
- Exit Code 2: Succeeded with Diff. (Success: The agent produced the desired change).

**Anti-Pattern:** Relying on cdktf without checking intermediate templates. Research indicates cdktf can mask drift detection. The TaskCard must explicitly command the agent to parse the exit code 2.

#### 4.2.2 Database Verification (Prisma/Atlas)

Prisma's CLI has a known issue where migrate status or connection failures might return exit code 0 or be ambiguous in older versions.

**Standard:** The TaskCard must inject a wrapper script.

```bash
# Wrapper for deterministic signal

npx prisma migrate status --exit-code
STATUS=$?
if; then
echo "Migration Verification Failed with Code $STATUS"
exit 1
fi
```

Atlas Integration: For complex logic, we leverage atlas migrate test. This allows the agent to write a "Pre-Migration Verification" step.

Task: "Write a migration to split names."

Verification: "Run atlas migrate test. Insert 'John Doe'. Assert database now contains 'John' and 'Doe'."

This effectively brings TDD (Test Driven Development) to Database Schemas, a critical requirement for autonomous agents modifying persistent state.

#### 4.2.3 Testing Verification (Jest/Vitest)

Snapshot testing is a dangerous anti-pattern in agentic coding. If an agent changes the UI and the snapshot fails, the agent's natural inclination is to "Update Snapshot" (-u), effectively validating its own visual regression.

**Standard:**

- Prohibit npm test (too broad).
- Mandate vitest run <specific_file> --typecheck.

**Constraint:** TaskCards involving UI logic must rely on component prop type verification or DOM query existence (getByRole) rather than visual snapshots. If a snapshot is required, the TaskCard must explicitly separate "Code Generation" from "Snapshot Approval" (which requires a Human-in-the-loop).

### 4.3 The "Golden Test" Strategy

For complex logic tasks, the Breakdown Agent must employ the "Golden Test" Strategy, reversing the typical development order.

- Task 1 (Test Agent): "Create math.test.ts. Assert add(2,2) === 4. Do NOT implement the add function."
- Output: A failing test file.
- Task 2 (Implementation Agent): "Implement math.ts to satisfy math.test.ts. You have READ access to math.test.ts and WRITE access to math.ts."
- Verification: Run math.test.ts.
- Why this works: It prevents the "Fox guarding the henhouse" scenario where a single agent writes a weak test to pass its own weak code. By separating the "Specifier" (Test Agent) from the "Implementer" (Coding Agent), we create an adversarial relationship that drives higher code quality.

## 5. File System and Context Boundaries

The physical organization of files acts as the ultimate guardrail for agentic context. The MDDS assumes and enforces a standard "fractal" architecture (e.g., Feature Folders) over layer-based architecture (Controller/Service/Dao).

### 5.1 Directory-Driven Context Scoping

In a traditional Layered Architecture: `src/controllers/`, `src/services/`, `src/models/`. Implementing a "User Feature" requires the agent to hold `src/controllers/user.ts`, `src/services/user.ts`, and `src/models/user.ts` in context. This spans the entire directory tree, polluting the context with unrelated controllers and services ("Context Mud").

In a Feature-Based Architecture: `src/features/user-profile/components/hooks/api/types.ts`. The Breakdown Agent can simply assign the directory `src/features/user-profile/` as the read_access root. This mechanically limits the "noise" tokens from other features.

**MDDS Rule:** If a repository is not structured by feature, the first set of TaskCards generated must be "Architectural Refactoring" to move related files into a cohesive directory. The agent cannot reliably execute complex logic until the file system supports isolated context.

### 5.2 The "Barrel File" Danger

Anti-Pattern: index.ts files (Barrel files) that export everything from a directory. Risk: If an agent reads src/utils/index.ts to find a single type, it might inadvertently load the token representation of the entire application structure linked through that barrel file. MDDS Rule: TaskCards must point to specific files (src/utils/date.ts), not barrel files (src/utils/index.ts). The schema validator should reject read_access paths that end in index.ts or index.js unless explicitly whitelisted.

## 6. Operational Protocols: Failure Modes and Recovery

Even with strict standards, agents will fail. The system must handle these failures deterministically to avoid infinite loops and cost overruns.

### 6.1 The "Hallucination Loop" Check

An agent may get stuck in a recursive failure loop: "Run Test -> Fail -> Attempt Fix -> Run Test -> Fail (Same Error)."

- **Mechanism:** The Execution Plan tracks the hash of the file content and the verification output after each attempt.
- **Rule:** If the file hash cycles (State A -> State B -> State A), the Breakdown Agent must intervene.
- **Recovery:** The Breakdown Agent issues a new TaskCard: "Revert to State A. Output a list of reasons why the previous fix attempt failed. Do not attempt to fix." This forces the agent to break its context cache and re-evaluate the problem.

### 6.2 Handling "Drift" (Scope Creep)

Agents often attempt to "clean up" code they see in the context window (e.g., fixing a typo in a comment in a file they shouldn't touch).

- **Mechanism:** git diff --name-only runs after every task.
- **Rule:** Compare the touched files against the write_access allowlist in the TaskCard.
- **Action:** If a non-whitelisted file is modified, the entire task result is rejected. The agent is not allowed to commit "bonus fixes." This enforces the discipline of the "Intent Lock".

### 6.3 The "Lying Agent" Defense

Agents often output "I have fixed the bug" or "Done" without actually running the code or when the output is hallucinated.

**Standard:** The Executor Agent is never believed. The System runs the verification_command independently.

If the Agent says "Success" but the command fails: Mark as Hallucination.

Feedback Loop: This failure is logged. If an agent model consistently hallucinates success on a specific type of task (e.g., Terraform plans), the MDDS updates its weighting to prefer a different model or prompt strategy for that task type.

## 7. Detailed Operational Scenarios

The following scenarios illustrate the application of the TDS and MDDS in real-world complex engineering situations.

### 7.1 Scenario A: The Database Schema Migration

User Query: "Add a 'bio' field to the User model."

MDDS Decomposition:

**Analysis:**

- Target: prisma/schema.prisma.
- Dependencies: src/types/generated.ts (Auto-generated), src/components/Profile.tsx.
- Complexity: Low logic, High risk (DB Migration).
- Constraint: Schema changes are blocking.

**TaskCard 1: Schema Mutation**

- type: SCHEMA_CHANGE
- write_access: [prisma/schema.prisma]
- instruction: "Add bio String? to User model. Do not run migration."
- verification: npx prisma validate (Check syntax only).

**TaskCard 2: Migration (Deterministic Checkpoint)**

- type: INFRA_MIGRATION
- write_access: [prisma/migrations/]
- instruction: "Run prisma migrate dev --name add_bio."
- verification: Wrapper script checking exit code of prisma migrate status.

Note: This task is a "Hard Blocker." If it fails, Task 3 is never instantiated.

**TaskCard 3: UI Implementation**

- type: FEATURE_IMPLEMENTATION
- read_access: [prisma/schema.prisma, src/components/Profile.tsx]
- write_access: [src/components/Profile.tsx]
- instruction: "Add Bio text area to Profile component. Bind to new 'bio' field."
- verification: vitest run src/components/Profile.test.tsx --typecheck (Ensures the new field is recognized by TS).

### 7.2 Scenario B: Refactoring a "God Object"

User Query: "Refactor the 2000-line utils.ts file."

MDDS Decomposition:

**Analysis:**

- utils.ts violates the 500 LOC Hard Threshold (Rule of 5).
- Direct editing is prohibited to prevent massive context loss.
- Strategy: "Strangler Fig" pattern.

**TaskCard 1: Static Analysis & Planning**

- type: ANALYSIS
- read_access: [utils.ts]
- write_access: [refactor_plan.json]
- instruction: "Analyze utils.ts. List all exported functions and their dependency groups. Output JSON grouping functions into DateUtils, StringUtils, ApiUtils."

**TaskCard 2: Extraction (Iterative - Group 1)**

- type: REFACTOR
- write_access: [src/utils/dateUtils.ts, src/utils.ts]
- instruction: "Move date functions to dateUtils.ts. Re-export them from utils.ts to maintain backward compatibility."
- verification: tsc && npm test (Must pass existing suite to ensure no regression).

**TaskCard 3...N:** Repeat for other groups.

**TaskCard Final:**

- type: CLEANUP
- write_access: [src/utils.ts]
- instruction: "Deprecate src/utils.ts exports."

### 7.3 Scenario C: The "Bug Fix" with Reproduction

User Query: "Fix the crash on the settings page."

MDDS Decomposition:

**Analysis:** The problem statement is semantic and vague. MDDS rejects direct implementation.

**TaskCard 1: Investigation & Reproduction**

- type: TEST_GENERATION
- read_access:
- write_access:
- instruction: "Create a test case that reproduces the crash described. The test MUST fail."
- verification: vitest run src/pages/Settings.repro.test.tsx. Success Condition: Exit Code 1 (Test Failure).

Note: This inverts the usual success signal. We want the test to fail to prove we found the bug.

**TaskCard 2: Fix Implementation**

- type: BUG_FIX
- read_access:
- write_access:
- instruction: "Modify code to pass the reproduction test case."
- verification: vitest run src/pages/Settings.repro.test.tsx. Success Condition: Exit Code 0 (Test Pass).

## 8. Conclusion: The Industrialization of Software Generation

The reliability of agentic coding is not a function of the LLM's "intelligence," but of the system's constraints. By treating the breakdown process as a mechanical engineering problem—governed by token budgets, file counts, and deterministic exit codes—we convert "probabilistic chaos" into "managed software assembly."

The Task Definition Standard (TDS) provides the immutable container for intent, ensuring that agents operate within a "Zero-Trust" environment where every action is bounded by rigid schema constraints. The Mechanical Decomposition Decision System (MDDS) replaces human intuition with count-based heuristics, ensuring that tasks are sized not by "feel," but by the mathematical probability of success within a context window.

This protocol represents the necessary maturation of agentic coding from a novelty to an industrial process. It acknowledges the limitations of current AI models—specifically their susceptibility to "Context Mud" and hallucination—and mitigates them through rigorous architectural standards. As agents evolve, the thresholds in the MDDS (e.g., token limits) may relax, but the fundamental architecture of Schema-Driven Decomposition and Deterministic Verification will remain the bedrock of reliable autonomous software development.

## References

- code.visualstudio.com — Using agents in Visual Studio Code. Opens in a new window.
- outshift.cisco.com — From deterministic code to probabilistic chaos: Securing AI agents that think for themselves. Opens in a new window.
- heyitworks.tech — Structuring AI Agent Tasks: A Repository Pattern for Systems ...
- arxiv.org
