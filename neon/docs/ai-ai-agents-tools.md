# AI tools for Agents

> The document "Ship faster with AI tools" outlines how Neon users can leverage AI agents and tools to accelerate development processes and improve efficiency within the Neon database environment.

## Source

- [AI tools for Agents HTML](https://neon.com/docs/ai/ai-agents-tools): The original HTML version of this documentation

Neon provides several ways to integrate with AI tools and agents, from natural language database control to autonomous agent frameworks. Choose the tools that fit your workflow.

## MCP integration

The Model Context Protocol (MCP) is a standardized way for AI tools to interact with Neon databases using natural language, providing secure and contextual access to your data and infrastructure.

- [Neon MCP Server](ai-neon-mcp-server.md): Learn about managing your Neon projects using natural language with Neon MCP Server
- [Connect MCP clients](ai-connect-mcp-clients-to-neon.md): Learn how to connect MCP clients like Cursor, Claude Code, and ChatGPT to your Neon database

## Claude Code plugin

If you're using Claude Code, install the Neon plugin to get Skills, MCP integration, and all the context rules in one package.

- [Claude Code plugin for Neon](ai-ai-claude-code-plugin.md): Includes Claude Code Skills for Neon, Neon MCP integration, and context rules

## AI rules

For other AI tools like Cursor, use these individual `.mdc` context rule files. Copy them to your AI tool's custom rules directory — the format is tool-agnostic and works with any AI assistant that supports context rules.

- [Neon Auth](ai-ai-rules-neon-auth.md): AI rules for implementing authentication with Neon
- [Neon Drizzle](ai-ai-rules-neon-drizzle.md): AI rules for using Drizzle ORM with Neon
- [Neon Serverless Driver](ai-ai-rules-neon-serverless.md): AI rules for serverless database connections
- [Neon TypeScript SDK](ai-ai-rules-neon-typescript-sdk.md): AI rules for using the Neon TypeScript SDK
- [Neon Python SDK](ai-ai-rules-neon-python-sdk.md): AI rules for using the Neon Python SDK
- [Neon API](ai-ai-rules-neon-api.md): AI rules for using the Neon API
- [Neon Toolkit](ai-ai-rules-neon-toolkit.md): AI rules for using the Neon Toolkit

## Build AI agents

Create autonomous agents that can manage and interact with your Neon databases programmatically. Build with our terse JavaScript client or the Neon API.

- [Neon for AI agent platforms](use-cases-ai-agents.md): Read about Neon as a solution for agents that need backends.
- [@neondatabase/toolkit](https://github.com/neondatabase/toolkit): A terse JavaScript client for spinning up Postgres databases and running SQL queries
- [Database versioning](ai-ai-database-versioning.md): How AI agents and codegen platforms use Neon snapshot APIs for database versioning
- [Neon API](reference-api-reference.md): Integrate using the Neon API

## Agent frameworks

Build AI agents using popular frameworks that integrate with Neon.

- [AgentStack Integration](https://neon.com/guides/agentstack-neon): Build and deploy AI agents with AgentStack's CLI and Neon integration
- [AutoGen Integration](https://neon.com/guides/autogen-neon): Create collaborative AI agents with Microsoft AutoGen and Neon
- [Azure AI Agent Service](https://neon.com/guides/azure-ai-agent-service): Build enterprise AI agents with Azure AI Agent Service and Neon
- [Composio + CrewAI](https://neon.com/guides/composio-crewai-neon): Create multi-agent systems with CrewAI and Neon
- [LangGraph Integration](https://neon.com/guides/langgraph-neon): Build stateful, multi-actor applications with LangGraph and Neon
