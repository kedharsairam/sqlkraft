---
name: "CollectionAggregate (geometry Data Type)"
title: "CollectionAggregate (geometry Data Type)"
category: "data-types"
description: "Returns a geometry instance from a collection of geometry types."
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---
## Syntax

```sql
CollectionAggregate ( geometry_collection )
```

## Return Type

geometry

## Arguments

### geometry_collection

A geometry collection instance.

## Remarks

Returns a geometry instance from a collection of geometry types.

## Examples

```sql
-- Create a geometry collection and aggregate
DECLARE @g geometry = geometry::STGeomFromText('GEOMETRYCOLLECTION(POINT(1 1), LINESTRING(0 0, 2 2))', 0);
```
