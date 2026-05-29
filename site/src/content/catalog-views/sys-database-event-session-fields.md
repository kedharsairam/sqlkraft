---
name: 'sys.database_event_session_fields'
title: 'sys.database_event_session_fields'
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

dynamic management view (DMV) returns a row for each

customizable column that was explicitly set on

events

and

targets

in a database-scoped event session.

Azure SQL Database and SQL database in Fabric support only

database-scoped sessions

.

Azure SQL Managed Instance supports both database-scoped sessions and

server-scoped sessions

.

Server-scoped sessions are recommended for SQL managed instances. For more information, see

CREATE

EVENT SESSION code examples

.

Column name

Data type


## Description
int

The ID of the event session. Is not nullable.

int

The ID of the object this field is associated with. Is not nullable.

sysname

The name of the field. Is not nullable.

sql_variant

The value of the field. Is not nullable.

Requires the VIEW DATABASE PERFORMANCE STATE permission.

This view has the following relationship cardinalities.

From

To

Relationship

Many to one

Many to one

Many to one

ﾉ

Expand table

ﾉ

Expand table

Related content

Extended events in Azure SQL Database

Event File target code for extended events in Azure SQL Database and SQL Managed Instance

sys.database_event_sessions (Azure SQL Database and Azure SQL Managed Instance)

sys.database_event_session_actions (Azure SQL Database and Azure SQL Managed Instance)

Monitoring Microsoft Azure SQL Database and Azure SQL Managed Instance performance using dynamic

management views

Last updated on 11/18/2025

```sql
sys.database_event_session_fields
```

```sql
event_session_id
```

```sql
object_id
```

```sql
name
```

```sql
value
```

```sql
sys.database_event_session_actions.event_session_id
sys.database_event_sessions.event_session_id
```

```sql
sys.database_event_session_actions.event_id
sys.database_event_session_actions.object_id
sys.database_event_session_actions.event_session_id
sys.database_event_session_events.event_session_id
sys.database_event_session_events.event_id
```

```sql
sys.database_event_session_actions.event_session_id
sys.database_event_session_actions.object_id
sys.database_event_session_targets.event_session_id
sys.database_event_session_targets.target_id
```
