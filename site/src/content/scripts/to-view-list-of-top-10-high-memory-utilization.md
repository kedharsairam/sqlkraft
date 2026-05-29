---
name: 'To View List of Top 10 High Memory Utilization'
title: 'To View List of Top 10 High Memory Utilization'
description: 'SQL Server diagnostic script for architecture operations.'
category: architecture
tags: ["architecture", "memory"]
pubDate: 2025-03-15
---

```sql
SELECT mg.session_id,mg.granted_memory_kb,mg.requested_memory_kb,mg.ideal_memory_kb,mg.request_time,mg.grant_time,mg.query_cost,mg.dop,st.[TEXT],qp.query_plan
FROM sys.dm_exec_query_memory_grants AS mg CROSS APPLY sys.dm_exec_sql_text(mg.plan_handle) AS st
CROSS APPLY sys.dm_exec_query_plan(mg.plan_handle) AS qp ORDER BY mg.required_memory_kb DESC
```
