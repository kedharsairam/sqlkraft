---
name: "To View Table Page Information"
title: "To View Table Page Information"
description: "SQL Server diagnostic script for index-maintenance operations."
category: index-maintenance
tags: ["index-maintenance", "table"]
pubDate: 2025-03-15
---

```sql
DBCC IND('databasename','tablename',0)
--0 for head structure
--2 for nonclustered index
--1 for clustered index
```
