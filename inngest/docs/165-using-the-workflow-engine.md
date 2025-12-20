# Using the workflow engine
Source: <https://www.inngest.com/docs/reference/workflow-kit/engine>

The workflow `Engine` is used to run a given [workflow instance](/docs/reference/workflow-kit/workflow-instance) within an Inngest Function:

```tsx {{ title: "src/inngest/workflow.ts" }}
new Engine({
  actions: actionsWithHandlers,
  loader: (event) => {
    return loadWorkflowInstanceFromEvent(event);
  },
});

export default inngest.createFunction(
  { id: "blog-post-workflow" },
  { event: "blog-post.updated" },
  async ({ event, step }) => {
    // When `run` is called,
    //  the loader function is called with access to the event
    await workflowEngine.run({ event, step });
  }
);

```

## Configure

<Properties>
  <Property name="actions" type="EngineAction[]">
    See [the `EngineAction[]` reference](/docs/reference/workflow-kit/actions#passing-actions-to-the-workflow-engine-engine-action).
  </Property>
  <Property name="loader" type="function">
    An async function receiving the [`event`](/docs/reference/functions/create#event) as unique argument and returning a valid [`Workflow` instance](/docs/reference/workflow-kit/workflow-instance) object.
  </Property>
  <Property name="disableBuiltinActions" type="boolean">
    For selectively adding built-in actions, set this to true and expose the actions you want via the [`<Provider>`](/docs/reference/workflow-kit/components-api) `availableActions` prop.
  </Property>
</Properties>

