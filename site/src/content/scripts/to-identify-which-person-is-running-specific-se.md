---
name: "To Identify which Person is Running Specific Se"
title: "To Identify which Person is Running Specific Se"
description: "SQL Server diagnostic script for general operations."
category: general
tags: ["general"]
pubDate: 2025-03-15
---

```sql
select * from sys.dm_exec_sessions where session_id = session_id
```
