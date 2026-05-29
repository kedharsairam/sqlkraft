---
name: 'To Check Recovery Model of Database'
title: 'To Check Recovery Model of Database'
description: 'SQL Server diagnostic script for backup-restore operations.'
category: backup-restore
tags: ["backup-restore", "database", "health-check"]
pubDate: 2025-03-15
---

```sql
select name, recovery_model_desc, recovery_model
from sys.databases
```
