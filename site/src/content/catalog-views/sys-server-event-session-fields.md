---
name: 'sys.server_event_session_fields'
title: 'sys.server_event_session_fields'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

09/24/2025

Applies to:

SQL Server

Azure SQL Managed Instance


## Returns a row for each customizable column that was explicitly set on events and targets.
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

Many to one

System catalog views (Transact-SQL)

ﾉ

Expand table

ﾉ

Expand table

Related content

Extended Events Catalog Views (Transact-SQL)

Extended Events overview

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
sys.server_event_session_actions.object_id
sys.server_event_session_actions.event_session_id
sys.server_event_session_events.event_session_id
sys.server_event_session_events.event_id
```

```sql
sys.server_event_session_actions.event_session_id
sys.server_event_session_actions.object_id
sys.server_event_session_targets.event_session_id
sys.server_event_session_targets.target_id
```
