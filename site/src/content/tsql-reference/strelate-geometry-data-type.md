---
name: "STRelate (geometry Data Type)"
title: "STRelate (geometry Data Type)"
category: "data-types"
description: "Returns true if the geometry instance is spatially related to another geometry according to the specified DE-9IM intersection pattern."
tags: ["tsql","data-types"]
pubDate: "2026-05-29"
---
## Syntax

```sql.STRelate ( other_geometry, intersection_pattern )
```

## Return Type

bit

## Arguments

### other_geometry

Another geometry instance to compare.

### intersection_pattern

A character string representing the DE-9IM intersection pattern.

## Remarks

Returns true if the geometry instance is spatially related to another geometry according to the specified DE-9IM intersection pattern.

## Examples

```sql
DECLARE @g1 geometry = geometry::STGeomFromText('POLYGON((0 0, 2 0, 2 2, 0 2, 0 0))', 0);
DECLARE @g2 geometry = geometry::STGeomFromText('POLYGON((1 1, 3 1, 3 3, 1 3, 1 1))', 0);
SELECT @g1.STRelate(@g2, 'T*T***T**') AS AreIntersecting;
```
