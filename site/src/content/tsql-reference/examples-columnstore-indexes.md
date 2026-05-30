---
name: "Examples: Columnstore indexes"
title: "Examples: Columnstore indexes"
category: "statements"
description: "These examples apply to columnstore indexes."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## A. REORGANIZE demo

These examples apply to columnstore indexes.

This example demonstrates how the

command works. It creates a

table that has multiple rowgroups, and then demonstrates how

merges the

rowgroups.

Use the TABLOCK option to insert rows in parallel. Starting with SQL Server 2016 (13.x), the

operation can run in parallel when

is used.

Run this command to see the

delta rowgroups. The number of rowgroups depends on

the degree of parallelism.

Run this command to force all

and

rowgroups into the columnstore.

Run this command again and you see that smaller rowgroups are merged into one compressed

rowgroup.

## B. Compress CLOSED delta rowgroups into the columnstore

## C. Compress all OPEN AND CLOSED delta rowgroups into the

## columnstore

This example uses the

option to compress each

delta rowgroup into the

columnstore as a compressed rowgroup. This isn't necessary, but is useful when the tuple-

mover isn't compressing

rowgroups fast enough.

You can run both example in the

sample database.

This sample runs

on all partitions.

This sample runs

on a specific partition.

Applies to:

SQL Server 2016 (13.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

The command

compresses each

and

delta rowgroup into the columnstore as a compressed rowgroup. This empties the

deltastore and forces all rows to get compressed into the columnstore. This is useful especially

after performing many insert operations since these operations store the rows in one or more

delta rowgroups.

combines rowgroups to fill rowgroups up to a maximum number of rows <=

1,024,576. Therefore, when you compress all

and

rowgroups you don't end up

with lots of compressed rowgroups that only have a few rows in them. You want rowgroups to

be as full as possible to reduce the compressed size and improve query performance.

The following examples use the

database.

This example moves all

and

delta rowgroups into the columnstore index.

### Doesn't apply to

## D. Defragment a columnstore index online

## E. Rebuild a clustered columnstore index offline

This example moves all

and

delta rowgroups into the columnstore index for a

specific partition.

: SQL Server 2012 (11.x) and SQL Server 2014 (12.x).

Starting with SQL Server 2016 (13.x),

does more than compress delta rowgroups

into the columnstore. It also performs online defragmentation. First, it reduces the size of the

columnstore by physically removing deleted rows when 10% or more of the rows in a

rowgroup have been deleted. Then, it combines rowgroups together to form larger rowgroups

that have up to the maximum of 1,024,576 rows per rowgroups. All rowgroups that are

changed get recompressed.

The following example performs a

to defragment the index by physically removing

rows that have been logically deleted from the table, and merging rowgroups.

Applies to: SQL Server, Azure SQL Database, and Azure SQL Managed Instance

７

Note

Starting with SQL Server 2016 (13.x), rebuilding a columnstore index is no longer

necessary in most situations since

physically removes deleted rows and

merges rowgroups. The

option forces all

or

delta

rowgroups into the columnstore which previously could only be done with a rebuild.

is online and occurs in the background so queries can continue as the

operation happens.

This example shows how to rebuild a clustered columnstore index and force all delta

rowgroups into the columnstore. This first step prepares a table

in the

database with a clustered columnstore index, and inserts data from the

first four columns.

The results show one

rowgroup, which means SQL Server waits for more rows to be

added before it closes the rowgroup and moves the data to the columnstore. This next

statement rebuilds the clustered columnstore index, which forces all rows into the columnstore.

The results of the

statement show the rowgroup is

, which means the

column segments of the rowgroup are now compressed and stored in the columnstore.



Tip

Starting with SQL Server 2016 (13.x) and in Azure SQL Database, we recommend using

instead of

for columnstore indexes.

７

Note

In SQL Server 2012 (11.x) and SQL Server 2014 (12.x),

is only used to compress

rowgroups into the columnstore. The only way to perform defragmentation

operations and to force all delta rowgroups into the columnstore is to rebuild the index.

### Applies to

### Doesn't apply to

## F. Rebuild a partition of a clustered columnstore index offline

## G. Change a clustered columnstore index to use archival

## compression

: SQL Server 2012 (11.x) and later versions, Azure SQL Database, and Azure SQL

Managed Instance

To rebuild a partition of a large clustered columnstore index, use

with the

partition option. This example rebuilds partition 12. Starting with SQL Server 2016 (13.x), we

recommend replacing

with

.

: SQL Server 2012 (11.x)

You can choose to reduce the size of a clustered columnstore index even further by using the

data compression option. This is practical for older data that you want to

keep on cheaper storage. We recommend only using this on data that isn't accessed often

since decompress is slower than with the normal

compression.

The following example rebuilds a clustered columnstore index to use archival compression, and

then shows how to remove the archival compression. The final result uses only columnstore

compression.

First, prepare the example by creating a table with a clustered columnstore index. Then,

compress the table further by using archival compression.

### Applies to

```sql
ALTER INDEX REORGANIZE
```

`REORGANIZE`

```sql
-- Create a database
CREATE
DATABASE
[columnstore];
GO
-- Create a rowstore staging table
CREATE
TABLE
[staging] (
AccountKey
INT
NOT
NULL
,
AccountDescription
NVARCHAR (50),
AccountType
NVARCHAR (50),
AccountCodeAlternateKey
INT
);
-- Insert 10 million rows into the staging table.
DECLARE
@
loop
INT
;
DECLARE
@AccountDescription
VARCHAR (50);
DECLARE
@AccountKey
INT
;
DECLARE
@AccountType
VARCHAR (50);
DECLARE
@AccountCode
INT
;
SELECT
@
loop
= 0
BEGIN
TRANSACTION
WHILE (@
loop
< 300000)
BEGIN
SELECT
@AccountKey =
CAST (
RAND () * 10000000
AS
INT
);
SELECT
@AccountDescription =
'accountdesc '
+
CONVERT (
VARCHAR (20), @AccountKey);
SELECT
@AccountType =
'AccountType '
+
CONVERT (
VARCHAR (20), @AccountKey);
SELECT
@AccountCode =
CAST (
RAND () * 10000000
AS
INT
);
INSERT
INTO staging
VALUES (
@AccountKey,
@AccountDescription,
@AccountType,
@AccountCode
);
SELECT
@
loop
= @
loop
+ 1;
```

```sql
INSERT INTO
```

`TABLOCK`

`OPEN`

`CLOSED`

`OPEN`

```sql
END
COMMIT
-- Create a table for the clustered columnstore index
CREATE
TABLE cci_target (
AccountKey
INT
NOT
NULL
,
AccountDescription
NVARCHAR (50),
AccountType
NVARCHAR (50),
AccountCodeAlternateKey
INT
);
-- Convert the table to a clustered columnstore index named inxcci_cci_target;
CREATE
CLUSTERED COLUMNSTORE
INDEX idxcci_cci_target
ON cci_target;
INSERT
INTO cci_target
WITH (TABLOCK)
SELECT
TOP 300000 *
FROM staging;
SELECT
*
FROM sys.dm_db_column_store_row_group_physical_stats
WHERE object_id  = object_id(
'cci_target'
);
ALTER
INDEX idxcci_cci_target
ON cci_target REORGANIZE
WITH (COMPRESS_ALL_ROW_GROUPS
=
ON
);
ALTER
INDEX idxcci_cci_target
ON cci_target REORGANIZE
WITH (COMPRESS_ALL_ROW_GROUPS
=
ON
);
```

`REORGANIZE`

`CLOSED`

`CLOSED`

`AdventureWorksDW2025`

`REORGANIZE`

`REORGANIZE`

```sql
REORGANIZE WITH (COMPRESS_ALL_ROW_GROUPS = ON)
```

`OPEN`

`CLOSED`

`REORGANIZE`

`OPEN`

`CLOSED`

`AdventureWorksDW2025`

`OPEN`

`CLOSED`

```sql
ALTER
INDEX cci_FactInternetSales2
ON
FactInternetSales2 REORGANIZE;
-- REORGANIZE a specific partition
ALTER
INDEX cci_FactInternetSales2
ON
FactInternetSales2 REORGANIZE
PARTITION
= 0;
```

`OPEN`

`CLOSED`

`REORGANIZE`

`REORGANIZE`

```sql
ALTER
INDEX cci_FactInternetSales2
ON
FactInternetSales2 REORGANIZE
WITH (COMPRESS_ALL_ROW_GROUPS =
ON
);
ALTER
INDEX cci_FactInternetSales2
ON
FactInternetSales2 REORGANIZE
PARTITION
= 0
WITH (COMPRESS_ALL_ROW_GROUPS =
ON
);
```

`REORGANIZE`

`COMPRESS_ALL_ROW_GROUPS`

`OPEN`

`CLOSED`

`REORGANIZE`

```sql
ALTER
INDEX cci_FactInternetSales2
ON
FactInternetSales2 REORGANIZE;
```

`FactInternetSales2`

`AdventureWorksDW2025`

`OPEN`

`SELECT`

`COMPRESSED`

```sql
ALTER INDEX REORGANIZE
```

```sql
ALTER INDEX REBUILD
```

`REORGANIZE`

`CLOSED`

```sql
CREATE
TABLE dbo.FactInternetSales2 (
ProductKey [
int
]
NOT
NULL
,
OrderDateKey [
int
]
NOT
NULL
,
DueDateKey [
int
]
NOT
NULL
,
ShipDateKey [
int
]
NOT
NULL
);
CREATE
CLUSTERED COLUMNSTORE
INDEX cci_FactInternetSales2
ON dbo.FactInternetSales2;
INSERT
INTO dbo.FactInternetSales2
SELECT
ProductKey, OrderDateKey, DueDateKey, ShipDateKey
FROM dbo.FactInternetSales;
SELECT
*
FROM sys.column_store_row_groups;
ALTER
INDEX cci_FactInternetSales2
ON
FactInternetSales2
REBUILD
;
SELECT
*
FROM sys.column_store_row_groups;
```

```sql
ALTER INDEX REBUILD
```

`REBUILD`

`REORGANIZE`

`COLUMNSTORE_ARCHIVE`

`COLUMNSTORE`

```sql
ALTER
INDEX cci_fact3
ON fact3
REBUILD
PARTITION
= 12;
```

```sql
--Prepare the example by creating a table with a clustered columnstore index.
CREATE
TABLE
SimpleTable (
ProductKey [
int
]
NOT
NULL
,
OrderDateKey [
int
]
NOT
NULL
,
DueDateKey [
int
]
NOT
NULL
,
ShipDateKey [
int
]
NOT
NULL
);
CREATE
CLUSTERED
INDEX cci_SimpleTable
ON
SimpleTable (ProductKey);
CREATE
CLUSTERED COLUMNSTORE
INDEX cci_SimpleTable
ON
SimpleTable
```
