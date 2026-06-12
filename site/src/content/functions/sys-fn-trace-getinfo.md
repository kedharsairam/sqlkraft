---
name: "sys.fn_trace_getinfo"
title: "sys.fn_trace_getinfo"
category: "system"
description: "Returns information about a specified trace or all existing traces. Valid inputs are the ID number of a trace, NULL, 0, or DEFAULT. NULL, 0, and DEFAULT are equivalent values in this context. Specify NULL, 0, or DEFAULT to return information for all traces in the instance of SQL Server. 1= Trace options. For more information, see @options in This feature will be r"
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_trace_getinfo ( { trace_id | NULL | 0 | DEFAULT } )"
---

## Description

Returns information about a specified trace or all existing traces. Valid inputs are the ID number of a trace, NULL, 0, or DEFAULT. NULL, 0, and DEFAULT are equivalent values in this context. Specify NULL, 0, or DEFAULT to return information for all traces in the instance of SQL Server. 1= Trace options. For more information, see @options in This feature will be removed in a future version of SQL Server.

## Syntax

```sql
sys.fn_trace_getinfo ( { trace_id | NULL | 0 | DEFAULT } )
```

## Permissions

Requires ALTER TRACE permission. sys.fn_trace_geteventinfo (Transact-SQL) sys.fn_trace_getinfo (Transact-SQL) sp_trace_generateevent (Transact-SQL) SQL Server Event Class Reference SQL Trace
## Examples

### Example 1

```sql
SELECT * FROM sys.fn_trace_getinfo(0) ;
GO
```
