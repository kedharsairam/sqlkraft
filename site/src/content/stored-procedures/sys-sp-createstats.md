---
name: "sys.sp_createstats"
title: "sp_createstats"
category: "general"
description: "SQL database in Microsoft Fabric statement to create single-column statistics on columns that aren't already the first column in a statistics object. Creating single-column statistics increases the number of histograms, which can improve cardinality estimates, query plans, and query performance. The first column of a statistics object has a histogram; other columns don't have is useful for applica"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "AUTO_CREATE_STATISTICS"
---

## Description

SQL database in Microsoft Fabric statement to create single-column statistics on columns that aren't already the first column in a statistics object. Creating single-column statistics increases the number of histograms, which can improve cardinality estimates, query plans, and query performance. The first column of a statistics object has a histogram; other columns don't have is useful for applications such as benchmarking when query execution times

## Syntax

```sql
AUTO_CREATE_STATISTICS
```
