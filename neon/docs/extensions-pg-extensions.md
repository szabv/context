# Supported Postgres extensions

> The document lists and describes the PostgreSQL extensions supported by Neon, detailing compatibility and usage specifics for each extension within Neon's database environment.

## Source

- [Supported Postgres extensions HTML](https://neon.com/docs/extensions/pg-extensions): The original HTML version of this documentation

Neon supports the Postgres extensions shown in the following table. The supported version of the extension sometimes differs by Postgres version. A dash (`-`) indicates that an extension is not yet supported.

**Need an extension we don't have?** 📩 [Request an extension](extensions-pg-extensions.md#request-an-extension)



| Extension                                                                                        |    PG14 |    PG15 |    PG16 |    PG17 |   PG18 | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :----------------------------------------------------------------------------------------------- | ------: | ------: | ------: | ------: | -----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [address_standardizer](https://postgis.net/docs/Extras.html#Address_Standardizer)                |   3.3.3 |   3.3.3 |   3.3.3 |   3.5.0 |  3.6.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [address_standardizer_data_us](https://postgis.net/docs/Extras.html#Address_Standardizer_Tables) |   3.3.3 |   3.3.3 |   3.3.3 |   3.5.0 |  3.6.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [anon](extensions-postgresql-anonymizer.md)                                                   |   2.4.1 |   2.4.1 |   2.4.1 |   2.4.1 |  2.4.1 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [autoinc (spi)](https://www.postgresql.org/docs/current/contrib-spi.html)                        |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [bloom](https://www.postgresql.org/docs/16/bloom.html)                                           |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [btree_gin](extensions-btree_gin.md)                                                          |     1.3 |     1.3 |     1.3 |     1.3 |    1.3 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [btree_gist](extensions-btree_gist.md)                                                        |     1.6 |     1.7 |     1.7 |     1.7 |    1.8 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [citext](extensions-citext.md)                                                                |     1.6 |     1.6 |     1.6 |     1.6 |    1.8 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [cube](extensions-cube.md)                                                                    |     1.5 |     1.5 |     1.5 |     1.5 |    1.5 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [dblink](extensions-dblink.md)                                                                |     1.2 |     1.2 |     1.2 |     1.2 |    1.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [dict_int](extensions-dict_int.md)                                                            |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [earthdistance](extensions-earthdistance.md)                                                  |     1.1 |     1.1 |     1.2 |     1.2 |    1.2 | To use `earthdistance`, you first need to install its dependency, the [`cube` extension](extensions-cube.md). Run: `CREATE EXTENSION IF NOT EXISTS cube; CREATE EXTENSION IF NOT EXISTS earthdistance`;                                                                                                                                                                                                                                                    |
| [fuzzystrmatch](extensions-fuzzystrmatch.md)                                                  |     1.1 |     1.1 |     1.2 |     1.2 |    1.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [h3](extensions-postgis-related-extensions.md#h3-and-h3-postgis)                              |   4.1.3 |   4.1.3 |   4.1.3 |   4.1.3 |  4.2.3 | Some components have been split out into the `h3_postgis` extension. Install both the `h3` and `h3_postgis` extensions.                                                                                                                                                                                                                                                                                                                                       |
| [h3_postgis](extensions-postgis-related-extensions.md#h3-and-h3-postgis)                      |   4.1.3 |   4.1.3 |   4.1.3 |   4.1.3 |  4.2.3 | Install with `CREATE EXTENSION h3_postgis CASCADE;` (requires `postgis` and `postgis_raster`)                                                                                                                                                                                                                                                                                                                                                                 |
| [hll](https://github.com/citusdata/postgresql-hll)                                               |    2.19 |    2.19 |    2.19 |    2.19 |   2.19 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [hstore](extensions-hstore.md)                                                                |     1.8 |     1.8 |     1.8 |     1.8 |    1.8 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [hypopg](https://hypopg.readthedocs.io/en/rel1_stable/)                                          |   1.4.2 |   1.4.2 |   1.4.2 |   1.4.2 |  1.4.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [insert_username (spi)](https://www.postgresql.org/docs/current/contrib-spi.html)                |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [intagg](https://www.postgresql.org/docs/16/intagg.html)                                         |     1.1 |     1.1 |     1.1 |     1.1 |    1.1 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [intarray](extensions-intarray.md)                                                            |     1.5 |     1.5 |     1.5 |     1.5 |    1.5 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [ip4r](https://github.com/RhodiumToad/ip4r)                                                      |     2.4 |     2.4 |     2.4 |     2.4 |    2.4 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [isn](https://www.postgresql.org/docs/16/isn.html)                                               |     1.2 |     1.2 |     1.2 |     1.2 |    1.3 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [lo](https://www.postgresql.org/docs/16/lo.html)                                                 |     1.1 |     1.1 |     1.1 |     1.1 |    1.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [ltree](extensions-ltree.md)                                                                  |     1.2 |     1.2 |     1.2 |     1.3 |    1.3 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [moddatetime (spi)](https://www.postgresql.org/docs/current/contrib-spi.html)                    |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [neon](extensions-neon.md)                                                                    |     1.9 |     1.9 |     1.9 |     1.9 |    1.9 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [neon_utils](extensions-neon-utils.md)                                                        |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [online_advisor](extensions-online_advisor.md)                                                |       - |       - |       - |     1.0 |      - |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_cron](extensions-pg_cron.md)                                                              |     1.6 |     1.6 |     1.6 |     1.6 |    1.6 | To install `pg_cron`, it must first be enabled. See [Enable the pg_cron extension](extensions-pg_cron.md#enable-the-pgcron-extension) for instructions. Please note that `pg_cron` jobs will only run when your compute is active. We therefore recommend only using `pg_cron` on computes that run 24/7 or where you have disabled [scale to zero](introduction-scale-to-zero.md).                                                                     |
|                                                                                                  |
| [pg_graphql](extensions-pg_graphql.md)                                                        |  1.5.11 |  1.5.11 |  1.5.11 |  1.5.11 |      - |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_hashids](https://github.com/iCyberon/pg_hashids)                                             |   1.2.1 |   1.2.1 |   1.2.1 |   1.2.1 |  1.2.1 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan)                                          |   1.4.1 |   1.5.0 |   1.6.0 |   1.7.0 |  1.8.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_ivm](https://github.com/sraoss/pg_ivm)                                                       |     1.9 |     1.9 |     1.9 |     1.9 |   1.12 | The `create_immv` function is created in the Postgres `public` schema by default, not the `pg_ivm` schema. In this case, run `SELECT create_immv()` instead of `SELECT pg_ivm.create_immv()`.                                                                                                                                                                                                                                                                 |
| [pg_jsonschema](https://github.com/supabase/pg_jsonschema)                                       |   0.3.3 |   0.3.3 |   0.3.3 |   0.3.3 |      - |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_mooncake](extensions-pg_mooncake.md)                                                      |   0.1.2 |   0.1.2 |   0.1.2 |   0.1.2 |      - | This extension is **experimental**. Using a separate, dedicated Neon project is recommended. Run `SET neon.allow_unstable_extensions='true';` before installing. See the [YouTube demo](https://youtu.be/QDNsxw_3ris?feature=shared&t=2048) and the [pg_mooncake documentation](https://pgmooncake.com/docs).                                                                                                                                                 |
| [pg_partman](https://github.com/pgpartman/pg_partman)                                            |   5.1.0 |   5.1.0 |   5.1.0 |   5.1.0 |  5.1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_prewarm](extensions-pg_prewarm.md)                                                        |     1.2 |     1.2 |     1.2 |     1.2 |    1.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_repack](extensions-pg_repack.md)                                                          |   1.5.2 |   1.5.2 |   1.5.2 |   1.5.2 |  1.5.2 | Available only on paid Neon plans. To install `pg_repack`, it must first be enabled by Neon Support. [Open a support ticket](https://console.neon.tech/app/projects?modal=support) with your endpoint ID and database name to request it. After it's enabled, you'll need to restart your compute before running `CREATE EXTENSION pg_repack;` To use `pg_repack`, you will need to [install the pg_repack CLI](https://reorg.github.io/pg_repack/#download). |
| [pg_roaringbitmap](https://github.com/ChenHuajun/pg_roaringbitmap)                               |     0.5 |     0.5 |     0.5 |     0.5 |    0.5 | Install with `CREATE EXTENSION roaringbitmap;`                                                                                                                                                                                                                                                                                                                                                                                                                |
| [pg_session_jwt](data-api-get-started.md)                                                     |   0.3.1 |   0.3.1 |   0.3.1 |   0.3.1 |  0.3.1 | This extension provides JWT session management functionality used by the [Data API](data-api-get-started.md).                                                                                                                                                                                                                                                                                                                                              |
| [pg_stat_statements](extensions-pg_stat_statements.md)                                        |     1.9 |    1.10 |    1.10 |    1.11 |   1.12 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_tiktoken](extensions-pg_tiktoken.md)                                                      |   0.0.1 |   0.0.1 |   0.0.1 |   0.0.1 |  0.0.1 | The [neon_superuser](manage-roles.md#the-neonsuperuser-role) role has `EXECUTE` privilege on the `pg_stat_statements_reset()` function.                                                                                                                                                                                                                                                                                                                    |
| [pg_trgm](extensions-pg_trgm.md)                                                              |     1.6 |     1.6 |     1.6 |     1.6 |    1.6 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pg_uuidv7](extensions-pg_uuidv7.md)                                                          |     1.6 |     1.6 |     1.6 |     1.6 |    1.6 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pgcrypto](extensions-pgcrypto.md)                                                            |     1.3 |     1.3 |     1.3 |     1.3 |    1.4 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pgjwt](https://github.com/michelp/pgjwt)                                                        |   0.2.0 |   0.2.0 |   0.2.0 |   0.2.0 |  0.2.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pgrag](extensions-pgrag.md)                                                                  |   0.0.0 |   0.0.0 |   0.0.0 |   0.0.0 |  0.0.0 | This extension is **experimental**. Using a separate, dedicated Neon project is recommended. Run `SET neon.allow_unstable_extensions='true';` before installing.                                                                                                                                                                                                                                                                                              |
| [pgrouting](extensions-postgis-related-extensions.md#pgrouting)                               |   3.4.2 |   3.4.2 |   3.4.2 |   3.6.2 |  3.8.0 | The PostGIS extension must be installed first.                                                                                                                                                                                                                                                                                                                                                                                                                |
| [pgrowlocks](extensions-pgrowlocks.md)                                                        |     1.2 |     1.2 |     1.2 |     1.2 |    1.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pgstattuple](extensions-pgstattuple.md)                                                      |     1.5 |     1.5 |     1.5 |     1.5 |    1.5 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pgtap](https://pgtap.org/documentation.html)                                                    |   1.3.3 |   1.3.3 |   1.3.3 |   1.3.3 |  1.3.3 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [pgvector](extensions-pgvector.md)                                                            |   0.8.0 |   0.8.0 |   0.8.0 |   0.8.0 |  0.8.1 | Install with `CREATE EXTENSION vector;`                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [pg_search](extensions-pg_search.md)                                                          | 0.15.26 | 0.15.26 | 0.15.26 | 0.15.26 |      - | Install with `CREATE EXTENSION pg_search;` on Postgres 17.                                                                                                                                                                                                                                                                                                                                                                                                    |
| [pgx_ulid](https://github.com/pksunkara/pgx_ulid)                                                |   0.1.5 |   0.1.5 |   0.1.5 |   0.2.0 |      - | Install with `CREATE EXTENSION ulid;` on Postgres 14, 15, 16. Install with `CREATE EXTENSION pgx_ulid; ` on Postgres 17.                                                                                                                                                                                                                                                                                                                                      |
| [plcoffee](https://coffeescript.org/)                                                            |  3.1.10 |  3.1.10 |  3.1.10 |       - |      - |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [plls](https://livescript.net/)                                                                  |  3.1.10 |  3.1.10 |  3.1.10 |       - |      - |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [plpgsql](https://www.postgresql.org/docs/16/plpgsql.html)                                       |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 | Pre-installed with Postgres.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [plpgsql_check](https://pgxn.org/dist/plpgsql_check/)                                            |   2.8.2 |   2.8.2 |   2.8.2 |   2.8.2 |  2.8.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [plv8](https://github.com/plv8/plv8)                                                             |  3.1.10 |  3.1.10 |  3.1.10 |   3.2.3 |      - |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [postgis](extensions-postgis.md)                                                              |   3.3.3 |   3.3.3 |   3.3.3 |   3.5.0 |  3.6.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [postgis_raster](https://postgis.net/docs/RT_reference.html)                                     |   3.3.3 |   3.3.3 |   3.3.3 |   3.5.0 |  3.6.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [postgis_sfcgal](extensions-postgis-related-extensions.md#postgis-sfcgal)                     |   3.3.3 |   3.3.3 |   3.3.3 |   3.5.0 |  3.6.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [postgis_tiger_geocoder](extensions-postgis-related-extensions.md#postgis-tiger-geocoder)     |   3.3.3 |   3.3.3 |   3.3.3 |   3.5.0 |  3.6.0 | Cannot be installed using the Neon SQL Editor. Use your `psql` user credentials to install this extension.                                                                                                                                                                                                                                                                                                                                                    |
| [postgis_topology](https://www.postgis.net/docs/Topology.html)                                   |   3.3.3 |   3.3.3 |   3.3.3 |   3.5.0 |  3.6.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [postgres_fdw](extensions-postgres_fdw.md)                                                    |     1.1 |     1.1 |     1.1 |     1.1 |    1.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [prefix](https://github.com/dimitri/prefix)                                                      |   1.2.0 |   1.2.0 |   1.2.0 |   1.2.0 |  1.2.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [rdkit](https://github.com/rdkit/rdkit)                                                          |   4.3.0 |   4.3.0 |   4.3.0 |   4.6.0 |  4.8.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [refint (spi)](https://www.postgresql.org/docs/current/contrib-spi.html)                         |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [rum](https://github.com/postgrespro/rum)                                                        |     1.3 |     1.3 |     1.3 |     1.3 |      - |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [seg](https://www.postgresql.org/docs/16/seg.html)                                               |     1.4 |     1.4 |     1.4 |     1.4 |    1.4 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [semver](https://pgxn.org/dist/semver)                                                           |  0.32.1 |  0.32.1 |  0.32.1 |  0.40.0 | 0.40.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [tablefunc](extensions-tablefunc.md)                                                          |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [tcn](https://www.postgresql.org/docs/16/tcn.html)                                               |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [timescaledb](extensions-timescaledb.md)                                                      |  2.10.1 |  2.10.1 |  2.13.0 |  2.17.1 |      - | Only Apache-2 licensed features are supported. Compression is not supported.                                                                                                                                                                                                                                                                                                                                                                                  |
| [tsm_system_rows](https://www.postgresql.org/docs/16/tsm-system-rows.html)                       |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [tsm_system_time](https://www.postgresql.org/docs/16/tsm-system-time.html)                       |     1.0 |     1.0 |     1.0 |     1.0 |    1.0 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [unaccent](extensions-unaccent.md)                                                            |     1.1 |     1.1 |     1.1 |     1.1 |    1.1 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [unit](https://github.com/df7cb/postgresql-unit)                                                 |       7 |       7 |       7 |       7 |      - |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [uuid-ossp](extensions-uuid-ossp.md)                                                          |     1.1 |     1.1 |     1.1 |     1.1 |    1.1 | Double-quote the extension name when installing: `CREATE EXTENSION "uuid-ossp"`                                                                                                                                                                                                                                                                                                                                                                               |
| [wal2json](extensions-wal2json.md)                                                            |     2.6 |     2.6 |     2.6 |     2.6 |    2.6 | `CREATE EXTENSION` not required. This decoder plugin is available by default but requires enabling [logical replication](guides-logical-replication-guide.md) in Neon.                                                                                                                                                                                                                                                                                     |
| [xml2](extensions-xml2.md)                                                                    |     1.1 |     1.1 |     1.1 |     1.1 |    1.2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Install an extension

Unless otherwise noted, supported extensions can be installed using [CREATE EXTENSION](https://www.postgresql.org/docs/16/sql-createextension.html) syntax.

```sql
CREATE EXTENSION <extension_name>;
```

You can install extensions from the Neon SQL Editor or from a client such as `psql` that permits running SQL queries. For information about using the Neon SQL Editor, see [Query with Neon's SQL Editor](get-started-query-with-neon-sql-editor.md). For information about using the `psql` client with Neon, see [Connect with psql](connect-query-with-psql-editor.md).

## Update an extension version

Neon updates supported extensions as new versions become available. Version updates are communicated in the [Changelog](changelog.md). To check the current version of extensions you have installed, query the `pg_extension` table:

```bash
SELECT * FROM pg_extension;
```

You can update an extension to the latest version using `ALTER EXTENSION <extension_name> UPDATE TO <new_version>` syntax. For example:

```sql
ALTER EXTENSION vector UPDATE TO '0.7.0';
```

   **Important**: When Neon releases a new extension or new extension version, a compute restart is required to make the new extension or extension version available for installation or update. A compute restart may occur on its own due to Neon's default [scale to zero](introduction-scale-to-zero.md) behavior. However, if your compute never restarts because you disabled scale to zero or because your compute is constantly active, you may need to force a restart. To force a restart, you can issue [Restart endpoint](https://api-docs.neon.tech/reference/restartprojectendpoint) API call. Please be aware that restarting a compute temporarily interrupts any connections currently using the compute. Extensions installations and updates are automatically applied to any read replica computes on the same branch as your primary compute the next time the read replica compute restarts.

## Request an extension



_We appreciate all extension requests. While we can't guarantee support, we regularly review requests and prioritize them based on factors like user demand, popularity in the Postgres ecosystem, and Neon's product direction. Some extensions are simple to add, while others require significant integration work._

## Custom-built extensions

For [Scale](introduction-plans.md) plan customers, Neon supports custom-built Postgres extensions for exclusive use with your Neon account. If you developed your own Postgres extension and want to use it with Neon, please reach out to us as described above. Please include the following information in your request:

- A repository link or archive file containing the source code for your extension
- A description of what the extension does, instructions for compiling it, and any prerequisites
- Whether an NDA or licensing agreement is necessary for Neon to provide support for your extension

Please keep in mind that certain restrictions may apply with respect to Postgres privileges and local file system access. Additionally, Neon features such as _Autoscaling_ and _Scale to Zero_ may limit the types of extensions we can support.

Depending on the nature of your extension, Neon may also request a liability waiver.

Custom-built extensions are not yet supported for Neon projects provisioned on Azure.

## Extension support

Neon supports a large number of Postgres extensions. When we say an extension is "supported," we mean that it's available for you to enable and use in your project.

We don't actively maintain third-party extension code. If you run into an issue or discover a bug with an extension, we recommend reporting it to the extension's upstream maintainers. If a fix is released, we're happy to update to the latest version of the extension.

For the extension versions that Neon supports, refer to the [Supported extensions table](extensions-pg-extensions.md) above. You can request support for a new version of an extension by opening a [support ticket](https://console.neon.tech/app/projects?modal=support) or by reaching out to us on [Discord](https://discord.com/invite/92vNTzKDGp).

## Experimental extensions

Neon occasionally adds support for extensions that are in early stages of development or undergoing validation. These extensions require an explicit opt-in and are not recommended for production use.

To run these extensions, you'll be required to configure the following session variable before installing the extension:

```sql
SET neon.allow_unstable_extensions = 'true';
```

   **Note**: "Unstable" doesn't mean the extension is buggy. It means that we have not yet met service level expectations for the extension, often related to testing and Neon integration requirements.

**Things to know about experimental extensions:**

- **Use with caution:** We recommend trying experimental extensions in a separate project—not in the Neon project you use for production.
- **Limited support:** Experimental extensions aren't covered by Neon support. If an extension causes your database to fail or prevents it from starting, we'll help you disable it if possible—but we can't guarantee more than that.
- **No guarantees:** An experimental extension might never become fully supported. It could require significant work from Neon or the extension's maintainers before it's ready for general use.
- **Subject to change or removal:** Experimental extensions may be updated at any time, including breaking changes. They can also be removed—especially if they pose security or operational risks.

If you're experimenting with an extension and run into trouble, we recommend checking with the extension's maintainers or community for support.

## Extensions with preloaded libraries

A preloaded library in Postgres is a shared library that must be loaded into memory when the Postgres server starts. These libraries are specified in your Postgres server's startup configuration using the `shared_preload_libraries` parameter and cannot be added dynamically after the server has started.

Some Postgres extensions require preloaded libraries but most do not. Neon Postgres servers preload libraries for certain extensions by default. You can view **currently enabled** libraries by running the following command.

```sql
SHOW shared_preload_libraries;
neon,pg_stat_statements,timescaledb,pg_cron,pg_partman_bgw,rag_bge_small_en_v15,rag_jina_reranker_v1_tiny_en
```

### Viewing available libraries

You can view **available** libraries by running [List preloaded libraries](https://api-docs.neon.tech/reference/getavailablepreloadlibraries) API:

```bash
curl --request GET \
     --url https://console.neon.tech/api/v2/projects/your_project_id/available_preload_libraries \
     --header 'accept: application/json' \
     --header 'authorization: Bearer $NEON_API_KEY'
```

The response body lists available libraries and whether the libraries are enabled by default. Response body attributes include:

- `library_name` — library name, typically named for the associated extension
- `description` — a description of the extension
- `is_default` — whether the library is enabled by default
- `is_experimental` — whether the extensions is [experimental](extensions-pg-extensions.md#experimental-extensions)
- `version` — the extension version

Details: Response body
For attribute definitions, find the [List preloaded libraries](https://api-docs.neon.tech/reference/getavailablepreloadlibraries) endpoint in the [Neon API Reference](https://api-docs.neon.tech/reference/getting-started-with-neon-api). Definitions are provided in the **Responses** section.

```json
{
  "libraries": [
    {
      "library_name": "timescaledb",
      "description": "Enables scalable inserts and complex queries for time-series data.",
      "is_default": true,
      "is_experimental": false,
      "version": "2.17.1"
    },
    {
      "library_name": "pg_cron",
      "description": "pg_cron is a cron-like job scheduler for PostgreSQL.",
      "is_default": true,
      "is_experimental": false,
      "version": "1.6.4"
    },
    {
      "library_name": "pg_partman_bgw",
      "description": "pg_partman_bgw is a background worker for pg_partman.",
      "is_default": true,
      "is_experimental": false,
      "version": "5.1.0"
    },
    {
      "library_name": "rag_bge_small_en_v15,rag_jina_reranker_v1_tiny_en",
      "description": "Shared libraries for pgrag extensions",
      "is_default": true,
      "is_experimental": true,
      "version": "0.0.0"
    },
    {
      "library_name": "pgx_ulid",
      "description": "pgx_ulid is a PostgreSQL extension for ULID generation.",
      "is_default": false,
      "is_experimental": false,
      "version": "0.2.0"
    },
    {
      "library_name": "pg_mooncake",
      "description": "Columnstore Table in Postgres",
      "is_default": false,
      "is_experimental": false,
      "version": "0.1.1"
    },
    {
      "library_name": "pg_search",
      "description": "pg_search: Full text search for PostgreSQL using BM25",
      "is_default": false,
      "is_experimental": false,
      "version": "0.15.12"
    },
    {
      "library_name": "anon",
      "description": "Anonymization & Data Masking for PostgreSQL",
      "is_default": false,
      "is_experimental": false,
      "version": "2.1.0"
    }
  ]
}
```

Important notes about libraries for Postgres extensions:

- Available libraries and those enabled by default may differ by Postgres version
- Neon does not enable libraries for all extensions that have them

### Enabling preloaded libraries

You can enable available libraries using the `preloaded_libraries` object in a [Create project](https://api-docs.neon.tech/reference/createproject) or [Update project](https://api-docs.neon.tech/reference/updateproject) API call. For example, this `Update project` call enables the specified libraries for the Neon project. When running this call, you have to provide a [Neon project ID](reference-glossary.md#project-id) and a [Neon API key](manage-api-keys.md).

```bash
curl --request PATCH \
    --url https://console.neon.tech/api/v2/projects/<your_project_id> \
    --header 'accept: application/json' \
    --header 'authorization: Bearer $NEON_API_KEY' \
    --header 'content-type: application/json' \
    --data '
{
  "project": {
    "settings": {
      "preload_libraries": {
        "enabled_libraries": [
          "neon","pg_stat_statements","timescaledb","pg_cron","pg_partman_bgw","rag_bge_small_en_v15,rag_jina_reranker_v1_tiny_en","pg_search"
        ]
      }
    }
  }
}
'
```

When running a `Create project` or `Update project` API call to enable libraries:

- Library names must be quoted, comma-separated, and specified in a single string.
- Specify all libraries that should be enabled. If a library is not included in the API call, it will not be enabled.
- The "use_defaults": true`option overrides the`"enabled_libraries"` option, enabling only default libraries
- The `neon` and `pg_stat_statements` libraries will remain enabled whether you include them in your API call or not — they're used by a Neon system-managed database.
- If you do not use one of the libraries enabled by default, you can exclude it from your API call. For example, if you do not use the `pgrag` extension, you can exclude its libraries (`"rag_bge_small_en_v15,rag_jina_reranker_v1_tiny_en"`).

## Extension notes

- Neon supports the `uuid-ossp` extension for generating UUIDs instead of the `uuid` extension.
- The `sslinfo` extension is not supported. Neon handles connections via a proxy that checks SSL.
- The `file_fdw` extension is not supported. Files would not remain accessible when Neon scales to zero.
