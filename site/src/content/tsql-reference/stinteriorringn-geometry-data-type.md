---
name: "STInteriorRingN (geometry Data Type)"
title: "STInteriorRingN (geometry Data Type)"
category: "data-types"
description: "Returns the specified interior ring of a polygon geometry instance."
tags: ["tsql","data-types"]
pubDate: 2026-05-29
---
## Syntax

```sql.STInteriorRingN ( n )
```

## Return Type

geometry

## Arguments

### n

An int expression between 1 and the number of interior rings in the polygon.

## Remarks

Returns the specified interior ring of a polygon geometry instance.

## Examples

```sql
DECLARE @g geometry = geometry::STGeomFromText('POLYGON((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 1 2, 2 2, 2 1, 1 1))', 0);
SELECT @g.STInteriorRingN(1).ToString();
```
