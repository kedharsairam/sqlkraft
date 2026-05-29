---
name: 'sys.database_event_session_actions'
title: 'sys.database_event_session_actions (Azure SQL Database)'
category: 'compatibility'
description: 'SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed SQL database in Microsoft Fabric dynamic management view (DMV) returns a row for each action on each event of a database-scoped event session. For information on actions in database-scoped event sys.dm_xe_database_session_event_actions Azure SQL Database and SQL database in Fabric support only database-scoped sessions A'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: 'sys.database_event_session_actions'
---

## Description

SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed SQL database in Microsoft Fabric dynamic management view (DMV) returns a row for each action on each event of a database-scoped event session. For information on actions in database-scoped event sys.dm_xe_database_session_event_actions Azure SQL Database and SQL database in Fabric support only database-scoped sessions Azure SQL Managed Instance supports both database-scoped sessions and server-scoped sessions Server-scoped sessions are recommended for SQL managed instances. For more information, see CREATE EVENT SESSION code examples The ID of the event session. Is not nullable. The ID of the event. This ID is unique within the event session object. Is not nullable. The name of the action. Is nullable. The name of the event package that contains the event. Is nullable.

## Syntax

```sql
sys.database_event_session_actions
```

## Remarks

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure SQL Managed

SQL database in Microsoft Fabric

dynamic management view (DMV) returns a row for each action on

each event of a database-scoped event session. For information on actions in

database-scoped event

sessions, see

sys.dm_xe_database_session_event_actions

Azure SQL Database and SQL database in Fabric support only

database-scoped sessions

Azure SQL Managed Instance supports both database-scoped sessions and

server-scoped sessions

Server-scoped sessions are recommended for SQL managed instances. For more information, see

CREATE EVENT SESSION code examples

Column name

Description

The ID of the event session. Is not nullable.

The ID of the event. This ID is unique within the event session object. Is not nullable.

The name of the action. Is nullable.

The name of the event package that contains the event. Is nullable.

The name of the module that contains the event. Is nullable.

Requires the VIEW DATABASE PERFORMANCE STATE permission.

This view has the following relationship cardinalities.

Relationship

Many to one

Many to one

Extended events in Azure SQL Database

Monitoring Microsoft Azure SQL Database performance using dynamic management views

Expand table

Expand table

Related content
