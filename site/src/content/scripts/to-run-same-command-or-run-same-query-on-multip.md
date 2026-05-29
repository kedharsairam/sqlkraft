---
name: 'To Run Same Command or Run Same Query on Multip'
title: 'To Run Same Command or Run Same Query on Multip'
description: 'SQL Server diagnostic script for database operations.'
category: database
tags: ["database"]
pubDate: 2025-03-15
---

```sql
DECLARE @command varchar(1000) 
SELECT @command = 'USE ? SELECT name FROM sysobjects WHERE xtype = ''U'' ORDER BY name'
--Ex1: SELECT @command = 'USE ? DBCC CHECKDB'
--Ex2: SELECT @command = 'USE ? alter database ? set compatibility_level = 150'
EXEC sp_MSforeachdb @command
```
