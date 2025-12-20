# Deployment, Apps & Environments
Deploy targets, app sync, environment setup, and production configuration.
Items: 21.

- [Apps](docs/101-apps.md) - Deployment: Inngest enables you to manage your Inngest Functions deployments via [Inngest Environments and Apps](/docs/apps).
- [Checkpointing](docs/174-checkpointing.md) - Deployment: Checkpointing is currently in developer preview.
- [Cloudflare Pages](docs/004-cloudflare-pages.md) - Deployment: Inngest allows you to deploy your event-driven functions to [Cloudflare Pages](https://pages.cloudflare.com/).
- [Cloudflare Workers environment variables and context](docs/019-cloudflare-workers-environment-variables-and-context.md) - Deployment: Cloudflare Workers does not set environment variables a global object like Node.js does with `process.env`.
- [Connect](docs/175-connect.md) - Deployment: These docs are part of a developer preview for Inngest's `connect` API.
- [Creating an Event Key](docs/011-creating-an-event-key.md) - Deployment: "Event Keys" are unique keys that allow applications to send (aka publish) events to Inngest.
- [Deployment](docs/098-deployment.md) - Deployment: Moving to production requires deploying your Inngest Functions on your favorite Cloud Provider and configuring it to allow the Inngest Platform to orchestrate runs.
- [DigitalOcean](docs/005-digitalocean.md) - Deployment: Inngest functions can be deployed to DigitalOcean's Functions, App Platform, or Droplets.
- [Environment variables](docs/145-environment-variables.md) - Deployment: You can use environment variables to control some configuration.
- [Environment Variables](docs/169-environment-variables.md) - Deployment: You can set environment variables to change various parts of Inngest's configuration.
- [Environments](docs/099-environments.md) - Deployment: Inngest accounts all have multiple environments that help support your entire software development lifecycle.
- [Inngest Apps](docs/003-inngest-apps.md) - Deployment: In Inngest, apps map directly to your projects or services.
- [Inngest Dev Server](docs/009-inngest-dev-server.md) - Deployment: The Inngest dev server is an [open source](https://github.com/inngest/inngest) environment that.
- [Netlify](docs/006-netlify.md) - Deployment: We provide a Netlify build plugin, [netlify-plugin-inngest](https://www.npmjs.com/package/netlify-plugin-inngest), that allows you to automatically sync any found apps whenever your site is deployed to Netlify.
- [Render](docs/007-render.md) - Deployment: [Render](https://render.com) lets you easily deploy and scale full stack applications.
- [Self-hosting](docs/173-self-hosting.md) - Deployment: Learn how to self-host Inngest.
- [Serve](docs/156-serve.md) - Deployment: The `serve()` API handler is used to serve your application's [functions](/docs/reference/functions/create) via HTTP.
- [Setting up your Inngest app](docs/095-setting-up-your-inngest-app.md) - Deployment: With Inngest, you define functions or workflows using the SDK and deploy them to whatever platform or cloud provider you want including including serverless and container runtimes.
- [Signing keys](docs/111-signing-keys.md) - Deployment: Learn about how signing keys are used to secure communication between Inngest and your servers, how to rotate them, and how to set them in your SDK.
- [Syncing an Inngest App](docs/002-syncing-an-inngest-app.md) - Deployment: Learn how to sync Inngest Apps after a deploy.
- [Vercel](docs/008-vercel.md) - Deployment: Inngest enables you to host your functions on Vercel using their [serverless functions platform](https://vercel.com/docs/concepts/functions/serverless-functions).
