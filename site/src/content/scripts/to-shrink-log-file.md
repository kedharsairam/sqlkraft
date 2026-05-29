---
name: "To Shrink Log File"
title: "To Shrink Log File"
description: "SQL Server diagnostic script for backup-restore operations."
category: backup-restore
tags: ["backup-restore"]
pubDate: 2025-03-15
---

```sql
USE [databasename]
DBCC SHRINKFILE (N'databasename_Log' , 0, TRUNCATEONLY)
```
