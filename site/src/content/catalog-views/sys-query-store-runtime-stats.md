---
name: "sys.query_store_runtime_stats"
title: "sys.query_store_runtime_stats"
category: "query-store"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about the runtime execution statistics information for the query."
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  LEFT
  JOIN
  sys.query_store_runtime_stats qsrs
  ON
  qspl.plan_id = qsrs.plan_id
  LEFT
  JOIN
  sys.query_store_runtime_stats_interval qsrsi
  ON
  qsrs.runtime_stats_interval_id = qsrsi.runtime_stats_interval_id
  WHERE
  qspl.plan_type = 1
  or
  qspl.plan_type = 2
  ORDER
  BY
  qspl.query_id, qsrs.last_execution_time;
  GO
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about the runtime execution statistics information for the query.

## Syntax

```sql
LEFT
JOIN sys.query_store_runtime_stats qsrs
ON qspl.plan_id = qsrs.plan_id
LEFT
JOIN sys.query_store_runtime_stats_interval qsrsi
ON qsrs.runtime_stats_interval_id = qsrsi.runtime_stats_interval_id
WHERE qspl.plan_type = 1 or qspl.plan_type = 2
ORDER
BY qspl.query_id, qsrs.last_execution_time;
GO
```
