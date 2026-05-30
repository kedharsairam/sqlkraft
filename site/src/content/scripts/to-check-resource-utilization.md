---
name: "To Check Resource Utilization"
title: "To Check Resource Utilization"
description: "SQL Server diagnostic script for architecture operations."
category: architecture
tags: ["architecture", "health-check"]
pubDate: 2025-03-15
---

```sql
SELECT object_name,
    counter_name,
    instance_name,
    cntr_value
FROM sys.dm_os_performance_counters
WHERE instance_name = '_Total' AND (counter_name = 'Processor Queue Length' OR counter_name = 'Batch Requests/sec');
```
