---
name: "To Identify Blockings"
title: "To Identify Blockings"
description: "SQL Server diagnostic script for performance operations."
category: performance
tags: ["blocking", "performance"]
pubDate: 2025-03-15
---

```sql
select * from sys.dm_exec_requests
where session_id>50 and blocking_session_id<>0
```
