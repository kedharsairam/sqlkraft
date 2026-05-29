---
name: 'sys.fn_trace_getinfo'
title: 'sys.fn_trace_getinfo'
category: 'system'
description: 'Returns information about a specified trace or all existing traces.'
tags: ["function"]
pubDate: 2026-05-29
---

## Description
(Transact-SQL)

.

2 = File name

3 = Max size

4 = Stop time

5 = Current trace status. 0 = stopped. 1 = running.

value

sql_variant

Information about the property of the trace specified.

When passed the ID of a specific trace, fn_trace_getinfo returns information about that trace.

When passed an invalid ID, this function returns an empty rowset.

fn_trace_getinfo appends a .trc extension to the name of any trace file included in its result set.

For information on defining a trace, see

sp_trace_create (Transact-SQL)

. For similar information

about trace filters, see

sys.fn_trace_getfilterinfo (Transact-SQL)

.

For a complete example of using trace stored procedures, see

Create a Trace (Transact-SQL)

.

Requires ALTER TRACE permission on the server.

The following example returns information about all active traces.

Create a Trace (Transact-SQL)

sp_trace_create (Transact-SQL)

See Also

sp_trace_generateevent (Transact-SQL)

sp_trace_setevent (Transact-SQL)

sp_trace_setfilter (Transact-SQL)

sp_trace_setstatus (Transact-SQL)

sys.fn_trace_getfilterinfo (Transact-SQL)

sys.fn_trace_geteventinfo (Transact-SQL)

sys.fn_trace_gettable (Transact-SQL)

```sql
SELECT * FROM sys.fn_trace_getinfo(0) ;
GO
```
