---
name: 'To view Tasks, Transactions, SPID, etc'
title: 'To view Tasks, Transactions, SPID, etc'
description: 'Get Avg Task Count and Avg Runnable Task Count'
category: architecture
tags: ["architecture"]
pubDate: 2025-03-15
---

```sql
-- Get Avg Task Count and Avg Runnable Task Count
SELECT AVG(current_tasks_count) AS [Avg Task Count],
AVG(runnable_tasks_count) AS [Avg Runnable Task Count]
FROM sys.dm_os_schedulers WITH (NOLOCK)
WHERE scheduler_id < 255;

-- Get Log reuse wait description
SELECT [name], log_reuse_wait_desc
FROM sys.databases WITH (NOLOCK)
WHERE database_id > 4;

-- Find out how many full-text changes are pending on a table
SELECT OBJECTPROPERTY(OBJECT_ID('objectname'),
'TableFulltextPendingChanges') AS 'Monday Full Text Pending Changes';

-- Find oldest open transaction
DBCC OPENTRAN

-- Find command for a given SPID
DBCC INPUTBUFFER(290)

-- Kill a SPID
KILL 290
```
