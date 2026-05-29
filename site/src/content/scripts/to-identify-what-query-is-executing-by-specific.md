---
name: "To Identify What Query is Executing by Specific"
title: "To Identify What Query is Executing by Specific"
description: "if the query is small, use the following"
category: general
tags: ["general"]
pubDate: 2025-03-15
---

```sql
--if the query is small, use the following
dbcc inputbuffer(session_id)

--if the query is huge, use the following
declare @handle binary(20)
select @handle = sql_handle from sysprocesses where spid = session_id
select* from :: fn_get_sql(@handle)
```
