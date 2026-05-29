---
name: 'To Check Which Login are in Specific Server Rol'
title: 'To Check Which Login are in Specific Server Rol'
description: 'SQL Server diagnostic script for security-audit operations.'
category: security-audit
tags: ["health-check", "login", "security-audit"]
pubDate: 2025-03-15
---

```sql
sp_srvrolepermission 'rolename'
go
```
