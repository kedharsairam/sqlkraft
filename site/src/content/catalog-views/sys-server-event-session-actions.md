---
name: "sys.server_event_session_actions"
title: "sys.server_event_session_actions"
category: "compatibility"
description: "Azure SQL Managed Instance Returns a row for each action on each event of an event session. The ID of the event session. Is not nullable. The ID of the event. This ID is unique within the event session object. Is not nullable."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "VIEW SERVER PERFORMANCE STATE"
---

## Description

Azure SQL Managed Instance Returns a row for each action on each event of an event session. The ID of the event session. Is not nullable. The ID of the event. This ID is unique within the event session object. Is not nullable. The name of the action. Is nullable. The name of the event package that contains the event. Is nullable. The name of the module that contains the event. Is nullable. SQL Server 2019 (15.x) and previous versions require permission on the server. SQL Server 2022 (16.x) and later versions require permission on the server. This view has the following relationship cardinalities. System catalog views (Transact-SQL) Extended Events Catalog Views (Transact-SQL) Extended Events overview Related content

## Syntax

```sql
VIEW SERVER PERFORMANCE STATE
```

## Remarks

Applies to:

Azure SQL Managed Instance

Returns a row for each action on each event of an event session.

Column name

Description

The ID of the event session. Is not nullable.

The ID of the event. This ID is unique within the event session object. Is not nullable.

The name of the action. Is nullable.

The name of the event package that contains the event. Is nullable.

The name of the module that contains the event. Is nullable.

SQL Server 2019 (15.x) and previous versions require

permission on the server.

SQL Server 2022 (16.x) and later versions require

permission on the server.

This view has the following relationship cardinalities.

Relationship

Many to one

Many to one

System catalog views (Transact-SQL)

Extended Events Catalog Views (Transact-SQL)

Extended Events overview

Expand table

Expand table

Related content
