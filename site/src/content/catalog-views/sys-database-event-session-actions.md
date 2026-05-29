---
name: 'sys.database_event_session_actions'
title: 'sys.database_event_session_actions'
category: 'objects'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure SQL Managed

Instance

SQL database in Microsoft Fabric

The

dynamic management view (DMV) returns a row for each action on

each event of a database-scoped event session. For information on actions in

active

database-scoped event

sessions, see

sys.dm_xe_database_session_event_actions

.

Azure SQL Database and SQL database in Fabric support only

database-scoped sessions

.

Azure SQL Managed Instance supports both database-scoped sessions and

server-scoped sessions

.

Server-scoped sessions are recommended for SQL managed instances. For more information, see

CREATE EVENT SESSION code examples

.

Column name

Data type


## Description
int

The ID of the event session. Is not nullable.

int

The ID of the event. This ID is unique within the event session object. Is not nullable.

sysname

The name of the action. Is nullable.

sysname

The name of the event package that contains the event. Is nullable.

sysname

The name of the module that contains the event. Is nullable.

Requires the VIEW DATABASE PERFORMANCE STATE permission.

This view has the following relationship cardinalities.

From

To

Relationship

Many to one

Many to one

Extended events in Azure SQL Database

Monitoring Microsoft Azure SQL Database performance using dynamic management views

ﾉ

Expand table

ﾉ

Expand table

Related content

Extended events overview (SQL Server and Azure SQL Managed Instance)

Last updated on 11/18/2025

```sql
sys.database_event_session_actions
```

```sql
event_session_id
```

```sql
event_id
```

```sql
name
```

```sql
package
```

```sql
module
```

```sql
sys.database_event_session_actions.event_session_id
sys.database_event_sessions.event_session_id
```

```sql
sys.database_event_session_actions.event_id
sys.database_event_session_actions.event_session_id
sys.database_event_session_events.event_session_id
sys.database_event_session_events.event_id
```
