---
name: "sys.dm_exec_background_job_queue_stats"
title: "sys.dm_exec_background_job_queue_stats"
category: "execution"
description: "Analytics Platform System (PDW) Returns a row that provides aggregate statistics for each query processor job submitted for asynchronous (background) execution. Number of requests successfully posted to the queue. Number of requests that started execution. Number of requests serviced to either success or failure."
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: |
  FROM sys.dm_exec_background_job_queue_stats;
  GO
---

## Description

Analytics Platform System (PDW) Returns a row that provides aggregate statistics for each query processor job submitted for asynchronous (background) execution. Number of requests successfully posted to the queue. Number of requests that started execution. Number of requests serviced to either success or failure. Number of requests that failed due to lock contention or Number of requests that failed due to other reasons.

## Syntax

```sql
FROM sys.dm_exec_background_job_queue_stats;
GO
```
