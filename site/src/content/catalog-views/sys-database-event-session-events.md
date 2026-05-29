---
name: 'sys.database_event_session_events'
title: 'sys.database_event_session_events'
category: 'objects'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure SQL

Managed Instance

SQL database in Microsoft Fabric

The

dynamic management view (DMV) returns a row for each event

in a database-scoped event session. For information on events in

active

database-scoped sessions, see

sys.dm_xe_database_session_events

.

Azure SQL Database and SQL database in Fabric support only

database-scoped sessions

.

Azure SQL Managed Instance supports both database-scoped sessions and

server-scoped

sessions

. Server-scoped sessions are recommended for SQL managed instances. For more

information, see

CREATE EVENT SESSION code examples

.

Column name

Data type


## Description
int

The ID of the event session. Is not nullable.

int

The ID of the event. This ID is unique within an event session object. Is not

nullable.

sysname

The name of the event. Is not nullable.

sysname

The name of the event package that contains the event. Is not nullable.

sysname

The name of the module that contains the event. Is not nullable.

nvarchar(3000)

The predicate expression that is applied to the event. Is nullable.

nvarchar(3000)

The XML predicate expression that is applied to the event. Is nullable.

Requires the VIEW DATABASE PERFORMANCE STATE permission.

This view has the following relationship cardinalities.

From

To

Relationship

Many to one

ﾉ

Expand table

ﾉ

Expand table

Learn more about related concepts in the following articles:

Extended events in Azure SQL Database

Event File target code for extended events in Azure SQL Database and SQL Managed Instance

sys.database_event_sessions (Azure SQL Database and Azure SQL Managed Instance)

sys.database_event_session_actions (Azure SQL Database and Azure SQL Managed Instance)

Monitoring Microsoft Azure SQL Database and Azure SQL Managed Instance performance using

dynamic management views

Last updated on 11/18/2025

Related content

```sql
sys.database_event_session_events
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
predicate
```

```sql
predicate_xml
```

```sql
sys.database_event_session_events.event_session_id
sys.database_event_sessions.event_session_id
```
