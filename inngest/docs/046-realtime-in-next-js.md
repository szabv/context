# Realtime in Next.js
Source: <https://www.inngest.com/docs/features/realtime/nextjs>
Description: How to use Realtime in your Next.js app.'

# Realtime in Next.js

Realtime provides a direct compatibility with Next.js API Routes's streaming capabilities.

A `stream` returned by the `subscribe()` helper can be used to create a HTTP stream response:

```tsx {{ filename: 

app/api/simple-search/route.ts" }}
export async function POST(req: Request) {
  await req.json();
  json;

  // Generate a unique ID for Inngest function run
  crypto.randomUUID();

  // The Inngest function will rely on this ID to publish messages
  // on a dedicated channel for this run.
  await inngest.send({
    name: "app/simple-search-agent.run",
    data: {
      uuid,
      input: prompt,
    },
  });

  // Subscribe to the Inngest function's channel.
  await subscribe({
    channel: `simple-search.${uuid}`,
    topics: ["updates"], // subscribe to one or more topics in the user channel
  });

  // Stream the response to the client with Vercel's streaming response.
  return new Response(stream.getEncodedStream(), {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      Connection: "keep-alive",
    },
  });
}
```

On the client, you can consume the stream using a simple `fetch()`:

```tsx {{ filename: "app/components/Chat.tsx" }}
"use client";
export function SimpleSearch() {
  useState<string[]>([]);
  useState("");

  async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!input.trim()) return;

    try {
      await fetch("/api/simple-search", {
        method: "POST",
        body: JSON.stringify({ prompt: input }),
      });

      response.body?.getReader();
      if (!reader) {
        return;
      }

      while (true) {
        await reader.read();
        if (done) {
          break;
        }
        new TextDecoder().decode(value);
        JSON.parse(text).data;
        if (data === "Search complete") {
          reader.cancel();
          break;
        } else {
          setUpdates((prev) => [...prev, data]);
        }
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setInput("");
    }
  };

  return (
    // ...
  );
}
```

<CardGroup cols={1}>

  <Card
    href={"https://github.com/inngest/inngest-js/tree/main/examples/realtime-demos#readme"}
    title={"See the complete example source code"}
    icon={<RiGithubFill className="text-basis h-8 w-8"/>}
    iconPlacement="top"
  >
     Explore our Next.js Realtime demo applications.
  </Card>

</CardGroup>

#
### How do I consume the stream on the client?
A stream return by a Vercel Function can be consumed by the client using the `fetch()` API.

From the `fetch()` response, you can get a `Reader` object, which you can use to read the stream's content using:
- a loop to read the stream's content chunk by chunk
- a `TextDecoder` to decode the stream's content into a string
- a `JSON.parse()` to parse the stream's content into a JSON object

```ts
await fetch("/api/simple-search", {
  method: "POST",
  body: JSON.stringify({ prompt: input }),
});

response.body?.getReader();
if (!reader) {
  return;
}

while (true) {
  await reader.read();
  if (done) {
      break;
  }
  new TextDecoder().decode(value);
  JSON.parse(text).data;
  if (data === "Search complete") {
      setIsLoading(false);
      setIsInputVisible(true);
      reader.cancel();
      break;
  } else {
      setUpdates((prev) => [...prev, data]);
  }
}
```

Depending on your use case, you might want to handle the stream's termination differently (see below for an example).

### How do I handle the termination of the stream?

By default, an Inngest Realtime stream will remain open until explicitly closed by the client.
For this reason, you should handle the stream's termination by publishing a specific message from your Inngest function and handling it in the client's stream reader.

```ts {{ filename: "app/inngest/functions/streaming-workflow.ts" }}
simpleSearchAgent = inngest.createFunction(
  {
    id: "simple-search-agent-workflow",
  },
  {
    event: "app/simple-search-agent.run",
  },
  async ({ step, event, publish }) => {
    event.data;

    // ...

    await publish({
      channel: `simple-search.${uuid}`,
      topic: "updates",
      data: "Search complete",
    });

    return {
      response,
    };
  }
);

```

```tsx {{ filename: "app/components/Chat.tsx" }}
"use client";
export function SimpleSearch() {
  useState<string[]>([]);
  useState("");

  async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!input.trim()) return;

    try {
      await fetch("/api/simple-search", {
        method: "POST",
        body: JSON.stringify({ prompt: input }),
      });

      response.body?.getReader();
      if (!reader) {
        return;
      }

      while (true) {
        await reader.read();
        if (done) {
          break;
        }
        new TextDecoder().decode(value);
        JSON.parse(text).data;
        if (data === "Search complete") {
          reader.cancel();
          break;
        } else {
          setUpdates((prev) => [...prev, data]);
        }
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setInput("");
    }
  };

  return (
    // ...
  );
}
```

### Is it compatible with Vercel's AI `useChat()`?

An Inngest Function publishing messages matching the `useChat()` hook's signature will be compatible with it.

See the [`Message`](https://sdk.vercel.ai/docs/reference/ai-sdk-ui/use-chat#messages) reference for the expected message format.

