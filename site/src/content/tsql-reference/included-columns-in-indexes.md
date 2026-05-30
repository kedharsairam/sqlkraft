---
name: "Included columns in indexes"
title: "Included columns in indexes"
category: "predicates"
description: "constraint can contain a computed column as long as it satisfies all"
tags: ["tsql", "predicates"]
pubDate: 2026-05-29
---

The

or

constraint can contain a computed column as long as it satisfies all

conditions for indexing. Specifically, the computed column must be deterministic and precise

or deterministic and persisted. For more information about determinism, see

Deterministic and

Nondeterministic Functions

.

Computed columns derived from

,

,

,

,

,

, and

data types can be indexed either as a key or included non-key

column as long as the computed column data type is allowable as an index key column or non-

key column. For example, you can't create a primary XML index on a computed

column. If

the index key size exceeds 900 bytes, a warning message is displayed.

Creating an index on a computed column might cause the failure of an insert or update

operation that previously worked. Such a failure might occur when the computed column

results in an arithmetic error.

For example, in the following table, although the expression of the computed column

appears to result in an arithmetic error when the row is inserted, the

statement works.

However, if you create an index on computed column

, the same

statement fails.

For more information, see

Indexes on computed columns

.

Non-key columns, called included columns, can be added to the leaf level of a nonclustered

index to improve query performance by covering the query. That is, all columns referenced in

the query are included in the index as either key or non-key columns. This allows the query

optimizer to obtain all required information from a nonclustered index scan or seek; the table

or clustered index data isn't accessed. For more information, see

Create indexes with included

columns

and the

SQL Server index architecture and design guide

.

`UNIQUE`

```sql
PRIMARY KEY
```

```sql
c
```

`INSERT`

```sql
c
```

`INSERT`

```sql
CREATE
TABLE t1 (a
INT
, b
INT
, c
AS a/b);
INSERT
INTO t1
VALUES (1, 0);
CREATE
TABLE t1 (a
INT
, b
INT
, c
AS a/b);
CREATE
UNIQUE
CLUSTERED
INDEX
Idx1
ON t1(c);
INSERT
INTO t1
VALUES (1, 0);
```
