# Customer Service AI Workflow Cookbook
Source: <https://www.inngest.com/docs/examples/customer-service-ai-workflow-cookbook>
Description: Patterns for building a two-step AI customer service workflow in TypeScript.

This cookbook shows a simple, two-step workflow:

1. Analyze sentiment and summarize the chat history.
2. Draft a reply based on sentiment and summary.

The reply string is returned from the workflow.

This example uses Gemini 3 Flash (preview) from Google AI Studio:

- Model code: `gemini-3-flash-preview`
- API key env var: `GEMINI_API_KEY`
- Node SDK: `@google/genai` (`GoogleGenAI`)
- REST endpoint: `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent`

## Event shape

```ts
type SupportChatMessage = {
  role: "user" | "assistant" | "system";
  content: string;
};

type SupportChatEvent = {
  name: "support/chat.received";
  data: {
    conversationId: string;
    messages: SupportChatMessage[];
  };
};
```

## Supporting files

```ts {{ filename: "inngest/examples/customer-service-ai/client.ts" }}
import { EventSchemas, Inngest } from "inngest";

import type { SupportChatMessage } from "./shared.js";

type SupportChatReceived = {
  data: {
    conversationId: string;
    messages: SupportChatMessage[];
  };
};

type Events = {
  "support/chat.received": SupportChatReceived;
};

export const inngest = new Inngest({
  id: "customer-support-workflows",
  schemas: new EventSchemas().fromRecord<Events>(),
});
```

```ts {{ filename: "inngest/examples/customer-service-ai/shared.ts" }}
export type SupportChatMessage = {
  role: "user" | "assistant" | "system";
  content: string;
};

export type SentimentAnalysis = {
  sentiment: "annoyed" | "not_annoyed";
  summary: string;
};

export const formatChatHistory = (messages: SupportChatMessage[]): string =>
  messages
    .map((message) => `${message.role.toUpperCase()}: ${message.content}`)
    .join("\n");

export const safeJsonParse = <T>(value: string, fallback: T): T => {
  try {
    return JSON.parse(value) as T;
  } catch {
    return fallback;
  }
};
```

## Pattern 1: Offload inference with `step.ai.infer`

Use this when you want Inngest to manage the Gemini inference call and pause execution while the model runs.

```ts {{ filename: "inngest/examples/customer-service-ai/workflows/customer-service-infer.ts" }}
import type { GetEvents, GetStepTools } from "inngest";

import { inngest } from "../client.js";
import { formatChatHistory, safeJsonParse } from "../shared.js";
import type { SentimentAnalysis } from "../shared.js";

type GeminiResponse = {
  candidates?: Array<{
    content?: {
      parts?: unknown[];
    };
  }>;
};

type SupportEvents = GetEvents<typeof inngest>;
type SupportStepTools = GetStepTools<typeof inngest, "support/chat.received">;

const geminiModel = "gemini-3-flash-preview";
const sentimentInstruction =
  "You are a support analyst. Return JSON with keys " +
  '"sentiment" and "summary". "sentiment" must be "annoyed" ' +
  'or "not_annoyed". "summary" should be 1-2 sentences.';
const replyInstruction =
  "You are a customer support agent. Use the summary and sentiment " +
  "to craft a concise reply. If sentiment is annoyed, apologize and " +
  "name the problem the customer thinks they're facing based on the summary. " +
  "If not annoyed, thank them for contacting support. Keep it under 5 sentences.";
const sentimentSchema = {
  type: "object",
  properties: {
    sentiment: {
      type: "string",
      enum: ["annoyed", "not_annoyed"],
    },
    summary: {
      type: "string",
    },
  },
  required: ["sentiment", "summary"],
};

const fallbackAnalysis: SentimentAnalysis = {
  sentiment: "not_annoyed",
  summary: "Summary unavailable.",
};

const isTextPart = (
  part: unknown,
): part is { text: string; thought?: boolean } => {
  if (typeof part !== "object" || part === null) {
    return false;
  }

  const record = part as { text?: unknown };
  return typeof record.text === "string";
};

const getGeminiText = (response: GeminiResponse): string => {
  const parts = response.candidates?.[0]?.content?.parts ?? [];
  for (const part of parts) {
    if (isTextPart(part) && !part.thought) {
      return part.text;
    }
  }

  for (const part of parts) {
    if (isTextPart(part)) {
      return part.text;
    }
  }

  return "";
};

export const customerServiceResponseInfer = inngest.createFunction(
  { id: "customer-service-response-infer" },
  { event: "support/chat.received" },
  async ({
    event,
    step,
  }: {
    event: SupportEvents["support/chat.received"];
    step: SupportStepTools;
  }) => {
    const chatHistory = formatChatHistory(event.data.messages);

    const analysisResponse = await step.ai.infer("analyze-sentiment-summary", {
      model: step.ai.models.gemini({ model: geminiModel }),
      body: {
        systemInstruction: {
          parts: [{ text: sentimentInstruction }],
        },
        contents: [
          {
            role: "user",
            parts: [{ text: `Chat history:\n${chatHistory}` }],
          },
        ],
        generationConfig: {
          responseMimeType: "application/json",
          responseSchema: sentimentSchema,
        },
      },
    });

    const analysisContent = getGeminiText(analysisResponse);
    const analysis = safeJsonParse<SentimentAnalysis>(
      analysisContent,
      fallbackAnalysis,
    );
    const sentiment = analysis.sentiment === "annoyed" ? "annoyed" : "not_annoyed";
    const summary = analysis.summary || fallbackAnalysis.summary;

    const replyResponse = await step.ai.infer("craft-support-reply", {
      model: step.ai.models.gemini({ model: geminiModel }),
      body: {
        systemInstruction: {
          parts: [{ text: replyInstruction }],
        },
        contents: [
          {
            role: "user",
            parts: [{ text: `Sentiment: ${sentiment}\nSummary: ${summary}` }],
          },
        ],
      },
    });

    const reply = getGeminiText(replyResponse).trim();
    return reply || "Thanks for contacting support. We'll follow up shortly.";
  },
);
```

