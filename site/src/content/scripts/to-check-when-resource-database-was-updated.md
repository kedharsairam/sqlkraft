---
name: "To Check When Resource Database was Updated"
title: "To Check When Resource Database was Updated"
description: "SQL Server diagnostic script for database operations."
category: database
tags: ["database", "health-check"]
pubDate: 2025-03-15
---

```sql
select serverproperty ('resourcelastupdatedatetime')
```
