---
name: 'sys.fn_has_change_feed_permissions'
title: 'sys.fn_has_change_feed_permissions'
category: 'system'
description: 'SQL Server 2022 (16.x) and later versions'
tags: ["function"]
pubDate: 2026-05-29
---

The percentage of the table that is used. Valid values are from 0 to 100.

@sample

is

, with a

default of

.

A table value is returned. The following grid describes the column contents of the table.


## Description
Represents the Unique ID of each cell, with a starting count of 1.

A rectangular polygon that represents each cell. Cell shape is identical to the

cell shape used for the spatial indexing.

Indicates the number of spatial objects that are touching or containing the cell.

User must be a member of the

fixed server role.

SQL Server Management Studio (SSMS) spatial tab shows a graphical representation of the

results. You can query the results against the spatial window to get an approximate number of

result items.

The bounding box for the

type is the entire globe.

The following example calls

on the

table in

the AdventureWorks2025 database.

ﾉ

Expand table

７

Note

Objects in the table might cover more than one cell, so the sum of the cells in the table

might be larger than the number of actual objects.

SQL

Spatial index stored procedures - arguments and properties

Last updated on 04/24/2026

Related content

```sql
100
```

```sql
cellid
```

```sql
cell
```

```sql
row_count
```

```sql
sp_help_spatial_geography_histogram
```

```sql
Person.Address
```

```sql
EXECUTE
sp_help_spatial_geography_histogram
@tabname = N
'Person.Address'
,
@colname = N
'SpatialLocation'
,
@resolution = 64,
@
sample
= 30;
```
