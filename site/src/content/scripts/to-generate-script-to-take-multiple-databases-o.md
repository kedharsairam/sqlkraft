---
name: 'To Generate Script to Take Multiple Databases O'
title: 'To Generate Script to Take Multiple Databases O'
description: 'SQL Server diagnostic script for database operations.'
category: database
tags: ["database"]
pubDate: 2025-03-15
---

```sql
select 'alter database ' +name+ ' set offline with rollback immediate' from sys.databases
where name not in ('master','model','msdb','tempdb','distribution')
```
