---
title: "New partition-aware seek operation"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

In SQL Server, the internal representation of a partitioned table is changed so that the table

appears to the query processor to be a multicolumn index with

as the leading

column.

is a hidden computed column used internally to represent the

of the

partition containing a specific row. For example, assume the table T, defined as

, is

partitioned on column a, and has a clustered index on column b. In SQL Server, this partitioned

table is treated internally as a nonpartitioned table with the schema

and a clustered index on the composite key

. This allows the Query Optimizer

to perform seek operations based on

on any partitioned table or index.

Partition elimination is now done in this seek operation.

In addition, the Query Optimizer is extended so that a seek or scan operation with one

condition can be done on

(as the logical leading column) and possibly other index

key columns, and then a second-level seek, with a different condition, can be done on one or

more additional columns, for each distinct value that meets the qualification for the first-level

seek operation. That is, this operation, called a skip scan, allows the Query Optimizer to

perform a seek or scan operation based on one condition to determine the partitions to be

accessed and a second-level index seek operation within that operator to return rows from

these partitions that meet a different condition. For example, consider the following query.

For this example, assume that table T, defined as

, is partitioned on column a, and

has a clustered index on column b. The partition boundaries for table T are defined by the

following partition function:

To solve the query, the query processor performs a first-level seek operation to find every

partition that contains rows that meet the condition

. This identifies the partitions to

be accessed. Within each partition identified, the processor then performs a second-level seek

Until SQL Server 2014 (12.x), partitioned tables and indexes are supported only in the SQL

Server Enterprise, Developer, and Evaluation editions. Starting with SQL Server 2016 (13.x)

SP1, partitioned tables and indexes are also supported in SQL Server Standard edition.

`PartitionID`

`PartitionID`

`ID`

```sql
T(a, b, c)
```

```sql
T(PartitionID, a, b, c)
```

```sql
(PartitionID, b)
```

`PartitionID`

`PartitionID`

```sql
T(a, b, c)
```

```sql
T.a < 10
```

```sql
SELECT
*
FROM
T
WHERE a < 10 and b = 2;
CREATE
PARTITION
FUNCTION myRangePF1 (
int
)
AS
RANGE
LEFT
FOR
VALUES (3, 7, 10);
```
