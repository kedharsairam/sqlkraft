---
name: 'sys.dm_exec_session_wait_stats'
title: 'sys.dm_exec_session_wait_stats'
category: 'execution'
description: 'SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns information about all the waits encountered by threads that executed for each session. You can use this view to diagnose performance issues with the SQL Server session and also with specific queries and batches. This view returns the same information that is aggregated for Name of the wait type. For more information'
tags: ["execution", "dmv"]
pubDate: 2026-05-29
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns information about all the waits encountered by threads that executed for each session. You can use this view to diagnose performance issues with the SQL Server session and also with specific queries and batches. This view returns the same information that is aggregated for Name of the wait type. For more information, see

## Permissions

SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns information about all the waits encountered by threads that executed for each session. You can use this view to diagnose performance issues with the SQL Server session and also with specific queries and batches. This view returns the same information that is aggregated for sys.dm_os_wait_stats , and provides the number as well. The ID of the session. Name of the wait type. For more information, see sys.dm_os_wait_stats . Number of waits on this wait type. This counter is incremented at the start of each wait. Total wait time for this wait type in milliseconds. This time is inclusive of . Maximum wait time on this wait type. Difference between the time that the waiting thread was signaled and when it started running. This DMV resets the information for a session when the session is opened, or when the session is reset (if connection pooling), For information about the wait types, see sys.dm_os_wait_stats . For SQL Server 2019 (15.x) and previous versions, if you have permission on the server, you see all executing sessions on the instance of SQL Server; otherwise, you see only the current session. ﾉ

## Code Blocks


```sql
session_id
```


```sql
wait_type
```


```sql
waiting_tasks_count
```


```sql
wait_time_ms
```


```sql
signal_wait_time_ms
```
