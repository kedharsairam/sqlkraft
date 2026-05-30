---
name: "STNumGeometries (geometry Data Type)"
title: "STNumGeometries (geometry Data Type)"
category: "data-types"
description: "Returns the number of geometries in a geometry collection."
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---
## Syntax

```sql
.STNumGeometries ( )
```

## Return Type

int

## Remarks

Returns the number of geometries in a geometry collection.

## Examples

```sql
DECLARE @g geometry = geometry::STGeomFromText('MULTIPOINT((1 1), (2 2))', 0);
SELECT @g.STNumGeometries() AS NumberOfGeometries;
```
