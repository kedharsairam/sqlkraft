---
name: 'sys.server_event_session_actions'
title: 'sys.server_event_session_actions (Transact-'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

SQL)

09/24/2025

Applies to:

SQL Server

Azure SQL Managed Instance


## Returns a row for each action on each event of an event session.
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

SQL Server 2019 (15.x) and previous versions require

permission on the server.

SQL Server 2022 (16.x) and later versions require

permission on the server.

This view has the following relationship cardinalities.

From

To

Relationship

Many to one

Many to one

System catalog views (Transact-SQL)

Extended Events Catalog Views (Transact-SQL)

Extended Events overview

ﾉ

Expand table

ﾉ

Expand table

Related content

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
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

```sql
sys.server_event_session_actions.event_session_id
sys.server_event_sessions.event_session_id
```

```sql
sys.server_event_session_actions.event_id
sys.server_event_session_actions.event_session_id
sys.server_event_session_events.event_session_id
sys.server_event_session_events.event_id
```
