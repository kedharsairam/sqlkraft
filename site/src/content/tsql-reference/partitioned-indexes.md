---
name: "Partitioned indexes"
title: "Partitioned indexes"
category: "statements"
description: "sorting and a temporary copy of the original table or existing clustered index data."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

sorting and a temporary copy of the original table or existing clustered index data. For more

information about clustered indexes, see

Create clustered indexes

and the

index

architecture and design guide.

Starting with SQL Server 2016 (13.x), in Azure SQL Database, SQL database in Microsoft Fabric,

and in Azure SQL Managed Instance, you can create a nonclustered index on a table stored as

a clustered columnstore index. If you first create a nonclustered index on a table stored as a

heap or clustered index, the index persists if you later convert the table to a clustered

columnstore index. It is also not necessary to drop the nonclustered index when you rebuild

the clustered columnstore index.

The

option isn't valid when you create a nonclustered index on a table stored as

a clustered columnstore index.

When a unique index exists, the Database Engine checks for duplicate values each time data is

added or modified. Operations that would generate duplicate key values are rolled back, and

the Database Engine returns an error message. This is true even if the data addition or

modification operation changes many rows but causes only one duplicate. If an attempt is

made to insert rows when there is a unique index with the

option set to

,

the rows violating the unique index are ignored.

Partitioned indexes are created and maintained in a similar manner to partitioned tables, but

like ordinary indexes, they are handled as separate database objects. You can have a

partitioned index on a table that isn't partitioned, and you can have a nonpartitioned index on

a table that is partitioned.

If you are creating an index on a partitioned table, and don't specify a filegroup on which to

place the index, the index is partitioned in the same manner as the underlying table. This is

because indexes, by default, are placed on the same filegroups as their underlying tables, and

for a partitioned table in the same partition scheme that uses the same partitioning columns.

When the index uses the same partition scheme and partitioning column as the table, the index

is

aligned

with the table.

２

Warning

### Required value

#### option

#### Required

#### Default

#### server value

#### Default OLE DB

#### and ODBC value

#### Default DB-

#### Library value

`FILESTREAM_ON`

`IGNORE_DUP_KEY`

`ON`
