---
name: "Limitations and considerations"
title: "Limitations and considerations"
category: "operators"
description: "To resolve this error, remove the"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

## Earlier vector index version limitations

## Current limitations (applies to the latest version too)

To resolve this error, remove the

parameter from

and use the

## syntax instead. For detailed information, see

Error using legacy syntax

.

Earlier vector index versions have the following additional limitations. To check your index

version, see

Verify the index version

.

: Predicates are applied only after vector retrieval, not during the search

process. This can result in fewer rows returned than expected when filters are applied.

: Tables with vector indexes are read-only. No DML operations (INSERT,

UPDATE, DELETE, MERGE) are allowed after the vector index is created. Use the

database scoped configuration to enable DML operations if

you can tolerate stale search results.

: You must manually adjust the

parameter in

to compensate for post-filtering, often requiring oversized values to get the desired

number of results.

The current preview has the following limitations:

Vector indexes can't be partitioned. No partition support.

The table must have a primary key clustered index.

Vector indexes aren't replicated to subscribers.

Tables with vector indexes can't be truncated using

. To remove all data,

drop the vector index first, truncate the table, repopulate with at least 100 rows, then

recreate the index. For more information, see

TRUNCATE TABLE restrictions

.

Vector indexes can't be deployed with DacPac or BACPAC. Vector indexes require at least

100 rows with non-NULL vectors at creation time. When you import a database using

### Workaround

### Minimum row count

### Error behavior

### Example error:

## Minimum data requirements

```sql
TOP_N
```

```sql
VECTOR_SEARCH
```

```sql
SELECT TOP
(N) WITH APPROXIMATE
```

```sql
ALLOW_STALE_VECTOR_INDEX
```

```sql
TOP_N
```

```sql
VECTOR_SEARCH
```

```sql
TRUNCATE TABLE
```

```sql
Msg 42274, Level 16, State 1
Vector search with version 3 index does not support explicit TOP_N parameter.
```
