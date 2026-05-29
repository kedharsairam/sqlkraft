---
name: "To Remove Restricted User"
title: "To Remove Restricted User"
description: "SQL Server diagnostic script for security-audit operations."
category: security-audit
tags: ["security-audit", "user"]
pubDate: 2025-03-15
---

```sql
Use [databasename]

ALTER DATABASE [databasename] SET SINGLE_USER WITH ROLLBACK IMMEDIATE
GO

ALTER DATABASE [databasename] SET MULTI_USER
GO
```
