---
name: "To Check Integrity of Database"
title: "To Check Integrity of Database"
description: "for a detail check"
category: backup-restore
tags: ["backup-restore", "database", "health-check"]
pubDate: 2025-03-15
---

```sql
--for a detail check
dbcc checkdb

--for a quick check
dbcc checkdb with physical_only
```
