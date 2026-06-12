---
title: "LineString"
topic: "spatial-data"
description: "SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric A is a one-dimen"
tags: ["spatial-data","linestring"]
pubDate: 2025-12-01
---

database in Microsoft Fabric

A

is a one-dimensional object representing a sequence of points and the line

segments connecting them in SQL Database Engine spatial data.

The following illustration shows examples of

instances.

As shown in the illustration:

Figure 1 is a simple, nonclosed

instance.

Figure 2 is a nonsimple, nonclosed

instance.

Figure 3 is a closed, simple

instance, and therefore is a ring.

Figure 4 is a closed, nonsimple

instance, and therefore is not a ring.

Accepted

instances can be input into a geometry variable, but they might not be

valid

instances. The following criteria must be met for a

instance to be

accepted. The instance must be formed of at least two points or it must be empty. The

following LineString instances are accepted.

shows that a

instance can be accepted, but not valid.

```sql
@g3
DECLARE
@g1 geometry =
'LINESTRING EMPTY'
;
DECLARE
@g2 geometry =
'LINESTRING(1 1,2 3,4 8, -6 3)'
;
DECLARE
@g3 geometry =
'LINESTRING(1 1, 1 1)'
;
```
