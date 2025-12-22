# Connect to Neon

> The "Connect to Neon" documentation outlines the steps and requirements for establishing a connection to a Neon database, detailing supported connection methods and necessary configurations for users.

## Source

- [Connect to Neon HTML](https://neon.com/docs/connect/connect-intro): The original HTML version of this documentation

Find detailed information and instructions about connecting to Neon from different clients and applications, troubleshooting connection issues, connection pooling, and more.

For integrating Neon with different frameworks, languages, and platforms, refer to our [Guides](https://neon.com/docs/guides/guides-intro) documentation.

## Choose a connection type

To help understand which driver and connection type you need, see:

- [Choose a driver and connection type](connect-choose-connection.md): How to select the right driver and connection type for your application

## Connect from clients and applications

Learn how to establish a connection to Neon from any application.

- [Connect from any app](connect-connect-from-any-app.md): Learn about connection strings and how to connect to Neon from any application
- [Connect locally](local-neon-local-connect.md): Connect to any Neon branch using a localhost connection string in VS Code, Cursor, or Windsurf
- [Neon serverless driver](serverless-serverless-driver.md): Connect to Neon from serverless environments over HTTP or WebSockets
- [Connect a GUI application](connect-connect-postgres-gui.md): Learn how to connect to a Neon database from a GUI application
- [Connect with psql](connect-query-with-psql-editor.md): Connect with psql, the native command-line client for Postgres
- [Passwordless auth](connect-passwordless-connect.md): Connect without a password using Neon's psql passwordless auth feature

## Connect from frameworks and languages

Learn how to connect to Neon from different frameworks and languages.

- [Connect from various frameworks](get-started-frameworks.md): Find detailed instructions for connecting to Neon from frameworks
- [Connect from various languages](get-started-languages.md): Find detailed instructions for connecting to Neon from languages

## Troubleshoot connection issues

Troubleshoot and resolve common connection issues.

- [Connection errors](connect-connection-errors.md): Learn how to resolve commonly-encountered connection errors
- [Connect latency and timeouts](connect-connection-latency.md): Learn about strategies for managing connection latency and timeouts

## Secure connections

Ensure the integrity and security of your connections to Neon.

- [Connect to Neon securely](connect-connect-securely.md): Learn how to connect to Neon securely using SSL/TLS encrypted connections
- [Avoid MME attacks in Postgres 16](https://neon.com/blog/avoid-mitm-attacks-with-psql-postgres-16): Learn how the psql client in Postgres 16 makes it simple to connect securely

## Connection pooling

Optimize your connections by enabling connection pooling.

- [Connection pooling in Neon](connect-connection-pooling.md): Learn how to enable connection pooling to support up to 10,000 concurrent connections
- [Connection pooling with Prisma](guides-prisma.md#connect-from-serverless-functions): Learn about connecting from Prisma to Neon from serverless functions
