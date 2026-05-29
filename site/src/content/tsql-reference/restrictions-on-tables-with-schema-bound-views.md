---
name: "Restrictions on tables with schema-bound views"
title: "Restrictions on tables with schema-bound views"
category: "queries"
description: "are runtime constants. In contrast, the functions"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

are runtime constants. In contrast, the functions

or

aren't runtime constants, because a unique value is produced for each row in the table. Adding a

column with a default value that's not a runtime constant is always run offline and an

exclusive (Sch-M) lock is acquired for the duration of the operation.

While the existing rows reference the value stored in metadata, the default value is stored on the

row for any new rows that are inserted and don't specify another value for the column. The

default value stored in metadata moves to an existing row when the row is updated (even if the

actual column isn't specified in the

statement), or if the table or clustered index is rebuilt.

You can't add columns of type

,

,

,

,

,

,

,

,

,

, or CLR user-defined types in an online operation. You

can't add a column online if doing so causes the maximum possible row size to exceed the 8,060-

byte limit. The column is added as an offline operation in this case.

In SQL Server 2012 (11.x) Enterprise edition and later versions, the

configuration option and the current workload determine the number of processors that run a

single

(index-based)

or

(clustered index)

statement. If the Database Engine detects that the system is busy, it automatically reduces the

degree of parallelism of the operation before statement execution starts. You can manually

configure the number of processors that run the statement by specifying the

option. For

more information, see

Server configuration: max degree of parallelism

.

In addition to performing

operations that involve partitioned tables, use

to

change the state of the columns, constraints, and triggers of a partitioned table, just like you use

it for nonpartitioned tables. However, you can't use this statement to change the way the table

itself is partitioned. To repartition a partitioned table, use

ALTER PARTITION SCHEME (Transact-

SQL)

and

ALTER PARTITION FUNCTION (Transact-SQL)

. Additionally, you can't change the data

type of a column of a partitioned table.

The restrictions that apply to

statements on tables with schema-bound views are the

same as the restrictions currently applied when modifying tables with a simple index. You can add

a column. However, you can't remove or change a column that participates in any schema-bound

```sql
GETUTCDATETIME()
```

```sql
NEWID()
```

```sql
NEWSEQUENTIALID()
```

```sql
NOT NULL
```

```sql
UPDATE
```

```sql
max degree of parallelism
```

```sql
ALTER TABLE ADD
```

```sql
CONSTRAINT
```

```sql
DROP
```

```sql
CONSTRAINT
```

```sql
MAXDOP
```

```sql
SWITCH
```

```sql
ALTER TABLE
```

```sql
ALTER TABLE
```
