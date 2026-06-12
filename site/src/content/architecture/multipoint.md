---
title: "MultiPoint"
topic: "spatial-data"
description: "SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric A is a collectio"
tags: ["spatial-data","multipoint"]
pubDate: 2025-12-01
---

database in Microsoft Fabric

A

is a collection of zero or more points. The boundary of a

instance is

empty.

The following example creates a

instance with SRID 23 and two points:

one point with the coordinates (2, 3), one point with the coordinates (7, 8), and a Z value of 9.5.

The following example expresses the

instance using.

The following example uses the method

to retrieve a description of the first

point in the collection.

```sql
geometry MultiPoint
MultiPoint
STMPointFromText()
STGeometryN()
DECLARE
@g geometry;
SET
@g = geometry::STGeomFromText(
'MULTIPOINT((2 3), (7 8 9.5))'
, 23);
DECLARE
@g geometry;
SET
@g = geometry::STMPointFromText(
'MULTIPOINT((2 3), (7 8 9.5))'
, 23);
SELECT
@g.STGeometryN(1).STAsText();
```
