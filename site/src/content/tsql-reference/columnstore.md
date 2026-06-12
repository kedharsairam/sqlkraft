---
name: "columnstore"
title: "Columnstore"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## A. Convert a heap to a clustered columnstore index

## B. Convert a clustered index to a clustered columnstore index

## with the same name

This example creates a table as a heap, and then converts it to a clustered columnstore index

named. The creation of the clustered columnstore index changes the storage for

the entire table from rowstore to columnstore.

This example creates a table with clustered index, and then demonstrates the syntax of

converting the clustered index to a clustered columnstore index. The creation of the clustered

columnstore index changes the storage for the entire table from rowstore to columnstore.

## C. Handle nonclustered indexes when converting a rowstore

## table to a columnstore index

This example shows how to handle nonclustered indexes when you convert a rowstore table to

a columnstore index. Beginning with SQL Server 2016 (13.x), no special action is required. SQL

Server automatically defines and rebuilds the nonclustered indexes on the new, clustered

columnstore index.

If you want to drop the nonclustered indexes, use the DROP INDEX statement before creating

the columnstore index. The DROP EXISTING option only drops the clustered index that is being

converted. It doesn't drop the nonclustered indexes.

In SQL Server 2012 (11.x) and SQL Server 2014 (12.x), you can't create a nonclustered index on

a columnstore index.

Only for SQL Server 2012 (11.x) and SQL Server 2014 (12.x), you must drop the nonclustered

indexes in order to create the columnstore index.

## D. Convert a large fact table from rowstore to columnstore

This example explains how to convert a large fact table from a rowstore table to a columnstore

table.

1. Create a small table to use in this example.

2. Drop all nonclustered indexes from the rowstore table. You might want to

script out the

indexes to re-create them later.

3. Convert the rowstore table to a columnstore table with a clustered columnstore index.

First, look up the name of the existing clustered rowstore index. In Step 1, we set the

name of the index to. If the index name wasn't specified, it was given

an automatically generated unique index name. You can retrieve the automatically

generated name with the following sample query:

## E. Convert a columnstore table to a rowstore table with a

## clustered index

## F. Convert a columnstore table to a rowstore heap

Option 1: Drop the existing clustered index

, and convert

to columnstore. Change the name of the new clustered columnstore index.

Option 2: Convert to columnstore, and reuse the existing rowstore clustered index name.

To convert a columnstore table to a rowstore table with a clustered index, use the

statement with the

option.

To convert a columnstore table to a rowstore heap, drop the clustered columnstore index. This

isn't typically recommended, but can some have narrow uses. For more information about

heaps, see

Heaps (tables without clustered indexes).

## G. Defragment by reorganizing the columnstore index

`cci_Simple`

```sql
CREATE
TABLE dbo.SimpleTable (
ProductKey
INT
NOT
NULL
,
OrderDateKey
INT
NOT
NULL
,
DueDateKey
INT
NOT
NULL
,
ShipDateKey
INT
NOT
NULL
);
GO
CREATE
CLUSTERED COLUMNSTORE
INDEX cci_Simple
ON dbo.SimpleTable;
GO
```

```sql
CREATE
TABLE dbo.SimpleTable2 (
ProductKey
INT
NOT
NULL
,
OrderDateKey
INT
NOT
NULL
,
DueDateKey
INT
NOT
NULL
,
ShipDateKey
INT
NOT
NULL
);
GO
CREATE
CLUSTERED
INDEX cl_simple
ON dbo.SimpleTable2(ProductKey);
GO
```

```sql
CREATE
CLUSTERED COLUMNSTORE
INDEX cl_simple
ON dbo.SimpleTable2
WITH (DROP_EXISTING =
ON
);
GO
```

```sql
--Create the table for use with this example.
CREATE
TABLE dbo.SimpleTable (
ProductKey
INT
NOT
NULL
,
OrderDateKey
INT
NOT
NULL
,
DueDateKey
INT
NOT
NULL
,
ShipDateKey
INT
NOT
NULL
);
GO
--Create two nonclustered indexes for use with this example
CREATE
INDEX nc1_simple
ON dbo.SimpleTable(OrderDateKey);
CREATE
INDEX nc2_simple
ON dbo.SimpleTable(DueDateKey);
GO
DROP
INDEX dbo.SimpleTable.nc1_simple;
DROP
INDEX dbo.SimpleTable.nc2_simple;
--Convert the rowstore table to a columnstore index.
CREATE
CLUSTERED COLUMNSTORE
INDEX cci_simple
```

`IDX_CL_MyFactTable`

```sql
ON dbo.SimpleTable;
GO
```

```sql
--Create a rowstore table with a clustered index and a nonclustered index.
CREATE
TABLE dbo.MyFactTable (
ProductKey
INT
NOT
NULL
,
OrderDateKey
INT
NOT
NULL
,
DueDateKey
INT
NOT
NULL
,
ShipDateKey
INT
NOT
NULL
INDEX
IDX_CL_MyFactTable CLUSTERED (ProductKey)
);
--Add a nonclustered index.
CREATE
INDEX my_index
ON dbo.MyFactTable(ProductKey, OrderDateKey);
--Drop all nonclustered indexes
DROP
INDEX my_index
ON dbo.MyFactTable;
SELECT i.object_id,
i.name,
t.object_id,
t.name
FROM sys.indexes
AS i
```

`IDX_CL_MyFactTable`

`MyFactTable`

```sql
CREATE
INDEX
```

`DROP_EXISTING`

```sql
INNER
JOIN sys.tables
AS t
ON i.object_id = t.object_id
WHERE i.type_desc =
'CLUSTERED'
AND t.name =
'MyFactTable'
;
--Drop the clustered rowstore index.
DROP
INDEX
[IDX_CL_MyFactTable]
ON dbo.MyFactTable;
GO
--Create a new clustered columnstore index with the name MyCCI.
CREATE
CLUSTERED COLUMNSTORE
INDEX
IDX_CCL_MyFactTable
ON dbo.MyFactTable;
GO
--Create the clustered columnstore index,
--replacing the existing rowstore clustered index of the same name
CREATE
CLUSTERED COLUMNSTORE
INDEX
[IDX_CL_MyFactTable]
ON dbo.MyFactTable
WITH (DROP_EXISTING =
ON
);
```

```sql
CREATE
CLUSTERED
INDEX
[IDX_CL_MyFactTable]
ON dbo.[MyFactTable](ProductKey)
WITH (DROP_EXISTING =
ON
);
```
