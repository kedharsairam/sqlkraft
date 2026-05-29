---
name: "Extended methods on geography instances"
title: "Extended methods on geography instances"
category: "queries"
description: "### Extended methods"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

### geography

### OGC methods

### Extended methods

#### Method

```sql
DECLARE @g geography;
DECLARE @h geography;
SET @g = geography::Parse('POLYGON ((-120.533 46.566, -118.283 46.1, -122.3 47.45,
-120.533 46.566))');
SET @h = geography::Parse('CURVEPOLYGON (COMPOUNDCURVE (CIRCULARSTRING
(-122.200928 47.454094, -122.810669 47.00648, -122.942505 46.687131, -121.14624
45.786679, -119.119263 46.183634), (-119.119263 46.183634, -119.273071 47.107523),
CIRCULARSTRING (-119.273071 47.107523, -120.640869 47.569114, -122.200928
47.454094)))');
SELECT @g.STWithin(@h);
```
