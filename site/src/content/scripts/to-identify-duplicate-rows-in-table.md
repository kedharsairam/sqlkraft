---
name: 'To Identify Duplicate Rows in Table'
title: 'To Identify Duplicate Rows in Table'
description: 'SQL Server diagnostic script for database operations.'
category: database
tags: ["database", "table"]
pubDate: 2025-03-15
---

```sql
select * , count(*) from tablename
group by name, id
having count(*) > 1
```
