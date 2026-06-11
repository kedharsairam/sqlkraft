---
name: "GeomFromGML (geography Data Type)"
title: "GeomFromGml (geography Data Type)"
category: "data-types"
description: "Constructs a geography instance from a GML representation."
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---
## Syntax

```sql
GeomFromGml ( GmlText, SRID )
```

## Return Type

geography

## Arguments

### GmlText

An XML input that represents the GML (Geography Markup Language) format.

### SRID

An int expression representing the spatial reference ID.

## Remarks

Constructs a geography instance from a GML representation.
