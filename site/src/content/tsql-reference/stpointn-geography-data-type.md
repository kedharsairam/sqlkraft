---
name: "STPointN (geography Data Type)"
title: "STPointN (geography Data Type)"
category: "data-types"
description: "Returns the specified point from a geography instance."
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---
## Syntax

```sql
.STPointN ( n )
```

## Return Type

geography

## Arguments

### n

An int expression between 1 and the number of points in the geography instance.

## Remarks

Returns the specified point from a geography instance.

## Examples

```sql
DECLARE @g geography = geography::STGeomFromText('LINESTRING(-122.360 47.656, -122.343 47.656)', 4326);
SELECT @g.STPointN(1).ToString();
```
