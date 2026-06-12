---
name: "STGeometryN (geometry Data Type)"
title: "STGeometryN (geometry Data Type)"
category: "data-types"
description: "Returns the specified geometry from a geometry collection."
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---
## Syntax

```sql.STGeometryN ( n )
```

## Return Type

geometry

## Arguments

### n

An int expression between 1 and the number of geometries in the geometry collection.

## Remarks

Returns the specified geometry from a geometry collection.

## Examples

```sql
DECLARE @g geometry = geometry::STGeomFromText('GEOMETRYCOLLECTION(POINT(1 1), LINESTRING(0 0, 2 2))', 0);
SELECT @g.STGeometryN(1).ToString();
```
