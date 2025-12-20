# Events & Triggers
How events are structured, sent, and used to trigger functions and workflows.
Items: 25.

- [`inngest/function.cancelled` {{ className: "not-prose" }}](docs/157-inngest-function-cancelled-classname-not-prose.md) - Eventing: The `inngest/function.cancelled` event is sent whenever any single function is cancelled in your [Inngest environment](/docs/platform/environments).
- [`inngest/function.failed` {{ className: "not-prose" }}](docs/158-inngest-function-failed-classname-not-prose.md) - Eventing: The `inngest/function.failed` event is sent whenever any single function fails in your [Inngest environment](/docs/platform/environments).
- [Batching events](docs/056-batching-events.md) - Eventing: Handle high load by processing events in batches.
- [Cancel on Events](docs/028-cancel-on-events.md) - Eventing: Learn how to cancel long running functions with events.
- [Consuming webhook events](docs/113-consuming-webhook-events.md) - Eventing: At its core, Inngest is centered around functions that are triggered by events.
- [Creating an Event Key](docs/011-creating-an-event-key.md) - Eventing: "Event Keys" are unique keys that allow applications to send (aka publish) events to Inngest.
- [Event format and structure](docs/010-event-format-and-structure.md) - Eventing: Inngest events are just JSON allowing them to be easily created and read.
- [Event payload format](docs/025-event-payload-format.md) - Eventing: The event payload is a JSON object that must contain a `name` and `data` property.
- [Events & Triggers](docs/027-events-and-triggers.md) - Eventing: Inngest functions are triggered asynchronously by **events** coming from various sources, including.
- [Handling Clerk webhook events](docs/058-handling-clerk-webhook-events.md) - Eventing: Set up Clerk webhooks with Inngest and use Clerk events within Inngest functions.
- [Inspecting an Event](docs/105-inspecting-an-event.md) - Eventing: The Event details will provide all the information to understand how this event was received, which data it contained and the tools to reproduce it locally.
- [Integrate email events with Resend webhooks](docs/077-integrate-email-events-with-resend-webhooks.md) - Eventing: Set up Resend webhooks with Inngest and use Resend events within Inngest functions.
- [Multiple triggers & wildcards](docs/073-multiple-triggers-and-wildcards.md) - Eventing: Inngest functions can be configured to trigger on multiple events or schedules.
- [Neon](docs/026-neon.md) - Eventing: Inngest allows you to trigger functions from your Neon Postgres database updates.
- [Send Event](docs/124-send-event.md) - Eventing: Use to send event(s) reliably within your function.
- [Send event](docs/151-send-event.md) - Eventing: Note: This guide is for sending events from *inside* an Inngest function.
- [Send events](docs/115-send-events.md) - Eventing: Send events to Inngest.
- [Send events](docs/134-send-events.md) - Eventing: Note: This guide is for sending events from *outside* an Inngest function.
- [Sending events](docs/012-sending-events.md) - Eventing: Learn how to send events with the Inngest SDK, set the Event Key, and send events from other languages via HTTP.
- [Sending events from functions](docs/079-sending-events-from-functions.md) - Eventing: How to send events from within functions to trigger other functions to run in parallel.
- [Trigger your code from Retool](docs/083-trigger-your-code-from-retool.md) - Eventing: Internal tools are a pain to build and maintain.
- [Wait for an Event](docs/038-wait-for-an-event.md) - Eventing: One step method is available to pause a Function's run until a given event is sent.
- [Wait for event](docs/127-wait-for-event.md) - Eventing: The ID of the step.
- [Wait for event](docs/154-wait-for-event.md) - Eventing: Wait until the Inngest server receives a specific event.
- [Webhook intents: Building a webhook integration](docs/112-webhook-intents-building-a-webhook-integration.md) - Eventing: Build webhook integrations with any application using webhook intents.
