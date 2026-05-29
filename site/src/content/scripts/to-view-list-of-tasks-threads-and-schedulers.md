---
name: 'To View List of Tasks, Threads and Schedulers'
title: 'To View List of Tasks, Threads and Schedulers'
description: 'SQL Server diagnostic script for architecture operations.'
category: architecture
tags: ["architecture"]
pubDate: 2025-03-15
---

```sql
select * from sys.dm_os_tasks

select * from sys.dm_os_threads

select * from sys.dm_os_schedulers
```
