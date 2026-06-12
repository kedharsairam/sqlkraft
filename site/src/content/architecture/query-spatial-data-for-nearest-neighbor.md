---
title: "Query Spatial Data for Nearest Neighbor"
topic: "spatial-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL analytics endpoint in Microsoft Fabric

  Warehouse in Microsoft Fabric

  SQL

  database in Microsoft Fabric

  A common query us
tags:
  - "spatial-data"
  - "query-spatial-data-for-nearest-neighbor"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

A common query used with spatial data is the nearest neighbor query. Nearest neighbor

queries are used to find the closest spatial objects to a specific spatial object. For example, a

store locator for a web site often must find the closest store locations to a customer location.

A nearest neighbor query can be written in various valid query formats, but for the nearest

neighbor query to use a spatial index the following syntax must be used.

In SQL Server,

and

clauses are used to perform a nearest neighbor query on

spatial data columns. The

clause contains a call to the

method for the

spatial column data type. The

clause indicates the number of objects to return for the

query.

```sql
TOP
ORDER BY
ORDER BY
STDistance()
TOP
SELECT
TOP ( number )
[
WITH
TIES
]
[ * | expression ]
[,.]
FROM spatial_table_reference,.
[
WITH (
[
INDEX ( index_ref ) ]
[ ,
SPATIAL
_
WINDOW
_
MAX
_
CELLS
=
<value>
]
[ ,. ]
)
]
WHERE column_ref.
STD istance ( @spatial_ object )
{
[
IS
NOT
NULL
] | [
< const ] | [ >
const ]
| [
<= const ] | [ >
= const ] | [
<>
const ] ]
}
[
AND
{ other_predicate } ]
}
ORDER
BY column_ref.
STD istance ( @spatial_ object ) [ ,.n ]
[ ; ]
```
