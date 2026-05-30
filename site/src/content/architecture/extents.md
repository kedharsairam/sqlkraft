---
title: "Extents"
topic: "query-processing"
description: "The index key of a clustered index can't contain"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

The index key of a clustered index can't contain

columns that have data in a

allocation unit. If a clustered index is created on a

column and

all existing data is in a

allocation unit, but a subsequent

or

statement pushes the data off-row, the statement fails. For more information, see

Index

architecture and design guide

.

You can include columns that contain row-overflow data as key or nonkey columns of a

nonclustered index.

The row size limit for tables that use

sparse columns

is 8,018 bytes. During conversion

between sparse and nonsparse columns, when the converted data plus existing data

exceeds 8,018 bytes,

error 576

is returned. When columns are converted between sparse

and nonsparse types, the Database Engine keeps a copy of the current row data. This

temporarily doubles the storage that is required for the row.

To obtain information about tables or indexes that might contain row-overflow data, use

the

sys.dm_db_index_physical_stats

dynamic management function. An index or partition

has row-overflow data if the function returns rows where the

column is

and the

column is greater than 0.

An extent is a collection of eight physically contiguous pages. The size of each extent is 64 KiB.

There are two types of extents:

extents are owned by a single object, for example a single table; all eight pages

in the extent can only be used by the owning object.

extents are shared by up to eight objects. Each of the eight pages in the extent can

be owned by a different object.

Up to, and including, SQL Server 2014 (12.x), the Database Engine doesn't allocate uniform

extents to tables with small amounts of data. A new heap or index allocates pages from mixed

extents. When the heap or index grows to the point that it uses eight pages, it then switches to

uniform extents for all subsequent allocations. If you create an index on an existing table that

has enough rows to generate eight pages in the index, all allocations to the index are in

uniform extents.

Starting with SQL Server 2016 (13.x), the Database Engine uses uniform extents for allocations

in a user database and in

, except for allocations belonging to the first eight pages of an

IAM chain

. Allocations in the

,

, and

databases still retain the previous

behavior.

Up to and including SQL Server 2014 (12.x), you can use trace flag (TF) 1118 to change the

default allocation to always use uniform extents. For more information about this trace flag, see

trace flag 1118

.

Starting with SQL Server 2016 (13.x), TF 1118 has no effect. The functionality provided by TF

1118 earlier is automatically enabled for all user databases and for

. For user databases,

this behavior can be controlled by the

database option. The default

value is

, which means that uniform extents are used. For more information, see

ALTER

DATABASE SET options

.

Starting with SQL Server 2012 (11.x), the

system function

can report page allocation information for a database, table, index, and partition.

）

Important

### Global Allocation Map (GAM)

### Shared Global Allocation Map (SGAM)

`ROW_OVERFLOW_DATA`

`IN_ROW_DATA`

`INSERT`

`UPDATE`

`alloc_unit_type_desc`

`ROW_OVERFLOW_DATA`

`page_count`

`tempdb`

`master`

`msdb`

`model`

`tempdb`

`MIXED_PAGE_ALLOCATION`

`OFF`

`sys.dm_db_database_page_allocations`
