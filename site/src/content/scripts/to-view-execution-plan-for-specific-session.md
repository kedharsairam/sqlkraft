---
name: "To View Execution Plan for Specific Session"
title: "To View Execution Plan for Specific Session"
description: "SQL Server diagnostic script for architecture operations."
category: architecture
tags: ["architecture", "session"]
pubDate: 2025-03-15
---

```sql
SELECT * FROM sys.dm_exec_query_statistics_xml(59);
```
