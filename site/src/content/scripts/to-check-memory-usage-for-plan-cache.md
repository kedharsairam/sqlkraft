---
name: 'To Check Memory Usage for Plan Cache'
title: 'To Check Memory Usage for Plan Cache'
description: 'SQL Server diagnostic script for architecture operations.'
category: architecture
tags: ["architecture", "cache", "health-check", "memory"]
pubDate: 2025-03-15
---

```sql
select name, type, buckets_count
from sys.dm_os_memory_cache_hash_tables
where name IN ( 'SQL Plans' , 'Object Plans' , 'Bound Trees' ,'Extended Stored Procedures')

select name, type, pages_kb, entries_count
from sys.dm_os_memory_cache_counters
where name IN ( 'SQL Plans' , 'Object Plans' ,  'Bound Trees' ,'Extended Stored Procedures')
```
