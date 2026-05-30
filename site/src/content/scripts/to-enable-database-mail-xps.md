---
name: "To Enable Database Mail XPs"
title: "To Enable Database Mail XPs"
description: "SQL Server diagnostic script for automation operations."
category: automation
tags: ["automation", "database"]
pubDate: 2025-03-15
---

```sql
sp_configure 'show advanced options', 1
go
reconfigure
go

sp_configure 'database mail xps', 1
go
reconfigure
go
```
