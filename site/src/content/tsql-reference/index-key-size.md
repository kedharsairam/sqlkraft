---
name: 'Index key size'
title: 'Index key size'
category: 'hints'
description: 'compatibility level is set to 90 or higher. If the database compatibility level is set to 80 or'
tags: ["tsql", "hints"]
pubDate: 2026-05-29
---

Setting

to

implicitly sets

to

when the database

compatibility level is set to 90 or higher. If the database compatibility level is set to 80 or

earlier, the

option must explicitly be set to

.

If the

options are incorrect, the following conditions can occur:

Creating the filtered index fails.

The Database Engine generates an error and rolls back the

,

,

, or

statement that changes data in the index.

Query optimizer doesn't consider the index in the execution plan for any Transact-SQL

statements.

For more information about filtered indexes, see

Create filtered indexes

and the

SQL Server

index architecture and design guide

.

For information about spatial indexes, see

CREATE SPATIAL INDEX

and

Spatial indexes

overview

.

For information about XML indexes see,

CREATE XML INDEX

and

XML Indexes (SQL Server)

.

The maximum size for an index key is 900 bytes for a clustered index and 1,700 bytes for a

nonclustered index. (Before SQL Database and SQL Server 2016 (13.x) the limit was always 900

1

1

### varchar

### varchar

### varchar

```sql
SET
```

```sql
ANSI_PADDING
ON
ON
ON
OFF
ANSI_WARNINGS
ON
ON
ON
OFF
ARITHABORT
ON
ON
OFF
OFF
CONCAT_NULL_YIELDS_NULL
ON
ON
ON
OFF
NUMERIC_ROUNDABORT
OFF
OFF
OFF
OFF
QUOTED_IDENTIFIER
ON
ON
ON
OFF
```

```sql
ANSI_WARNINGS
```

```sql
ON
```

```sql
ARITHABORT
```

```sql
ON
```

```sql
ARITHABORT
```

```sql
ON
```

```sql
SET
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
MERGE
```
