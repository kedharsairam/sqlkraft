---
name: 'To Check Specific Database is Participating in'
title: 'To Check Specific Database is Participating in'
description: 'SQL Server diagnostic script for replication operations.'
category: replication
tags: ["database", "health-check", "replication"]
pubDate: 2025-03-15
---

```sql
select * from sys.databases where name = 'databasename'
```
