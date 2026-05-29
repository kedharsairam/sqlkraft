---
name: 'sys.server_event_session_events'
title: 'sys.server_event_session_events (Transact-'
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


## Returns a row for each event in an event session.

## Description
The ID of the event session. Is not nullable.

The ID of the event. This ID is unique within an event session object. Is

not nullable.

The name of the event. Is not nullable.

The name of the event package that contains the event. Is not nullable.

The name of the module that contains the event. Is not nullable.

The predicate expression that is applied to the event. Is nullable.

The XML predicate expression that is applied to the event. Is nullable.

SQL Server 2019 (15.x) and previous versions require

permission on the server.

SQL Server 2022 (16.x) and later versions require

permission on the

server.

This view has the following relationship cardinalities.

Many to one

ﾉ

Expand table

ﾉ

Expand table

System catalog views (Transact-SQL)

Extended Events Catalog Views (Transact-SQL)

Extended Events overview

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
predicate
```

```sql
predicate_xml
```

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

```sql
sys.server_event_session_events.event_session_id
sys.server_event_sessions.event_session_id
```
