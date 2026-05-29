---
name: "To Verify the Backup file"
title: "To Verify the Backup file"
description: "SQL Server diagnostic script for backup-restore operations."
category: backup-restore
tags: ["backup", "backup-restore"]
pubDate: 2025-03-15
---

```sql
restore verifyonly from disk = 'path\filename.bak'
with file = filepositionnumber
```
