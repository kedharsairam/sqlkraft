---
name: "To Check Page Life Expectancy, Buffer Cache Hit"
title: "To Check Page Life Expectancy, Buffer Cache Hit"
description: "diagnostic script for architecture operations."
category: architecture
tags: ["architecture", "cache", "health-check"]
pubDate: 2025-03-15
---

```sql
SELECT object_name, counter_name, cntr_value from sys.dm_os_performance_counters WHERE [object_name] LIKE '%Buffer Manger%' AND [counter_name] = 'page life expectancy'
SELECT object_name, counter_name, cntr_value from sys.dm_os_performance_counters WHERE [object_name] LIKE '%Buffer Manger%' AND [counter_name] = 'Buffer cache hit ratio'
```
