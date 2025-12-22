# IP Allow

> The "IP Allow" documentation for Neon outlines the process for configuring IP allowlists to manage access to Neon databases, detailing steps for adding, editing, and removing IP addresses to control database security.

## Source

- [IP Allow HTML](https://neon.com/docs/introduction/ip-allow): The original HTML version of this documentation

Neon's IP Allow feature, available with the Neon [Scale](introduction-plans.md) plan, ensures that only trusted IP addresses can connect to the project where your database resides, preventing unauthorized access and helping maintain overall data security. You can limit access to individual IP addresses, IP ranges, or IP addresses and ranges defined with [CIDR notation](reference-glossary.md#cidr-notation).

You can configure **IP Allow** in your Neon project's settings. To get started, see [Configure IP Allow](manage-projects.md#configure-ip-allow).



## IP Allow together with Protected Branches

You can apply IP restrictions more precisely by designating specific branches in your Neon project as protected and enabling the **Restrict IP access to protected branches only** option. This will apply your IP allowlist to protected branches only with no IP restrictions on other branches in your project. Typically, the protected branches feature is used with branches that contain production or sensitive data. For step-by-step instructions, refer to our [Protected Branches guide](guides-protected-branches.md).

   **Tip**: If you are an AWS user, Neon also supports a **Private Networking** feature, which enables connections to your Neon databases via AWS PrivateLink, bypassing the open internet entirely. See [Private Networking](guides-neon-private-networking.md).
