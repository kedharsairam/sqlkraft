---
name: "SET FMTONLY"
title: "SET FMTONLY"
category: "statements"
description: "Controls whether metadata-only mode is active for query results."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---
## Syntax

```sql
SET FMTONLY { ON | OFF }
```

## Arguments

### ON

Only metadata is returned; no actual rows are processed.

### OFF

Full results including data rows are returned (default).

## Remarks

SET FMTONLY ON is commonly used in client applications to retrieve column metadata without executing the full query. This setting is deprecated and should be replaced with sp_describe_first_result_set.

## Examples

```sql
-- Enable FMTONLY to retrieve only metadata
SET FMTONLY ON;
SELECT * FROM sys.objects;
SET FMTONLY OFF;
```
