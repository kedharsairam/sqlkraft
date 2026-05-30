---
name: "sys.dm_exec_query_stats"
title: "sys.dm_exec_query_stats"
category: "execution"
description: "SQL database in Microsoft Fabric Returns aggregate performance statistics for cached query plans in SQL Server. The view contains one row per query statement within the cached plan, and the lifetime of the rows are tied to the plan itself. When a plan is removed from the cache, the corresponding rows are can vary with each execution as the data only reflects finished queries, and not ones still in"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_exec_query_stats"
---

## Description

SQL database in Microsoft Fabric Returns aggregate performance statistics for cached query plans in SQL Server. The view contains one row per query statement within the cached plan, and the lifetime of the rows are tied to the plan itself. When a plan is removed from the cache, the corresponding rows are can vary with each execution as the data only reflects finished queries, and not ones still in-flight.

## Syntax

`sys.dm_exec_query_stats`
