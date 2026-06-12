---
name: "sys.sp_trace_setevent"
title: "sp_trace_setevent"
category: "general"
description: "Adds or removes an event or event column to a trace. on existing traces that are stopped ( ). An error is returned if this stored procedure is executed on a trace that doesn't exist or whose This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_trace_setevent
              [ @traceid = ] traceid
              , [ @eventid = ] eventid
              , [ @columnid = ] columnid
              , [ @on = ] on
              [ ; ]
---

## Description

Adds or removes an event or event column to a trace. on existing traces that are stopped ( ). An error is returned if this stored procedure is executed on a trace that doesn't exist or whose This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_trace_setevent
[ @traceid = ] traceid
, [ @eventid = ] eventid
, [ @columnid = ] columnid
, [ @on = ] on
[ ; ]
```
