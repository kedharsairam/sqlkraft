---
name: "sys.trace_events"
title: "sys.trace_events"
category: "compatibility"
description: "Contains one row for each Extended Events event that is mapped to a SQL Trace event class. This table is stored in the master database, in the sys schema. The ID of the SQL Trace event class that is being mapped."
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  SELECT te.name, xe.package_name, xe.xe_event_name
      FROM sys.trace_events AS te
      LEFT JOIN sys.trace_xe_event_map AS xe
      ON te.trace_event_id = xe.trace_event_id
      WHERE xe.trace_event_id IS NOT NULL
      SELECT te.trace_event_id, te.name
      FROM sys.trace_events AS te
      LEFT JOIN sys.trace_xe_event_map AS xe
      ON te.trace_event_id = xe.trace_event_id
      WHERE xe.trace_event_id IS NULL
---

## Description

Contains one row for each Extended Events event that is mapped to a SQL Trace event class. This table is stored in the master database, in the sys schema. The ID of the SQL Trace event class that is being mapped.

## Syntax

```sql
SELECT te.name, xe.package_name, xe.xe_event_name
FROM sys.trace_events AS te
LEFT JOIN sys.trace_xe_event_map AS xe
ON te.trace_event_id = xe.trace_event_id
WHERE xe.trace_event_id IS NOT NULL
SELECT te.trace_event_id, te.name
FROM sys.trace_events AS te
LEFT JOIN sys.trace_xe_event_map AS xe
ON te.trace_event_id = xe.trace_event_id
WHERE xe.trace_event_id IS NULL
```

## Permissions

Article • 02/28/2023 The catalog view contains a list of all SQL trace events. These trace events do not change for a given version of the SQL Server Database Engine. For more information about these trace events, see SQL Server Event Class Reference. Description Unique ID of the event. This column is also in the and catalog views. Category ID of the event. This column is also in the catalog view. Unique name of this event. This parameter is not localized. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. Object Catalog Views (Transact-SQL) sys.traces (Transact-SQL) sys.trace_categories (Transact-SQL) sys.trace_columns (Transact-SQL) ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Event catalog views instead. ﾉ Expand table See also Article • 02/28/2023 The catalog view contains a list of all possible usage combinations of events and columns. For each event listed in the column, all available columns are listed in the column. Not all available columns are populated each time a given event occurs. These values do not change for a given version of the SQL Server Database Engine. For a complete list of supported trace events, see SQL Server Event Class Reference. Description ID of the trace event. This column is also in the catalog view. ID of the trace column. This column is also in the catalog view. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. Object Catalog Views (Transact-SQL) sys.traces (Transact-SQL) sys.trace_categories (Transact-SQL) sys.trace_columns (Transact-SQL) ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Event catalog views instead. ﾉ Expand table See Also sys.trace_events (Transact-SQL) sys.trace_subclass_values (Transact-SQL) Article • 02/28/2023 Each row in the catalog view identifies a category that is unique across the server. These categories do not change for a given version of the SQL Server Database Engine. For a complete list of supported trace events, see SQL Server Event Class Reference. Description Unique ID of this category. This column is also in the catalog view. Unique name of this category. This parameter is not localized. Category type: 0 = Normal 1 = Connection 2 = Error The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Event catalog views instead. ﾉ Expand table See Also Article • 02/28/2023 The catalog view contains a list of named column values. These subclass values do not change for a given version of the SQL Server Database Engine. For a complete list of supported trace events, see SQL Server Event Class Reference. Description ID of the trace event. This parameter is also in the catalog view. ID of the trace column used for enumeration. This parameter is also in the catalog view. Meaning of the column value. Column value. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. Object Catalog Views (Transact-SQL) sys.traces (Transact-SQL) sys.trace_categories (Transact-SQL) sys.trace_columns (Transact-SQL) ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Event catalog views instead. ﾉ Expand table See Also sys.trace_events (Transact-SQL) sys.trace_event_bindings (Transact-SQL)

## Remarks

Contains one row for each Extended Events event that is mapped to a SQL Trace event class.

This table is stored in the master database, in the sys schema.

Description

trace_event_id

The ID of the SQL Trace event class that is being mapped.

package_name

The name of the Extended Events package where the mapped event

xe_event_name

The name of the Extended Events event that is mapped to the SQL Trace

event class.

You can use the following query to identify the Extended Events events that are equivalent to

the SQL Trace event classes:

Not all event classes have equivalent Extended Events events. You can use the following query

to list the event classes that do not have an Extended Events equivalent:

Expand table

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

Profiler for Trace Capture

Use Extended Events Profiler embedded in SQL

Server Management Studio.

Profiler

Profiler for Trace Replay

Distributed Replay overview

Profiler

Microsoft.SqlServer.Management.Trace namespace (contains the APIs for

Trace and Replay objects)

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

varbinary(50). If developers have allocated

varbinary(50)

the application might require changes if the
