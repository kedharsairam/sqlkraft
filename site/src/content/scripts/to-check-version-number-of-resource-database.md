---
name: "To Check Version Number of Resource Database"
title: "To Check Version Number of Resource Database"
description: "SQL Server diagnostic script for database operations."
category: database
tags: ["database", "health-check"]
pubDate: 2025-03-15
---

```sql
select serverproperty ('resourceversion')
```
