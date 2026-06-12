---
name: "To Update User Role in Database"
title: "To Update User Role in Database"
description: "diagnostic script for security-audit operations."
category: "security-audit"
tags: ["database","security-audit","user"]
pubDate: 2025-03-15
---

```sql
USE [databasename]
GO
ALTER ROLE [db_datareader] DROP MEMBER [username]
GO
USE [databasename]
GO
ALTER ROLE [db_owner] ADD MEMBER [username]
GO
```
