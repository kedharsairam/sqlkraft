---
title: "GeometryCollection"
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

  A

  is a collectio
tags:
  - "spatial-data"
  - "geometrycollection"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

A

is a collection of zero or more

or

instances. A

can be empty.

For a

instance to be accepted, it must either be an empty

instance or all the instances comprising the

instance

must be accepted instances. The following example shows accepted instances.

The following example throws a

because the

instance in

the

instance is not accepted.

A

instance is valid when all instances that comprise the

instance are valid. The following shows three valid

instances and one instance that is not valid.

```sql
System.FormatException
DECLARE
@g1 geometry =
'GEOMETRYCOLLECTION EMPTY'
;
DECLARE
@g2 geometry =
'GEOMETRYCOLLECTION(LINESTRING EMPTY,POLYGON((-1 -1, -1 -5,
-5 -5, -5 -1, -1 -1)))'
;
DECLARE
@g3 geometry =
'GEOMETRYCOLLECTION(LINESTRING(1 1, 3 5),POLYGON((-1 -1, -1
-5, -5 -5, -5 -1, -1 -1)))'
;
DECLARE
@g geometry =
'GEOMETRYCOLLECTION(LINESTRING(1 1), POLYGON((-1 -1, -1 -5, -5
-5, -5 -1, -1 -1)))'
;
DECLARE
@g1 geometry =
'GEOMETRYCOLLECTION EMPTY'
;
DECLARE
@g2 geometry =
'GEOMETRYCOLLECTION(LINESTRING EMPTY,POLYGON((-1 -1, -1 -5,
```
