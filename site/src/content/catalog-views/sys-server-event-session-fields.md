---
name: "sys.server_event_session_fields"
title: "sys.server_event_session_fields"
category: "compatibility"
description: "Azure SQL Managed Instance Returns a row for each customizable column that was explicitly set on events and targets. The ID of the event session. Is not nullable. The ID of the object this field is associated with. Is not nullable. The name of the field. Is not nullable. The value of the field. Is not nullable. SQL Server 2019 (15.x) and previous versions require permission on the server. SQL Serv"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "VIEW SERVER PERFORMANCE STATE"
---

## Description

Azure SQL Managed Instance Returns a row for each customizable column that was explicitly set on events and targets. The ID of the event session. Is not nullable. The ID of the object this field is associated with. Is not nullable. The name of the field. Is not nullable. The value of the field. Is not nullable. SQL Server 2019 (15.x) and previous versions require permission on the server. SQL Server 2022 (16.x) and later versions require permission on the server. This view has the following relationship cardinalities. System catalog views (Transact-SQL) Related content

## Syntax

```sql
VIEW SERVER PERFORMANCE STATE
```

## Remarks

Applies to:

Azure SQL Managed Instance

Returns a row for each customizable column that was explicitly set on events and targets.

Column name

Description

The ID of the event session. Is not nullable.

The ID of the object this field is associated with. Is not nullable.

The name of the field. Is not nullable.

sql_variant

The value of the field. Is not nullable.

SQL Server 2019 (15.x) and previous versions require

permission on the server.

SQL Server 2022 (16.x) and later versions require

permission on the server.

This view has the following relationship cardinalities.

Relationship

Many to one

Many to one

Many to one

System catalog views (Transact-SQL)

Expand table

Expand table

Related content
