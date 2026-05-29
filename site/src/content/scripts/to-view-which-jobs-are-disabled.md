---
name: "To View Which Jobs are Disabled"
title: "To View Which Jobs are Disabled"
description: "SQL Server diagnostic script for automation operations."
category: automation
tags: ["agent-job", "automation"]
pubDate: 2025-03-15
---

```sql
SELECT name FROM msdb.dbo.sysjobs WHERE enabled = 0 ORDER BY name
```
