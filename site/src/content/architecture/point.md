---
title: "Point"
topic: "spatial-data"
description: ""
tags: ["spatial-data","point"]
pubDate: "2025-12-01"
---

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

In SQL Server spatial data, a

is a 0-dimensional object representing a single location and

can contain Z (elevation) and M (measure) values.

The

type for the

data type represents a single location where

Lat

represents

latitude and

Long

represents longitude. The values for latitude and longitude are measured in

degrees. Values for latitude always lie in the interval [-90, 90], and values that are inputted

outside this range will throw an exception. Values for longitude always lie in the interval (-180,

180], and values inputted outside this range are wrapped around to fit in this range. For

example, if 190 is inputted for longitude, then it will be wrapped to the value -170.

SRID

represents the spatial reference ID of the

instance that you wish to return.

The

type for the

data type represents a single location where

X

represents the

X-coordinate of the Point being generated and

Y

represents the Y-coordinate of the Point

being generated.

SRID

represents the spatial reference ID of the

instance that you

wish to return.

The following example creates a geometry Point instance representing the point

with

an SRID of.

```sql
(3, 4)
0
DECLARE
@g geometry;
SET
@g = geometry::STGeomFromText(
'POINT (3 4)'
, 0);
```
