---
name: 'sys.fn_trace_gettable'
title: 'sys.fn_trace_gettable'
category: 'system'
description: 'Returns the content of one or more trace files in tabular form.'
tags: ["function"]
pubDate: 2026-05-29
returnType: 'B. Using fn_trace_gettable to return a table with an IDENTITY'
---

## A. Using fn_trace_gettable to import rows from a trace file

## column that can be loaded into a SQL Server table

automatically appended when a file rolls over.) As a workaround, you can rename the trace files

to remove the underscores in the original file name. For example, if the original file is named

and the rollover file is named

, you can rename the files to

and

.

This function can read a trace that is still active on the instance on which it is executed.

Requires ALTER TRACE permission on the server.

The following example calls

inside the

clause of a

statement.

The following example calls the function as part of a

statement and returns a

table with an

column that can be loaded into the table

.

See Also

sp_trace_generateevent (Transact-SQL)

sp_trace_setevent (Transact-SQL)

sp_trace_setfilter (Transact-SQL)

sp_trace_setstatus (Transact-SQL)

```sql
fn_trace_gettable
```

```sql
FROM
```

```sql
SELECT...INTO
```

```sql
SELECT...INTO
```

```sql
IDENTITY
```

```sql
temp_trc
```

```sql
USE AdventureWorks2022;
GO
SELECT * INTO temp_trc
FROM fn_trace_gettable('c:\temp\mytrace.trc', default);
GO
```

```sql
USE AdventureWorks2022;
GO
SELECT IDENTITY(int, 1, 1) AS RowNumber, * INTO temp_trc
FROM fn_trace_gettable('c:\temp\mytrace.trc', default);
GO
```
