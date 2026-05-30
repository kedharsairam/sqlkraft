---
name: "instance with an inscribed Polygon instance"
title: "Instance with an inscribed Polygon instance"
category: "queries"
description: "The following example uses"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

The following example uses

to compute the symmetric difference of two

instances.

SQL

The following example returns a

that represents the symmetric difference

between a

and a

.

SQL

The following example returns a

instance with an interior

ring that

represents the symmetric difference between the two instances compared.

SQL

OGC Methods on Geometry Instances

Last updated on 11/18/2025

See Also

```sql
STSymDifference()
```

```sql
Polygon
```

```sql
GeometryCollection
```

```sql
CurvePolygon
```

```sql
Polygon
```

```sql
CurvePolygon
```

```sql
Polygon
```

```sql
DECLARE
@g geometry;
DECLARE
@h geometry;
SET
@g = geometry::STGeomFromText(
'POLYGON((0 0, 0 2, 2 2, 2 0, 0 0))'
, 0);
SET
@h = geometry::STGeomFromText(
'POLYGON((1 1, 3 1, 3 3, 1 3, 1 1))'
, 0);
SELECT
@g.STSymDifference(@h).ToString();
```

```sql
DECLARE
@g geometry =
'CURVEPOLYGON (CIRCULARSTRING (0 -4, 4 0, 0 4, -4 0, 0 -4))'
;
DECLARE
@h geometry =
'POLYGON ((1 -1, 5 -1, 5 3, 1 3, 1 -1))'
;
SELECT
@h.STSymDifference(@g).ToString();
```

```sql
DECLARE
@g geometry =
'CURVEPOLYGON (CIRCULARSTRING (0 -4, 4 0, 0 4, -4 0, 0 -4))'
;
DECLARE
@h geometry =
'POLYGON ((1 -1, 2 -1, 2 1, 1 1, 1 -1))'
;
SELECT
@h.STSymDifference(@g).ToString();
```
