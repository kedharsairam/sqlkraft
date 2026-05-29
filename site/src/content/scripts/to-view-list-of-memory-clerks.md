---
name: 'To View List of Memory Clerks'
title: 'To View List of Memory Clerks'
description: 'SQL Server diagnostic script for architecture operations.'
category: architecture
tags: ["architecture", "memory"]
pubDate: 2025-03-15
---

```sql
select * from sys.dm_os_memory_clerks

--to view only unique but not duplicates, use the following command
select distinct(type) from sys.dm_os_memory_clerks
order by type
```
