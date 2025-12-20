# Realtime: Stream updates from Inngest functions
Source: <https://www.inngest.com/docs/examples/realtime>
Description: Stream updates and enable real-time workflows with Inngest functions.

Inngest Realtime enables you to stream updates from your functions, power live UIs, and implement bi-directional workflows such as Human-in-the-Loop. Use channels and topics to broadcast updates, stream logs, or await user input.

## Pattern: Stream updates from a single function run

Enable users to follow the progress of a long-running task by streaming updates from a dedicated channel. Here's how to trigger a function and subscribe to its updates:

```ts { title: "app/api/hello-world/route.ts" }
export async function POST(req: Request) {
  await req.json();
  json;
  crypto.randomUUID();

  await inngest.send({
    name: "hello-world/hello",
    data: { uuid },
  });

  await subscribe(inngest, {
    channel: `hello-world.${uuid}`,
    topics: ["logs"],
  });

  return new Response(stream.getEncodedStream(), {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      Connection: "keep-alive",
    },
  });
}
```

Your function can then publish updates to this channel:

```ts { title: "src/inngest/functions/hello-world.ts" }
new Inngest({
  id: "my-app",
  middleware: [realtimeMiddleware()],
});

helloChannel = channel((uuid: string) => `hello-world.${uuid}`).addTopic(
  topic("logs").type<string>()
);

someTask = inngest.createFunction(
  { id: "hello-world" },
  { event: "hello-world/hello" },
  async ({ event, step, publish }) => {
    event.data;
    await publish(helloChannel(uuid).logs("Hello, world!"));
  }
);
```

By creating a channel with a unique identifier, you can stream updates for a specific run to the end user.

<CardGroup cols={2}>

  <Card
    href="https://github.com/inngest/inngest-js/tree/main/examples/realtime/nodejs/realtime-single-run-subscription"
    title={"Explore the full source code"}
    icon={<RiNodejsFill className="text-basis h-8 w-8"/>}
    iconPlacement="top"
  >
   Clone this example locally to run it and explore the full source code.
  </Card>

</CardGroup>

## Pattern: Stream updates from multiple function runs

A Realtime channel can be used to stream updates from multiple function runs. Here, we'll define two channels: one global channel and one post-specific channel:

```ts {{ filename: "src/inngest/channels.ts" }}
import {
  channel,
  topic,
} from "@inngest/realtime";
globalChannel = channel("global").addTopic(topic("logs").type<string>());

postChannel = channel((postId: string) => `post:${postId}`)
  .addTopic(
    topic("updated").schema(
      z.object({
        id: z.string(),
        likes: z.number(),
      })
    )
  )
  .addTopic(
    topic("deleted").schema(
      z.object({
        id: z.string(),
        reason: z.string(),
      })
    )
  );
```

Our `likePost` function will publish updates to both channels:

```ts {{ filename: "src/inngest/functions/likePost.ts" }}
import {
  channel,
  realtimeMiddleware,
  subscribe,
  topic,
} from "@inngest/realtime";
likePost = app.createFunction(
  {
    id: "post/like",
    retries: 0,
  },
  {
    event: "app/post.like",
  },
  async ({
    event: {
      data: { postId = "123" },
    },
    step,
    publish,
  }) => {
    if (!postId) {
      await publish(
        globalChannel().logs("Missing postId when trying to like post")
      );
      throw new Error("Missing postId");
    }

    await publish(globalChannel().logs(`Liking post ${postId}`));

    // Fake a post update
    await step.run("Update likes", async () => {
      {
        id: "123",
        likes: Math.floor(Math.random() * 10000),
      };

      return publish(postChannel(fakePost.id).updated(fakePost));
    });

    return post;
  }
);
```

The `globalChannel` will be used to stream updates for all posts, and the `postChannel` will be used to stream updates for specific posts.

<CardGroup cols={2}>

  <Card
    href="https://github.com/inngest/inngest-js/tree/main/examples/realtime/nodejs/realtime-across-multiple-channels"
    title={"Explore the full source code"}
    icon={<RiNodejsFill className="text-basis h-8 w-8"/>}
    iconPlacement="top"
  >
   Clone this example locally to run it and explore the full source code.
  </Card>

</CardGroup>

## Human in the loop: Bi-directional workflows

Combine Realtime with `waitForEvent()` to enable workflows that require user input, such as review or approval steps. Here's how to send a message to the user and wait for their confirmation:

```ts { title: "src/inngest/functions/agentic-workflow.ts" }
new Inngest({
  id: "my-app",
  middleware: [realtimeMiddleware()],
});

agenticWorkflowChannel = channel("agentic-workflow").addTopic(
  topic("messages").schema(
    z.object({
      message: z.string(),
      confirmationUUid: z.string(),
    })
  )
);

agenticWorkflow = inngest.createFunction(
  { id: "agentic-workflow" },
  { event: "agentic-workflow/start" },
  async ({ event, step, publish }) => {
    await step.run(/* ... */);
    await step.run("get-confirmation-uuid", async () => crypto.randomUUID());
    await publish(agenticWorkflowChannel().messages({
      message: "Confirm to proceed?",
      confirmationUUid,
    }));
    await step.waitForEvent("wait-for-confirmation", {
      event: "agentic-workflow/confirmation",
      timeout: "15m",
      if: `async.data.confirmationUUid == \"${confirmationUUid}\"`,
    });
    if (confirmation) {
      // continue workflow
    }
  }
);
```

The `confirmationUUid` links the published message to the reply event, ensuring the correct user response is handled.

<CardGroup cols={2}>

  <Card
    href="https://github.com/inngest/inngest-js/tree/main/examples/realtime/nodejs/realtime-human-in-the-loop"
    title={"Explore the full source code"}
    icon={<RiNodejsFill className="text-basis h-8 w-8"/>}
    iconPlacement="top"
  >
   Clone this example locally to run it and explore the full source code.
  </Card>

</CardGroup>

## Learn more

<ResourceGrid cols={2}>

<Resource resource={{
  href: "/docs/features/realtime",
  name: "Realtime documentation",
  description: "Learn more about streaming updates and real-time workflows with Inngest.",
  pattern: 1,
}}/>

<Resource resource={{
  href: "/docs/features/realtime/react-hooks",
  name: "Using Realtime with Next.js",
  description: "Learn how to use Realtime with Next.js.",
  pattern: 2,
}}/>

</ResourceGrid>