## Pattern 2: Wrap an existing AI SDK with `step.ai.wrap`

Use this when you already call the Google GenAI SDK and want observability without changing your SDK call shape.

```ts {{ filename: "inngest/examples/customer-service-ai/workflows/customer-service-wrap.ts" }}
import { GoogleGenAI } from "@google/genai";
import type { GetEvents, GetStepTools } from "inngest";

import { inngest } from "../client.js";
import { formatChatHistory, safeJsonParse } from "../shared.js";
import type { SentimentAnalysis } from "../shared.js";

type SupportEvents = GetEvents<typeof inngest>;
type SupportStepTools = GetStepTools<typeof inngest, "support/chat.received">;

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const generateContent = ai.models.generateContent.bind(ai.models);

const geminiModel = "gemini-3-flash-preview";
const sentimentInstruction =
  "You are a support analyst. Return JSON with keys " +
  '"sentiment" and "summary". "sentiment" must be "annoyed" ' +
  'or "not_annoyed". "summary" should be 1-2 sentences.';
const replyInstruction =
  "You are a customer support agent. Use the summary and sentiment " +
  "to craft a concise reply. If sentiment is annoyed, apologize and " +
  "name the problem the customer thinks they're facing based on the summary. " +
  "If not annoyed, thank them for contacting support. Keep it under 5 sentences.";
const sentimentSchema = {
  type: "object",
  properties: {
    sentiment: {
      type: "string",
      enum: ["annoyed", "not_annoyed"],
    },
    summary: {
      type: "string",
    },
  },
  required: ["sentiment", "summary"],
};

const fallbackAnalysis: SentimentAnalysis = {
  sentiment: "not_annoyed",
  summary: "Summary unavailable.",
};

export const customerServiceResponseWrap = inngest.createFunction(
  { id: "customer-service-response-wrap" },
  { event: "support/chat.received" },
  async ({
    event,
    step,
  }: {
    event: SupportEvents["support/chat.received"];
    step: SupportStepTools;
  }) => {
    const chatHistory = formatChatHistory(event.data.messages);

    const analysisResponse = await step.ai.wrap(
      "analyze-sentiment-summary",
      generateContent,
      {
        model: geminiModel,
        contents: `Chat history:\n${chatHistory}`,
        config: {
          systemInstruction: sentimentInstruction,
          responseMimeType: "application/json",
          responseSchema: sentimentSchema,
        },
      },
    );

    const analysisContent = analysisResponse.text ?? "";
    const analysis = safeJsonParse<SentimentAnalysis>(
      analysisContent,
      fallbackAnalysis,
    );
    const sentiment = analysis.sentiment === "annoyed" ? "annoyed" : "not_annoyed";
    const summary = analysis.summary || fallbackAnalysis.summary;

    const replyResponse = await step.ai.wrap(
      "craft-support-reply",
      generateContent,
      {
        model: geminiModel,
        contents: `Sentiment: ${sentiment}\nSummary: ${summary}`,
        config: {
          systemInstruction: replyInstruction,
        },
      },
    );

    const reply = replyResponse.text?.trim() ?? "";
    return reply || "Thanks for contacting support. We'll follow up shortly.";
  },
);
```

## Prompt contract

- Step 1 returns JSON with `sentiment: "annoyed" | "not_annoyed"` and `summary`.
- Step 2 uses those fields to decide whether to apologize or thank the user.
- The final reply string is the workflow return value.

## Related concepts

- [AI Inference](/docs/features/inngest-functions/steps-workflows/step-ai-orchestration)
- [Inngest Steps](/docs/learn/inngest-steps)
