---
name: 'To view List of Tables in Database'
title: 'To view List of Tables in Database'
description: 'SQL Server diagnostic script for database operations.'
category: database
tags: ["database", "table"]
pubDate: 2025-03-15
---

```sql
select * from sys.tables

--or
--universal command
select * from information_schema.tables
```
