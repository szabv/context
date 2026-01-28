# Langfuse + Vercel AI SDK Integration Guide

## Overview

This guide covers integrating Langfuse observability with the Vercel AI SDK using OpenTelemetry. The key challenges are:

1. **Session correlation** - Grouping multiple messages in a conversation
2. **Trace input/output** - Displaying user messages and AI responses in Langfuse dashboard
3. **Context propagation** - Ensuring child spans inherit session/user metadata

## Prerequisites

```bash
pnpm add @langfuse/tracing @langfuse/otel @opentelemetry/api @opentelemetry/sdk-trace-node
```

Environment variables:
```env
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

## Architecture

```
observe() creates root span
├── propagateAttributes() adds sessionId/userId to context
│   └── streamText() creates child spans (ai.streamText, ai.toolCall, etc.)
│       └── Tool executions create nested spans
└── onFinish() sets output on root span
```

## Implementation

### 1. Instrumentation Setup (`instrumentation.ts`)

```typescript
import type { LangfuseSpanProcessor } from "@langfuse/otel";

declare global {
  var langfuseSpanProcessor: LangfuseSpanProcessor | undefined;
}

export async function flushLangfuseTraces(): Promise<void> {
  if (globalThis.langfuseSpanProcessor) {
    await globalThis.langfuseSpanProcessor.forceFlush();
  }
}

export async function register() {
  if (process.env.NEXT_RUNTIME !== "nodejs") {
    return;
  }

  const { NodeTracerProvider } = await import("@opentelemetry/sdk-trace-node");
  const { LangfuseSpanProcessor } = await import("@langfuse/otel");

  globalThis.langfuseSpanProcessor = new LangfuseSpanProcessor({
    publicKey: process.env.LANGFUSE_PUBLIC_KEY,
    secretKey: process.env.LANGFUSE_SECRET_KEY,
    baseUrl: process.env.LANGFUSE_BASE_URL,
  });

  const tracerProvider = new NodeTracerProvider({
    spanProcessors: [globalThis.langfuseSpanProcessor],
  });

  tracerProvider.register();
}
```

### 2. API Route Handler (`app/api/chat/route.ts`)

```typescript
import { observe, propagateAttributes } from "@langfuse/tracing";
import { trace } from "@opentelemetry/api";
import { streamText } from "ai";
import { after } from "next/server";
import { flushLangfuseTraces } from "@/instrumentation";

const handler = async (request: Request) => {
  const { id, messages } = await request.json();
  const session = await auth();

  // Get the last user message for trace input
  const lastUserMessage = messages.filter((m) => m.role === "user").pop();
  const inputContent = lastUserMessage?.content ?? messages[messages.length - 1]?.content;

  // CRITICAL: Capture the ROOT span here - we reuse it for both input AND output
  // onFinish runs in a different span context (ai.streamText), so we must capture it now
  const rootSpan = trace.getActiveSpan();

  // Set input on the root span
  if (rootSpan) {
    const serializedInput = JSON.stringify(inputContent);
    rootSpan.setAttribute("langfuse.trace.input", serializedInput);
    rootSpan.setAttribute("langfuse.observation.input", serializedInput);
  }

  // propagateAttributes ensures sessionId/userId flow to ALL child spans
  return await propagateAttributes(
    {
      sessionId: id,           // Groups conversation turns
      userId: session.user?.id,
      traceName: "chat-message",
      metadata: { messageCount: String(messages.length) },
    },
    async () => {
      const result = await streamText({
        model: yourModel,
        messages: coreMessages,
        tools: { /* ... */ },
        onFinish: async ({ responseMessages }) => {
          // Set output on the SAME root span (not trace.getActiveSpan() which is different here!)
          const lastAssistantMessage = responseMessages
            .filter((m) => m.role === "assistant")
            .pop();
          if (lastAssistantMessage && rootSpan) {
            const serializedOutput = JSON.stringify(lastAssistantMessage.content);
            rootSpan.setAttribute("langfuse.trace.output", serializedOutput);
            rootSpan.setAttribute("langfuse.observation.output", serializedOutput);
          }

          // End the root span after streaming
          rootSpan?.end();
        },
        experimental_telemetry: {
          isEnabled: true,
          functionId: "stream-text",
        },
      });

      // Flush traces after response
      after(async () => {
        await flushLangfuseTraces();
      });

      return result.toDataStreamResponse({});
    },
  );
};

export const POST = observe(handler, {
  name: "handle-chat-message",
  endOnExit: false,        // We end the span manually in onFinish
  captureInput: false,     // We set input manually (Request object isn't useful)
  captureOutput: false,    // We set output manually
});
```

## Critical Gotchas

### 1. Root Span vs Active Span

The `onFinish` callback runs inside the `ai.streamText` span context, NOT the root span. If you call `trace.getActiveSpan()` in `onFinish`, you get the wrong span.

```typescript
// WRONG - input and output end up on different spans
const handler = async () => {
  trace.getActiveSpan()?.setAttribute("input", ...);  // Root span

  await streamText({
    onFinish: () => {
      trace.getActiveSpan()?.setAttribute("output", ...);  // ai.streamText span!
    }
  });
};

// CORRECT - capture root span and reuse it
const handler = async () => {
  const rootSpan = trace.getActiveSpan();  // Capture once
  rootSpan?.setAttribute("input", ...);

  await streamText({
    onFinish: () => {
      rootSpan?.setAttribute("output", ...);  // Same span
    }
  });
};
```

### 2. Trace Input/Output Mapping

Langfuse copies trace-level input/output from the **root observation**. You must set BOTH:
- `langfuse.trace.input` / `langfuse.trace.output` (trace level)
- `langfuse.observation.input` / `langfuse.observation.output` (observation level)

### 3. observe() Auto-Capture

By default, `observe()` captures function arguments as input (the `Request` object). Disable this:

```typescript
export const POST = observe(handler, {
  captureInput: false,   // Don't capture Request object
  captureOutput: false,  // Don't capture Response object
});
```

### 4. Session Grouping

Use `propagateAttributes()` to set `sessionId` - this groups all messages in a conversation together in Langfuse's Sessions view.

```typescript
propagateAttributes({
  sessionId: chatId,      // Same ID for all messages in a chat
  userId: user.id,        // For user-level analytics
}, async () => {
  // All child spans inherit these attributes
});
```

## Verification Checklist

1. **Console logs show same span ID** for input and output:
   ```
   Set input on span: abc123
   Set output on span: abc123  ← Must match!
   ```

2. **Langfuse dashboard shows**:
   - Input column: User's message
   - Output column: Assistant's response
   - Sessions view: Messages grouped by chat ID

3. **Child spans have sessionId/userId**:
   - Click on `ai.streamText` or `ai.toolCall` spans
   - Verify they have `sessionId` and `userId` attributes

## References

- [Langfuse FAQ: Empty Trace Input/Output](https://langfuse.com/faq/all/empty-trace-input-and-output)
- [Langfuse OpenTelemetry Integration](https://langfuse.com/integrations/native/opentelemetry)
- [Vercel AI SDK Telemetry](https://sdk.vercel.ai/docs/ai-sdk-core/telemetry)
