---
name: "FULLTEXTSERVICEPROPERTY"
title: "FULLTEXTSERVICEPROPERTY"
category: "statements"
description: "Returns information about Full-Text Search service-level properties."
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---
## Syntax

```sql
FULLTEXTSERVICEPROPERTY ( 'property' )
```

## Return Type

int

## Property Descriptions

| Property | Return Type | Description |
|----------|-------------|-------------|
| ResourceUsage | int | Resource usage for full-text indexing. |
| ConnectTimeout | int | Connection timeout for full-text service. |
| DataTimeout | int | Data timeout for full-text service. |

## Remarks

Returns information about Full-Text Search service-level properties.

## Example

```sql
SELECT FULLTEXTSERVICEPROPERTY('database_name', 'ResourceUsage') AS ResourceUsage;
```
