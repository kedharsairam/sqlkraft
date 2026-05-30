---
name: "sys.sp_trace_setstatus"
title: "sp_trace_setstatus"
category: "general"
description: "Modifies the current state of the specified trace. Transact-SQL syntax conventions The ID of the trace to be modified. , with no default. The user employs this value to identify, modify, and control the trace. For information about retrieving the This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that cu"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_trace_setstatus
  [ @traceid = ] traceid
  , [ @status = ] status
  [ ; ]
---

## Description

Modifies the current state of the specified trace. Transact-SQL syntax conventions The ID of the trace to be modified. , with no default. The user employs this value to identify, modify, and control the trace. For information about retrieving the This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_trace_setstatus
[ @traceid = ] traceid
, [ @status = ] status
[ ; ]
```
