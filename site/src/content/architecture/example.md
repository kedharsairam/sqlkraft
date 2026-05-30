---
title: "Example"
topic: "query-processing"
description: "Table Partition 3: A >= 20 AND A < 30"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Table Partition 3: A >= 20 AND A < 30

B=50, B=100, B=150

Table Partition 4: A >= 30

B=50, B=100, B=150

To improve the performance of queries that access a large amount of data from large

partitioned tables and indexes, we recommend the following best practices:

Stripe each partition across many disks. This is especially relevant when using spinning

disks.

When possible, use a server with enough main memory to fit frequently accessed

partitions, or all partitions in memory, to reduce I/O cost.

If the data you query won't fit in memory, compress the tables and indexes. This will

reduce I/O cost.

Use a server with fast processors and as many processor cores as you can afford, to take

advantage of parallel query processing capability.

Ensure the server has sufficient I/O controller bandwidth.

Create a clustered index on every large partitioned table to take advantage of B-tree

scanning optimizations.

Follow the best practice recommendations in the white paper,

The Data Loading

Performance Guide

, when bulk loading data into partitioned tables.

The following example creates a test database containing a single table with seven partitions.

Use the tools described previously when executing the queries in this example to view

partitioning information for both compile-time and run-time plans.

SQL

７

Note

This example inserts more than 1 million rows into the table. Running this example can

take several minutes depending on your hardware. Before executing this example, verify

that you have more than 1.5 GB of disk space available.

Logical and physical showplan operator reference

Extended Events overview

## Best practices for monitoring workloads with Query Store

Cardinality Estimation (SQL Server)

Intelligent query processing in SQL databases

Operator Precedence (Transact-SQL)

Execution plan overview

Performance Center for SQL Server Database Engine and Azure SQL Database

）

Note:

The author created this article with assistance from AI.

Learn more

Last updated on 11/18/2025

Related content

```sql
USE
master
;
GO
IF DB_ID (N'db_sales_test') IS NOT NULL
```

```sql
DROP
DATABASE
db_sales_test;
GO
CREATE
DATABASE
db_sales_test;
GO
USE
db_sales_test;
GO
CREATE
PARTITION
FUNCTION
[pf_range_fact](
int
)
AS
RANGE
RIGHT
FOR
VALUES
(20080801, 20080901, 20081001, 20081101, 20081201, 20090101);
GO
CREATE
PARTITION
SCHEME [ps_fact_sales]
AS
PARTITION
[pf_range_fact]
ALL
TO
([PRIMARY]);
GO
CREATE
TABLE
fact_sales(date_id
int
, product_id
int
, store_id
int
,
quantity
int
, unit_price
numeric
(7,2), other_data
char
(1000))
ON
ps_fact_sales(date_id);
GO
CREATE
CLUSTERED
INDEX
ci
ON
fact_sales(date_id);
GO
PRINT 'Loading...';
SET
NOCOUNT
ON
;
DECLARE
@i
int
;
SET
@i = 1;
WHILE (@i<1000000)
BEGIN
INSERT
INTO
fact_sales
VALUES
(20080800 + (@i%30) + 1, @i%10000, @i%200,
RAND
() -
25, (@i%3) + 1,
''
);
SET
@i += 1;
END
;
GO
DECLARE
@i
int
;
SET
@i = 1;
WHILE (@i<10000)
BEGIN
INSERT
INTO
fact_sales
VALUES
(20080900 + (@i%30) + 1, @i%10000, @i%200,
RAND
() -
25, (@i%3) + 1,
''
);
SET
@i += 1;
END
;
PRINT 'Done.';
GO
-- Two-partition query.
SET
STATISTICS
XML
ON
;
GO
SELECT
date_id,
SUM
(quantity*unit_price)
AS
total_price
FROM
fact_sales
WHERE
date_id
BETWEEN
20080802
AND
20080902
GROUP
BY
date_id ;
GO
SET
STATISTICS
XML
OFF
;
GO
-- Single-partition query.
SET
STATISTICS
XML
ON
;
GO
SELECT
date_id,
SUM
(quantity*unit_price)
AS
total_price
FROM
fact_sales
WHERE
date_id
BETWEEN
20080801
AND
20080831
```

```sql
GROUP
BY
date_id;
GO
SET
STATISTICS
XML
OFF
;
GO
```
