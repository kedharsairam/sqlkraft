---
name: "sys.database_event_session_events"
title: "sys.database_event_session_events (Azure SQL Database)"
category: "compatibility"
description: "2016 (13.x) and later versions Azure SQL Database Managed Instance SQL database in Microsoft Fabric dynamic management view (DMV) returns a row for each event in a database-scoped event session. For information on events in database-scoped sessions, see sys.dm_xe_database_session_events Azure SQL Database and SQL database in Fabric support only database-scoped sessions Azure SQL Managed"
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: "sys.database_event_session_events"
---

## Description

2016 (13.x) and later versions Azure SQL Database Managed Instance SQL database in Microsoft Fabric dynamic management view (DMV) returns a row for each event in a database-scoped event session. For information on events in database-scoped sessions, see sys.dm_xe_database_session_events Azure SQL Database and SQL database in Fabric support only database-scoped sessions Azure SQL Managed Instance supports both database-scoped sessions and. Server-scoped sessions are recommended for SQL managed instances. For more information, see CREATE EVENT SESSION code examples The ID of the event session. Is not nullable. The ID of the event. This ID is unique within an event session object. Is not The name of the event. Is not nullable.

## Syntax

`sys.database_event_session_events`

## Remarks

2016 (13.x) and later versions

Managed Instance

dynamic management view (DMV) returns a row for each event

in a database-scoped event session. For information on events in

database-scoped sessions, see

sys.dm_xe_database_session_events

and SQL database in Fabric support only

database-scoped sessions

supports both database-scoped sessions and

server-scoped. Server-scoped sessions are recommended for SQL managed instances. For more

information, see

CREATE EVENT SESSION code examples

Column name

Description

The ID of the event session. Is not nullable.

The ID of the event. This ID is unique within an event session object. Is not

The name of the event. Is not nullable.

The name of the event package that contains the event. Is not nullable.

The name of the module that contains the event. Is not nullable.

nvarchar(3000)

The predicate expression that is applied to the event. Is nullable.

nvarchar(3000)

The XML predicate expression that is applied to the event. Is nullable.

Requires the VIEW DATABASE PERFORMANCE STATE permission.

This view has the following relationship cardinalities.

Relationship

Many to one

Expand table

Expand table

sys.database_event_session_events (Azure SQL Database and Azure SQL Managed Instance)

Monitoring Microsoft Azure SQL Database and Azure SQL Managed Instance performance using

dynamic management views
