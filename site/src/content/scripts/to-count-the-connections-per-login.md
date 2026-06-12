---
name: "To Count the Connections per Login"
title: "To Count the Connections per Login"
description: "diagnostic script for security-audit operations."
category: "security-audit"
tags: ["login","security-audit"]
pubDate: 2025-03-15
---

```sql
select login_name ,DB_NAME(database_id) As Database_Name , count(*) as Total_connections from sys.dm_exec_sessions where session_id > 55 group by login_name,DB_NAME(database_id)
```
