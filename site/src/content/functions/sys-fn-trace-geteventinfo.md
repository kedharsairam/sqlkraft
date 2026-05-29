---
name: 'sys.fn_trace_geteventinfo'
title: 'sys.fn_trace_geteventinfo'
category: 'system'
description: 'Returns information about an event being traced.'
tags: ["function"]
pubDate: 2026-05-29
---

When passed the ID of a specific trace,


## returns information about that
trace. When passed an invalid ID, this function returns an empty rowset.

Requires ALTER TRACE permission on the server.

The following example returns information about trace number 2.

sp_trace_setevent (Transact-SQL)

sp_trace_setfilter (Transact-SQL)

Create a Trace (Transact-SQL)

sp_trace_create (Transact-SQL)

sp_trace_generateevent (Transact-SQL)

sp_trace_setstatus (Transact-SQL)

sys.fn_trace_getinfo (Transact-SQL)

sys.fn_trace_gettable (Transact-SQL)

sys.fn_trace_getfilterinfo (Transact-SQL)

See Also

```sql
SELECT * FROM fn_trace_geteventinfo(2) ;
GO
```
