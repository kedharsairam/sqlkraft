---
name: 'sys.sp_trace_create'
title: 'sp_trace_create'
category: 'general'
description: 'Invalid parameters. Returned when the user supplied incompatible parameters. is a SQL Server stored procedure that performs many of the actions previously executed by extended stored procedures available in earlier versions of SQL Server. Use only creates a trace definition. This stored procedure can''t be used to start or change a trace. Parameters of all SQL Trace stored procedures ( ) are strict'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_trace_create
  [ @traceid = ] traceid
  OUTPUT
  , [ @options = ] options
  , [ @tracefile = ]
  N
  'tracefile'
  [ , [ @maxfilesize = ] maxfilesize ]
  [ , [ @stoptime = ]
  'stoptime'
  ]
  [ , [ @filecount = ] filecount ]
  [ ; ]
---

## Description

Invalid parameters. Returned when the user supplied incompatible parameters. is a SQL Server stored procedure that performs many of the actions previously executed by extended stored procedures available in earlier versions of SQL Server. Use only creates a trace definition. This stored procedure can't be used to start or change a trace. Parameters of all SQL Trace stored procedures ( ) are strictly typed. If these parameters aren't called with the correct input parameter data types, as specified in the argument description, the stored procedure returns an error. , the SQL Server service account must have permission on the trace file folder. If the SQL Server service account isn't an administrator on the computer where the trace file is located, you must explicitly grant write permission to the SQL Server service Create a Trace (Transact-SQL) Deprecated feature

## Syntax

```sql
sp_trace_create
[ @traceid = ] traceid
OUTPUT
, [ @options = ] options
, [ @tracefile = ]
N
'tracefile'
[ , [ @maxfilesize = ] maxfilesize ]
[ , [ @stoptime = ]
'stoptime'
]
[ , [ @filecount = ] filecount ]
[ ; ]
```

## Remarks

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

Create a Trace (Transact-SQL)

sp_trace_setfilter (Transact-SQL)

sp_trace_create (Transact-SQL)

sp_trace_generateevent (Transact-SQL)

sp_trace_setevent (Transact-SQL)

sp_trace_setstatus (Transact-SQL)

sys.fn_trace_geteventinfo (Transact-SQL)

sys.fn_trace_getinfo (Transact-SQL)

sys.fn_trace_gettable (Transact-SQL)

Deprecated feature

Replacement

Feature name

Embedded SQL for C

Although the Database Engine still supports

connections from existing applications that use

the DB-Library and Embedded SQL APIs, it

doesn't include the files or documentation

required to do programming work on

applications that use these APIs. A future

version of the SQL Server Database Engine will

drop support for connections from DB-Library

or Embedded SQL applications. Don't use DB-

Library or Embedded SQL to develop new

applications. Remove any dependencies on

either DB-Library or Embedded SQL when you

modify existing applications. Instead of these

APIs, use the SQLClient namespace or an API

such as ODBC. The current version doesn't

include the DB-Library DLL required to run

these applications. To run DB-Library or

Embedded SQL applications, you must have

available the DB-Library DLL from SQL Server

version 6.5, SQL Server 7.0, or SQL Server 2000

SQL Server Profiler for Trace Capture

Use Extended Events Profiler embedded in SQL

Server Management Studio.

SQL Server Profiler

SQL Server Profiler for Trace Replay

SQL Server Distributed Replay overview

SQL Server Profiler

Microsoft.SqlServer.Management.Trace namespace (contains the APIs for

SQL Server Trace and Replay objects)

Trace Configuration:

Microsoft.SqlServer.Management.XEvent

Trace Reading:

Microsoft.SqlServer.XEvent.Linq

Trace Replay: None

procedures,

and catalog

fn_trace_geteventinfo

fn_trace_getfilterinfo

fn_trace_getinfo

fn_trace_gettable

sys.trace_categories

sys.trace_columns

sys.trace_subclass_values

Extended Events overview

fn_trace_geteventinfo

fn_trace_getfilterinfo

fn_trace_getinfo

fn_trace_gettable

Set options

parameter for

is currently documented as

varbinary(8000)

which is the correct maximum length. However

the current implementation returns

varbinary(50)

. If developers have allocated

varbinary(50)

the application might require changes if the
