---
name: "Point (geometry Data Type)"
title: "Point (geometry Data Type)"
category: "data-types"
description: "The following example uses"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

The following example uses to create a instance.

SQL

STGeomFromText

Extended Static Geometry Methods

See Also

geometry

Point

float

Point

float

Point

int

geometry

geometry

```sql
Parse()
```

```sql
geometry
```

```sql
DECLARE
@g geometry;
SET
@g = geometry::
Parse
(
'LINESTRING (100 100, 20 180, 180 180)'
);
SELECT
@g.ToString();
```
