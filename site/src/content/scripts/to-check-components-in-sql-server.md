---
name: 'To Check Components in SQL Server'
title: 'To Check Components in SQL Server'
description: 'it will check cpu, memory, io and so on...'
category: high-availability
tags: ["health-check", "high-availability"]
pubDate: 2025-03-15
---

```sql
--it will check cpu, memory, io and so on...
--this will work only from sql server 2012
sp_server_diagnostics
```
