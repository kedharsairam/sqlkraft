---
title: "Trace Management Objects"
topic: "query-processing"
description: "and CONCAT_NULLS_YIELDS_NULL"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Deprecated feature

Replacement

Feature name

and

database option

and

database option

,

and CONCAT_NULLS_YIELDS_NULL

are always set to.

are unavailable.

sys.dm_exec_describe_first_result_set

,

sys.dm_exec_describe_first_result_set_for_object

,

sp_describe_first_result_set

, and

sp_describe_undeclared_parameters.

Specifying

or

in the

clause of an

or

statement.

Remove the

or

table hints from the

clause.

or

in

or

Specifying table hints without using

the

keyword.

Use.

Table hint without

INSERT_HINTS

INSERT_HINTS

Deprecated feature

Replacement

Feature name

Profiler for Trace Capture

Use Extended Events Profiler embedded in SQL Server Management Studio.

Profiler

Profiler for Trace Replay

Distributed Replay overview

Deprecated feature

Replacement

Feature

name

Microsoft.SqlServer.Management.Trace namespace (contains the APIs

for SQL Server Trace and Replay objects)

Trace Configuration:

Microsoft.SqlServer.Management.XEvent

Trace Reading:

Microsoft.SqlServer.XEvent.Linq

Trace Replay: None

ﾉ

Expand table

ﾉ

Expand table

Deprecated feature

Replacement

Feature

name

Inline XDR Schema

Generation

The XMLDATA directive to the

option is deprecated. Use XSD generation in the case of

and

modes. There's no replacement for the XMLDATA directive in EXPLICT mode.

XMLDATA

Discontinued Database Engine functionality in SQL Server

ﾉ

Expand table

７

Note

The cookie

parameter for

is currently documented as

varbinary(8000)

which is the correct

maximum length. However the current implementation returns

varbinary(50). If developers have allocated

varbinary(50)

the application might require changes if the cookie return size increases in a future release. Though not

a deprecation issue this is mentioned in this topic because the application adjustments are similar. For more

information, see

sp_setapprole.
