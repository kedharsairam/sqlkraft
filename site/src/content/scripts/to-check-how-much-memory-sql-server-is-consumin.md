---
name: "To Check How much Memory SQL Server is Consumin"
title: "To Check How much Memory SQL Server is Consumin"
description: "it will give you an approx. value of how much sql server is using memory in mb."
category: "architecture"
tags: ["architecture","health-check","memory"]
pubDate: "2025-03-15"
---

```sql
--it will give you an approx. value of how much sql server is using memory in mb.
--this is also size of buffer pool at this moment.
select sum(pages_kb)/1024 memoryusedinmb from sys.dm_os_memory_clerks
```
