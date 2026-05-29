---
name: 'sys.query_context_settings'
title: 'sys.query_context_settings'
category: 'objects'
description: '- query that''s being used in cursor update requests'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
- query that's being used in cursor update requests

- initial result set is returned when a cursor is opened

(Cursor Auto Fetch)

- encrypted query

- query in context of row-level security predicate

Cursor options specified by the user such as the cursor type.

Cursor options that SQL Server might implicitly convert to in

order to support the execution of the statement.

The type of trigger execution plan used as the result of a

statement.

0 indicates a non-trigger plan, a trigger plan that doesn't

execute as the result of a

statement, or a trigger plan

that executes as the result of a

statement that only

specifies a

action.

1 indicates an

trigger plan that runs as the result of a

statement.

2 indicates an

trigger plan that runs as the result of a

statement.

3 indicates a

trigger plan that runs as the result of a

statement containing a corresponding

or

action.

For nested triggers run by cascading actions, this value is the

action of the

statement that caused the cascade.

ID of the default schema, which is used to resolve names

that aren't fully qualified.

Used for replication.

1 indicates a contained database.

Requires the

permission.

sys.database_query_store_options

sys.query_store_plan

sys.query_store_query

sys.query_store_query_text

sys.query_store_runtime_stats

sys.query_store_wait_stats

sys.query_store_runtime_stats_interval

Monitor performance by using the Query Store

System catalog views (Transact-SQL)

Query Store stored procedures (Transact-SQL)

sys.fn_stmt_sql_handle_from_sql_stmt

Last updated on 12/29/2025

Related content

```sql
0x20
```

```sql
0x40
```

```sql
0x80
```

```sql
0x100
```

```sql
required_cursor_options
```

```sql
acceptable_cursor_options
```

```sql
merge_action_type
```

```sql
MERGE
```

```sql
MERGE
```

```sql
MERGE
```

```sql
DELETE
```

```sql
INSERT
```

```sql
MERGE
```

```sql
UPDATE
```

```sql
MERGE
```

```sql
DELETE
```

```sql
MERGE
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
MERGE
```

```sql
default_schema_id
```

```sql
is_replication_specific
```

```sql
is_contained
```

```sql
VIEW DATABASE STATE
```
