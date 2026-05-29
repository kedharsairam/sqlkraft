---
title: "What hash partitioning with a computed column does"
topic: "io-fundamentals"
description: "The following sample script can be customized for purposes of your implementation:"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

The following sample script can be customized for purposes of your implementation:

SQL

This script can be used to hash partition a table that is experiencing problems caused by

Last

page/trailing page insert contention

. This technique moves contention from the last page by

partitioning the table and distributing inserts across table partitions with a hash value modulus

operation.

As the following diagram illustrates, this technique moves the contention from the last page by

rebuilding the index on the hash function and creating the same number of partitions as there

are physical CPU cores on the SQL Server computer. The inserts are still going into the end of

the logical range (a sequentially increasing value) but the hash value modulus operation

ensures that the inserts are split across the different B-trees, which alleviates the bottleneck.

This is illustrated in the following diagrams:

```sql
--Create the partition scheme and function, align this to the number of CPU cores
1:1 up to 32 core computer
-- so for below this is aligned to 16 core system
CREATE
PARTITION
FUNCTION
[pf_hash16](
TINYINT
)
AS
RANGE
LEFT
FOR
VALUES
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15);
CREATE
PARTITION
SCHEME [ps_hash16]
AS
PARTITION
[pf_hash16]
ALL
TO
([ALL_DATA]);
-- Add the computed column to the existing table (this is an OFFLINE operation)
-- Consider using bulk loading techniques to speed it up
ALTER
TABLE
[dbo].[latch_contention_table]
ADD
[HashValue]
AS
(
CONVERT
(
TINYINT
,
ABS
(BINARY_CHECKSUM([hash_col]) % (16)),
(0))) PERSISTED
NOT
NULL
;
--Create the index on the new partitioning scheme
CREATE
UNIQUE
CLUSTERED
INDEX
[IX_Transaction_ID]
ON
[dbo].[latch_contention_table]([T_ID]
ASC
, [HashValue])
ON
ps_hash16 (HashValue);
```
