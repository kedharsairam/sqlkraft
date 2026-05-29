---
name: 'sys.query_store_wait_stats'
title: 'sys.query_store_wait_stats'
category: 'query-store'
description: 'SQL Server 2017 (14.x) and later versions Contains information about the wait information for the query. Identifier of the row representing wait statistics for the plan_id, runtime_stats_interval_id, execution_type and wait_category. It is unique only for the past runtime statistics intervals. For the currently active interval, there may be multiple rows representing wait statistics for the plan r'
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
---

## Description

SQL Server 2017 (14.x) and later versions Contains information about the wait information for the query. Identifier of the row representing wait statistics for the plan_id, runtime_stats_interval_id, execution_type and wait_category. It is unique only for the past runtime statistics intervals. For the currently active interval, there may be multiple rows representing wait statistics for the plan referenced by plan_id, with the execution type
