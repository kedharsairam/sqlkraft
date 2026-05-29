---
name: "To Check Error Log for Errors"
title: "To Check Error Log for Errors"
description: "SQL Server diagnostic script for troubleshooting operations."
category: troubleshooting
tags: ["health-check", "troubleshooting"]
pubDate: 2025-03-15
---

```sql
EXEC xp_ReadErrorLog 0, 1, N'error'
```
