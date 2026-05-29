---
name: 'sys.fn_trace_gettable'
title: 'sys.fn_trace_gettable'
category: 'system'
description: 'Returns the content of one or more trace files in tabular form. Transact-SQL syntax conventions Specifies the initial trace file to be read. , with no default. Specifies the number of rollover files to be read. This number includes the initial file specified in is specified as reads all rollover files until it reaches the end of the trace. returns a table with all the columns valid for the specifi'
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: 'fn_trace_gettable ( ''filename'' , number_files )'
---

## Description

Returns the content of one or more trace files in tabular form. Transact-SQL syntax conventions Specifies the initial trace file to be read. , with no default. Specifies the number of rollover files to be read. This number includes the initial file specified in is specified as reads all rollover files until it reaches the end of the trace. returns a table with all the columns valid for the specified trace. For more information, see sp_trace_setevent (Transact-SQL) Be aware that the fn_trace_gettable function will not load rollover files (when this option is specified by using the argument) where the original trace file name ends with an underscore and a numeric value. (This does not apply to the underscore and number that are This feature will be removed in a future version of SQL Server. Avoid using this feature in Invalid parameters. Returned when the user supplied incompatible parameters.

## Syntax

```sql
fn_trace_gettable ( 'filename' , number_files )
```

## Permissions

Description Note: The columns that are returned by the snapshots.fn_trace_gettable function correspond to the values in the name column in the sys.trace_columns system view. The only difference is that the GroupID column is not returned by the function. Requires SELECT permission for mdw_reader. Data Collection See Also

## Remarks

Applies to:

Returns the content of one or more trace files in tabular form.

Transact-SQL syntax conventions

Specifies the initial trace file to be read.

, with no default.

number_files

Specifies the number of rollover files to be read. This number includes the initial file specified in

number_files

number_files

is specified as

reads all rollover files until it reaches

the end of the trace.

returns a table with all the columns valid for the

specified trace. For more information, see

sp_trace_setevent (Transact-SQL)

Be aware that the fn_trace_gettable function will not load rollover files (when this option is

specified by using the

number_files

argument) where the original trace file name ends with an

underscore and a numeric value. (This does not apply to the underscore and number that are

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Extended Events instead.

Description

Invalid parameters. Returned when the user supplied incompatible parameters.

is a SQL Server stored procedure that performs many of the actions

previously executed by

extended stored procedures available in earlier versions of

SQL Server. Use

instead of:

only creates a trace definition. This stored procedure can't be used to start or

change a trace.

Parameters of all SQL Trace stored procedures (

) are strictly typed. If these

parameters aren't called with the correct input parameter data types, as specified in the

argument description, the stored procedure returns an error.

, the SQL Server service account must have

permission on the trace

file folder. If the SQL Server service account isn't an administrator on the computer where the

trace file is located, you must explicitly grant write permission to the SQL Server service

For an example of using trace stored procedures, see

Create a Trace

has the following characteristics:

It's a rollover trace. The default

is 2 but can be overridden by the user using

The default

@maxfilesize

, as with other traces, is 5 MB and can be changed.

You can automatically load the trace file created with

into a table by

system function. For more information, see
