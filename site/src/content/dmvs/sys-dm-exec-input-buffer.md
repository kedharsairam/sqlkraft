---
name: "sys.dm_exec_input_buffer"
title: "sys.dm_exec_input_buffer"
category: "execution"
description: "2014 (12.x) SP2 and later versions SQL database in Microsoft Fabric Returns information about statements submitted to an instance of SQL Server. Is the session ID executing the batch to be looked up."
tags: ["execution","dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_exec_input_buffer ( session_id , request_id )"
---

## Description

2014 (12.x) SP2 and later versions SQL database in Microsoft Fabric Returns information about statements submitted to an instance of SQL Server. Is the session ID executing the batch to be looked up.

## Syntax

```sql
sys.dm_exec_input_buffer ( session_id , request_id )
```

## Permissions

2014 (12.x) SP2 and later versions SQL database in Microsoft Fabric Returns information about statements submitted to an instance of SQL Server. session_id Is the session ID executing the batch to be looked up. session_id is. session_id can be obtained from the following dynamic management objects: sys.dm_exec_requests sys.dm_exec_sessions sys.dm_exec_connections request_id The request_id from sys.dm_exec_requests. request_id is. The type of event in the input buffer for the given session ID (SPID). Any parameters provided for the statement. The text of the statement in the input buffer for the given session ID (SPID). On SQL Server, if the user has VIEW SERVER STATE permission, the user will see all executing sessions on the instance of SQL Server; otherwise, the user will see only the current session. ﾉ returns a rowset with the following columns. Description Event type. This could be or. The output will be when no last event was detected. 0 = Text 1- n = Parameters For an of RPC, contains only the procedure name. For an of Language, only the first 4000 characters of the event are displayed. For example, returns the following result set when the last event in the buffer is. Output SQL Server requires the permission, or membership in the fixed server role. ﾉ Expand table ７ Note Starting with SQL Server 2014 (12.x) SP2, use to return information about statements submitted to an instance of SQL Server.
