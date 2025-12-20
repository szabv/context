# Cloudflare Workers environment variables and context
Source: <https://www.inngest.com/docs/examples/middleware/cloudflare-workers-environment-variables>

Cloudflare Workers does not set environment variables a global object like Node.js does with `process.env`. Workers [binds environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/) to the worker's special `fetch` event handler thought a specific `env` argument.

This means accessing environment variables within Inngest function handlers isn't possible without explicitly passing them through from the worker event handler to the Inngest function handler.

We can accomplish this by use the [middleware](/docs/features/middleware) feature for Workers or when using [Hono](/docs/learn/serving-inngest-functions#framework-hono).

## Creating middleware

You can create middleware which extracts the `env` argument from the Workers `fetch` event handler arguments for either Workers or Hono:

1. Use `onFunctionRun`'s `reqArgs` array to get the `env` object and, optionally, cast a type.
2. Return the `env` object within the special `ctx` object of `transformInput` lifecycle method.

<CodeGroup>

```ts {{ title: "Workers" }}
new InngestMiddleware({
  name: 'Cloudflare Workers bindings',
  init({ client, fn }) {
    return {
      onFunctionRun({ ctx, fn, steps, reqArgs }) {
        return {
          transformInput({ ctx, fn, steps }) {
            // reqArgs is the array of arguments passed to the Worker's fetch event handler
            // ex. fetch(request, env, ctx)
            // We cast the argument to the global Env var that Wrangler generates:
            reqArgs[1] as Env;
            return {
              ctx: {
                // Return the env object to the function handler's input args
                env,
              },
            };
          },
        };
      },
    };
  },
});

// Include the middleware when creating the Inngest client
inngest = new Inngest({
  id: 'my-workers-app',
  middleware: [bindings],
});
```

```ts {{ title: "Hono" }}
type Bindings = {
  MY_VAR: string;
  DB_URL: string;
  MY_BUCKET: R2Bucket;
};

new InngestMiddleware({
  name: 'Hono bindings',
  init({ client, fn }) {
    return {
      onFunctionRun({ ctx, fn, steps, reqArgs }) {
        return {
          transformInput({ ctx, fn, steps }) {
            // reqArgs is the array of arguments passed to a Hono handler
            // We cast the argument to the correct Hono Context type with our
            // environment variable bindings
            reqArgs as [Context<{ Bindings: Bindings }>];
            return {
              ctx: {
                // Return the context's env object to the function handler's input args
                env: honoCtx.env,
              },
            };
          },
        };
      },
    };
  },
});

// Include the middleware when creating the Inngest client
inngest = new Inngest({
  id: 'my-hono-app',
  middleware: [bindings],
});
```

</CodeGroup>

Within your functions, you can now access the environment variables via the `env` object argument that you returned in `transformInput` above. Here's an example function:

```ts
inngest.createFunction(
  { id: 'my-fn' },
  { event: 'demo/event.sent' },
  // The "env" argument returned in transformInput is passed through:
  async ({ event, step, env }) => {

    // The env object will be typed as well:
    console.log(env.MY_VAR);
  }
);
```

