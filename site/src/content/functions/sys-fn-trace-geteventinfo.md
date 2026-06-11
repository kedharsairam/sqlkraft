---
name: "sys.fn_trace_geteventinfo"
title: "sys.fn_trace_geteventinfo"
category: "system"
description: "Returns information about an event being traced. Transact-SQL syntax conventions Is the ID of the trace. , with no default."
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "fn_trace_geteventinfo ( trace_id )"
---

## Description

Returns information about an event being traced. Transact-SQL syntax conventions Is the ID of the trace. , with no default. ID of the traced event ID numbers of all columns collected for each event This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Events instead.

## Syntax

```sql
fn_trace_geteventinfo ( trace_id )
```

## Permissions

Requires ALTER TRACE permission. sys.fn_trace_geteventinfo (Transact-SQL) sys.fn_trace_getinfo (Transact-SQL) sp_trace_generateevent (Transact-SQL) SQL Server Event Class Reference SQL Trace Related content

## Remarks

Applies to:

Returns information about an event being traced.

Transact-SQL syntax conventions

Is the ID of the trace.

, with no default.

Description

ID of the traced event

ID numbers of all columns collected for each event

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Extended Events instead.

Expand table

## Examples

### Example 1

```sql
SELECT * FROM fn_trace_geteventinfo(2) ;
GO
```

### Example 2

```sql
SELECT
CAST (0x5B007B0022004900640022003A0031002C002200440061007400610022003A00220045007800610
06D0070006C0065002000640061007400610022007D005D00
AS
NVARCHAR (
MAX
));
-- This returns: [{"Id":1,"Data":"Example data"}]
```

### Example 3

```sql
SELECT
CAST (0x5B007B0022004900640022003A0031002C002200440061007400610022003A00220045007800610
06D0070006C0065002000640061007400610022007D005D00
AS
NVARCHAR (
MAX
));
-- This returns: [{"Id":1,"Data":"Example data"}]
```
