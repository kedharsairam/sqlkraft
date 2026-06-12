---
name: "sys.database_event_session_targets"
title: "sys.database_event_session_targets (Azure SQL Database)"
category: "compatibility"
description: "2016 (13.x) and later versions Azure SQL Database Managed Instance SQL database in Microsoft Fabric dynamic management view (DMV) returns a row for each event target for a database-scoped event session."
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: "sys.database_event_session_targets"
---

## Description

2016 (13.x) and later versions Azure SQL Database Managed Instance SQL database in Microsoft Fabric dynamic management view (DMV) returns a row for each event target for a database-scoped event session. For information about database-scoped sys.dm_xe_database_session_targets Azure SQL Database and SQL database in Fabric support only database-scoped sessions Azure SQL Managed Instance supports both database-scoped sessions and server-scoped sessions Server-scoped sessions are recommended for SQL managed instances. For more information, see CREATE EVENT SESSION code examples The ID of the event session. Is not nullable. The ID of the target. ID is unique within the event session object. Is not nullable.

## Syntax

`sys.database_event_session_targets`

## Remarks

2016 (13.x) and later versions

Managed Instance

dynamic management view (DMV) returns a row for each

event target for a database-scoped event session. For information about

database-scoped

sessions, see

sys.dm_xe_database_session_targets

and SQL database in Fabric support only

database-scoped sessions

supports both database-scoped sessions and

server-scoped sessions

Server-scoped sessions are recommended for SQL managed instances. For more information, see

CREATE EVENT SESSION code examples

Column name

Description

The ID of the event session. Is not nullable.

The ID of the target. ID is unique within the event session object. Is not nullable.

The name of the event target. Is not nullable.

The name of the event package that contains the event target. Is not nullable.

The name of the module that contains the event target. Is not nullable.

Requires the VIEW DATABASE PERFORMANCE STATE permission.

This view has the following relationship cardinalities.

Relationship

Many to one

Extended events in Azure SQL Database

Event File target code for extended events in Azure SQL Database and SQL Managed Instance

sys.database_event_sessions (Azure SQL Database and Azure SQL Managed Instance)

Expand table

Expand table
