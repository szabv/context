# Subscribing
Source: <https://www.inngest.com/docs/features/realtime/subscribe>
Description: Learn how to subscribe to data from Inngest functions.';

### Subscribing

To subscribe to data on the client (browser), you'll need to create a subscription token and use the `subscribe()` function which also requires `channel` and `topic` to be specified.

Your application uses the Inngest SDK to create a token, which is then used by the subscribe function to connect to the Inngest WebSocket server.


<Steps>
  <Step title=

Create a subscription token">
    Subscription tokens are required to securely establish a connection to the Inngest WebSocket server.

    Your application must create tokens on the server and pass them to the client. You can create a new endpoint to generate a token, ensuring that the user is authorized to subscribe to a given channel and topics.

    Here's an example of a server endpoint that creates a token, scoped to a user's channel and specific topics.

    <CodeGroup>
    ```ts {{ title: "Next.js - Server action" }}
    // ex. /app/actions/get-subscribe-token.ts
    "use server";

    // See the "Typed channels (recommended)" section above for more details:
    // this could be any auth provider

    export type UserChannelToken = Realtime.Token<typeof userChannel, ["ai"]>;

    export async function fetchRealtimeSubscriptionToken(): Promise<UserChannelToken> {
      await getSession();

      // This creates a token using the Inngest API that is bound to the channel and topic:
      await getSubscriptionToken(inngest, {
        channel: `user:${userId}`,
        topics: ["ai"],
      });

      return token;
    }
    ```

    ```ts {{ title: "Express" }}
    // this could be any auth provider

    app.post("/api/get-subscribe-token", async (req, res) => {
      getSession(req)

      // This creates a token using the Inngest API that is bound to the channel and topic:
      await getSubscriptionToken(inngest, {
        channel: `user:${userId}`,
        topics: ["ai"],
      })

      res.json({ token })
    })
    ```

    ```py {{ title: "Python - Fast API" }}
    @app.get("/api/get_subscription_token")
    async def get_realtime_token():
        user_id = session["user_id"]
    # - Authorize what the user is allowed to subscribe to
    # - Allow the client to specify what topics they want to subscribe to
    return await realtime.get_subscription_token(
        client=inngest_client,
        channel=f"user:{user_id}",
        topics=["messages"],
    )
    ```
    </CodeGroup>
  </Step>
  <Step title="Subscribe to a channel">
    Once you have a token, you can subscribe to a channel by calling the `subscribe` function with the token. You can also subscribe using the `useInngestSubscription` React hook. Read more about the [React hook here](/docs/features/realtime/react-hooks).

    <CodeGroup>

    ```ts {{ title: "React hook - useInngestSubscription()" }}
    // ex: ./app/page.tsx
    "use client";

    // ℹ️ Import the hook from the hooks sub-package:
    export default function Home() {
      // The hook automatically fetches the token from the server.
      // The server checks that the user is authorized to subscribe to
      // the channel and topic, then returns a token:
      useInngestSubscription({
        refreshToken: fetchRealtimeSubscriptionToken,
      });

      return (
        <div>
          {data.map((message, i) => (
            <div key={i}>{message.data}</div>
          ))}
        </div>
      );
    }
    ```

    ```ts {{ title: "Basic subscribe" }}
    // The server checks that the user is authorized to subscribe to
    // the channel and topic, then returns a token:
    await fetch("/api/get-subscribe-token", {
      method: "POST",
      credentials: "include",
    }).then(res => res.json());

    // The token is bound to the channel and topic, so we can
    // subscribe to the channel and topic:
    await subscribe(token);

    for await (const message of stream) {
      console.log(message)
    }
    ```

    </CodeGroup>

    {/* TODO - We need other docs for typing - it's complex and needs more examples with different
      frameworks and whatnot.

    <Info>
      Both Next.js Server Actions and `subscribe()` approaches offer a fully typed experience.

      The Next.js Server Action relies on the `Realtime.Token<>` type helper to get a typed token.

      The `subscribe()` approach uses the `typeOnlyChannel()` helper to get a typed channel.
    </Info>*/}

    That's all you need to do to subscribe to a channel from the client!
  </Step>
</Steps>

