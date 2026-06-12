---
name: "To Generate Script to Change the Database Owner"
title: "To Generate Script to Change the Database Owner"
description: "diagnostic script for database operations."
category: "database"
tags: ["database"]
pubDate: 2025-03-15
---

```sql
SELECT NAME,SUSER_SNAME(OWNER_SID) AS OWNER FROM SYS.DATABASES WHERE SUSER_SNAME(OWNER_SID) != ('SA')

SELECT NAME,OWNER FROM (SELECT NAME,SUSER_SNAME(OWNER_SID) AS OWNER FROM SYS.DATABASES) TEMP
WHERE OWNER NOT IN ('SA')

SELECT 'ALTER AUTHORIZATION ON DATABASE::' + ' '+ NAME+ ' '+ 'TO SA' FROM SYS.DATABASES WHERE SUSER_SNAME(OWNER_SID) != ('SA')
```
