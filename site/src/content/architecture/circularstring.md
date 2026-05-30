---
title: "CircularString"
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
  - "circularstring"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

A

is a collection of zero or more continuous circular arc segments. A circular arc

segment is a curved segment defined by three points in a two-dimensional plane; the first

point cannot be the same as the third point. If all three points of a circular arc segment are

collinear, the arc segment is treated as a line segment.

The drawing below shows valid

instances:

A

instance is accepted if it is either empty or contains an odd number of points,

n, where n > 1. The following

instances are accepted.

shows that

instance might be accepted, but not valid. The following

CircularString instance declaration is not accepted. This declaration throws a

.

```sql
@g3
System.FormatException
DECLARE
@g1 geometry =
'CIRCULARSTRING EMPTY'
;
DECLARE
@g2 geometry =
'CIRCULARSTRING(1 1, 2 0, -1 1)'
;
DECLARE
@g3 geometry =
'CIRCULARSTRING(1 1, 2 0, 2 0, 2 0, 1 1)'
;
DECLARE
@g geometry =
'CIRCULARSTRING(1 1, 2 0, 2 0, 1 1)'
;
```
