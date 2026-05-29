---
title: "Columnstore index architecture"
topic: "index-architecture"
description: "The following example creates a table with columns of different data types."
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

The following example creates a table with columns of different data types.

SQL

In the following filtered index definition, column

is implicitly converted to an integer data

type for comparing it to the constant 1. This generates error message 10611 because the

conversion occurs on the left-hand side of the operator in the filtered predicate.

SQL

The solution is to convert the constant on the right-hand side to be of the same type as

column

, as seen in the following example:

SQL

Moving the data conversion from the left side to the right side of a comparison operator might

change the meaning of the conversion. In the previous example, when the

operator

was added to the right side, the comparison changed from an

comparison to a

comparison.

A

columnstore index

is a technology for storing, retrieving, and managing data by using a

columnar data format, called columnstore. For more information, see

Columnstore indexes:

overview

.

For version information and to find out what's new, visit

What's new in columnstore indexes

.

Knowing these basics makes it easier to understand other columnstore articles that explain

how to use this technology effectively.

### columnstore

### rowstore

### deltastore

### rowgroup

```sql
b
```

```sql
b
```

```sql
CONVERT
```

```sql
CREATE
TABLE
dbo.TestTable
(
a
INT
,
b VARBINARY(4)
);
CREATE
NONCLUSTERED
INDEX
TestTabIndex
ON
dbo.TestTable (a, b)
WHERE
b = 1;
CREATE
INDEX
TestTabIndex
ON
dbo.TestTable (a, b)
WHERE
b =
CONVERT
(VARBINARY(4), 1);
```
