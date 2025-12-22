# Neon CLI commands — databases

> The document details Neon CLI commands for managing databases, including creating, listing, and deleting databases within the Neon environment.

## Source

- [Neon CLI commands — databases HTML](https://neon.com/docs/reference/cli-databases): The original HTML version of this documentation

## Before you begin

- Before running the `databases` command, ensure that you have [installed the Neon CLI](reference-cli-install.md).
- If you have not authenticated with the [neon auth](reference-cli-auth.md) command, running a Neon CLI command automatically launches the Neon CLI browser authentication process. Alternatively, you can specify a Neon API key using the `--api-key` option when running a command. See [Connect](reference-neon-cli.md#connect).

For information about databases in Neon, see [Manage databases](manage-databases.md).

## The `databases` command

### Usage

The `databases` command allows you to list, create, and delete databases in a Neon project.

| Subcommand        | Description       |
| ----------------- | ----------------- |
| [list](reference-cli-databases.md#list)     | List databases    |
| [create](reference-cli-databases.md#create) | Create a database |
| [delete](reference-cli-databases.md#delete) | Delete a database |

### list

This subcommand allows you to list databases.

#### Usage

```bash
neon databases list [options]
```

#### Options

In addition to the Neon CLI [global options](reference-neon-cli.md#global-options), the `list` subcommand supports these options:

| Option           | Description                                                                                   | Type   |                      Required                       |
| ---------------- | --------------------------------------------------------------------------------------------- | ------ | :-------------------------------------------------: |
| `--context-file` | [Context file](reference-cli-set-context.md#using-a-named-context-file) path and file name | string |                                                     |
| `--project-id`   | Project ID                                                                                    | string | Only if your Neon account has more than one project |
| `--branch`       | Branch ID or name                                                                             | string |                                                     |

If a branch ID or name is not provided, the command lists databases for the default branch of the project.

#### Example

```bash
neon databases list --branch br-autumn-dust-190886
┌────────┬────────────┬──────────────────────┐
│ Name   │ Owner Name │ Created At           │
├────────┼────────────┼──────────────────────┤
│ neondb │ daniel     │ 2023-06-19T18:27:19Z │
└────────┴────────────┴──────────────────────┘
```

### create

This subcommand allows you to create a database.

#### Usage

```bash
neon databases create [options]
```

#### Options

In addition to the Neon CLI [global options](reference-neon-cli.md#global-options), the `create` subcommand supports these options:

| Option           | Description                                                                                   | Type   |                      Required                       |
| ---------------- | --------------------------------------------------------------------------------------------- | ------ | :-------------------------------------------------: |
| `--context-file` | [Context file](reference-cli-set-context.md#using-a-named-context-file) path and file name | string |                                                     |
| `--project-id`   | Project ID                                                                                    | string | Only if your Neon account has more than one project |
| `--branch`       | Branch ID or name                                                                             | string |                                                     |
| `--name`         | The name of the database                                                                      | string |                       &check;                       |
| `--owner-name`   | The name of the role that owns the database                                                   | string |                                                     |

- If a branch ID or name is not provided, the command creates the database in the default branch of the project.
- If the `--owner-name` option is not specified, the current user becomes the database owner.

#### Example

```bash
neon databases create --name mynewdb --owner-name john
┌─────────┬────────────┬──────────────────────┐
│ Name    │ Owner Name │ Created At           │
├─────────┼────────────┼──────────────────────┤
│ mynewdb │ john       │ 2023-06-19T23:45:45Z │
└─────────┴────────────┴──────────────────────┘
```

### delete

This subcommand allows you to delete a database.

#### Usage

```bash
neon databases delete <database> [options]
```

`<database>` is the database name.

#### Options

In addition to the Neon CLI [global options](reference-neon-cli.md#global-options), the `delete` subcommand supports these options:

| Option           | Description                                                                                   | Type   |                      Required                       |
| ---------------- | --------------------------------------------------------------------------------------------- | ------ | :-------------------------------------------------: |
| `--context-file` | [Context file](reference-cli-set-context.md#using-a-named-context-file) path and file name | string |                                                     |
| `--project-id`   | Project ID                                                                                    | string | Only if your Neon account has more than one project |
| `--branch`       | Branch ID or name                                                                             | string |                                                     |

If a branch ID or name is not provided, it is assumed the database resides in the default branch of the project.

#### Example

```bash
neon databases delete mydb
┌─────────┬────────────┬──────────────────────┐
│ Name    │ Owner Name │ Created At           │
├─────────┼────────────┼──────────────────────┤
│ mydb    │ daniel     │ 2023-06-19T23:45:45Z │
└─────────┴────────────┴──────────────────────┘
```
