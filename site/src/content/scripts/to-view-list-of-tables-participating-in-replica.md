---
name: 'To View List of Tables Participating in Replica'
title: 'To View List of Tables Participating in Replica'
description: 'SQL Server diagnostic script for replication operations.'
category: replication
tags: ["replication", "table"]
pubDate: 2025-03-15
---

```sql
select * from sys.tables where is_replicated = 1
select * from sys.tables where is_merger_published = 1
```
