---
name: 'To View Locks'
title: 'To View Locks'
description: 'SQL Server diagnostic script for performance operations.'
category: performance
tags: ["performance"]
pubDate: 2025-03-15
---

```sql
select * from sys.dm_tran_locks

--or

select * from master..syslockinfo
```
