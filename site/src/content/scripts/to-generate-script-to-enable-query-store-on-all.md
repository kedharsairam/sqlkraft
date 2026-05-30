---
name: "To Generate Script to Enable Query Store on all"
title: "To Generate Script to Enable Query Store on all"
description: "SQL Server diagnostic script for database operations."
category: database
tags: ["database"]
pubDate: 2025-03-15
---

```sql
Set nocount on
select 'ALTER DATABASE ' + name + ' SET QUERY_STORE = ON' + char(10) + char(13)
+'GO' , char(10) + char(13)
+ 'ALTER DATABASE ' + Name + ' SET QUERY_STORE (OPERATION_MODE = READ_WRITE)' + char(10) + char(13) + 'go'
from sys.databases
where name not in ('master','tempdb','model', 'msdb', 'distribution')
```
