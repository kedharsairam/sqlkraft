---
name: 'To Find Orphan Users in Database'
title: 'To Find Orphan Users in Database'
description: 'SQL Server diagnostic script for security-audit operations.'
category: security-audit
tags: ["database", "security-audit", "user"]
pubDate: 2025-03-15
---

```sql
exec sp_change_users_login 'report'
```
