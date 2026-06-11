---
name: "sys.dm_exec_query_profiles"
title: "sys.dm_exec_query_profiles"
category: "execution"
description: "SQL database in Microsoft Fabric Monitors real time query progress while the query is in execution. For example, use this DMV to determine which part of the query is running slow. Join this DMV with other system DMVs using the columns identified in the description field. Or, join this DMV with other performance counters (such as Performance Monitor, xperf) by using the timestamp columns."
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: "SET STATISTICS XML ON"
---

## Description

SQL database in Microsoft Fabric Monitors real time query progress while the query is in execution. For example, use this DMV to determine which part of the query is running slow. Join this DMV with other system DMVs using the columns identified in the description field. Or, join this DMV with other performance counters (such as Performance Monitor, xperf) by using the timestamp columns. The counters returned are per operator per thread. The results are dynamic and do not match

## Syntax

```sql
SET STATISTICS XML ON
```
