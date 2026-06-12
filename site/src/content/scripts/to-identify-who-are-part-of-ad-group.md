---
name: "To Identify Who are part of AD Group"
title: "To Identify Who are part of AD Group"
description: "Finding out members of Active Directory Group that is already in SQL Server"
category: "security-audit"
tags: ["security-audit"]
pubDate: "2025-03-15"
---

```sql
--Finding out members of Active Directory Group that is already in SQL Server
EXEC master.dbo.xp_logininfo 'Forest\SQLADMINS',@option ='Members'

--Finding out Active directory group that below user belong to.
EXEC master.dbo.xp_logininfo 'FOREST\user02'
```
