---
name: 'sys.fn_trace_getfilterinfo'
title: 'sys.fn_trace_getfilterinfo'
category: 'system'
description: 'Returns information about the filters applied to a specified trace.'
tags: ["function"]
pubDate: 2026-05-29
---

## Description
0 = Equal

1 = Not equal

2 = Greater than

3 = Less than

4 = Greater than or equal

5 = Less than or equal

6 = Like

7 = Not like

sql_variant

Specifies the value on which the filter is applied.

The user sets

trace_id

value to identify, modify, and control the trace. When passed the ID of a

specific trace,


## returns information about any filter on that trace. If the
specified trace does not have a filter, this function returns an empty rowset. When passed an

invalid ID, this function returns an empty rowset. For similar information about traces, see

sys.fn_trace_getinfo (Transact-SQL)

.

Requires ALTER TRACE permission on the server.

The following example returns information about all filters on trace number 2.

See Also

Create a Trace (Transact-SQL)

sp_trace_setfilter (Transact-SQL)

sp_trace_create (Transact-SQL)

sp_trace_generateevent (Transact-SQL)

sp_trace_setevent (Transact-SQL)

sp_trace_setstatus (Transact-SQL)

sys.fn_trace_geteventinfo (Transact-SQL)

sys.fn_trace_getinfo (Transact-SQL)

sys.fn_trace_gettable (Transact-SQL)

```sql
SELECT * FROM fn_trace_getfilterinfo(2) ;
GO
```
