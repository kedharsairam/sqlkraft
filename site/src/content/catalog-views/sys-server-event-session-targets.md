---
name: 'sys.server_event_session_targets'
title: 'sys.server_event_session_targets'
category: 'compatibility'
description: 'Azure SQL Managed Instance Returns a row for each event target for an event session. The ID of the event session. Is not nullable. The ID of the target. ID is unique within the event session object. Is not The name of the event target. Is not nullable. The name of the event package that contains the event target. Is not nullable. The name of the module that contains the event target. Is not nullab'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: 'VIEW SERVER PERFORMANCE STATE'
---

## Description

Azure SQL Managed Instance Returns a row for each event target for an event session. The ID of the event session. Is not nullable. The ID of the target. ID is unique within the event session object. Is not The name of the event target. Is not nullable. The name of the event package that contains the event target. Is not nullable. The name of the module that contains the event target. Is not nullable. SQL Server 2019 (15.x) and previous versions require permission on the server. SQL Server 2022 (16.x) and later versions require permission on the This view has the following relationship cardinalities. System catalog views (Transact-SQL) Related content

## Syntax

```sql
VIEW SERVER PERFORMANCE STATE
```

## Remarks

Applies to:

Azure SQL Managed Instance

Returns a row for each event target for an event session.

Column name

Description

The ID of the event session. Is not nullable.

The ID of the target. ID is unique within the event session object. Is not

The name of the event target. Is not nullable.

The name of the event package that contains the event target. Is not nullable.

The name of the module that contains the event target. Is not nullable.

SQL Server 2019 (15.x) and previous versions require

permission on the server.

SQL Server 2022 (16.x) and later versions require

permission on the

This view has the following relationship cardinalities.

Relationship

Many to one

System catalog views (Transact-SQL)

Expand table

Expand table

Related content
