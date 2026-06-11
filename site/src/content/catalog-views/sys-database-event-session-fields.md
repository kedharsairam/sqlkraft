---
name: "sys.database_event_session_fields"
title: "sys.database_event_session_fields (Azure SQL Database)"
category: "compatibility"
description: "SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed SQL database in Microsoft Fabric dynamic management view (DMV) returns a row for each customizable column that was explicitly set on in a database-scoped event session."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.database_event_session_fields"
---

## Description

SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed SQL database in Microsoft Fabric dynamic management view (DMV) returns a row for each customizable column that was explicitly set on in a database-scoped event session. Azure SQL Database and SQL database in Fabric support only database-scoped sessions Azure SQL Managed Instance supports both database-scoped sessions and server-scoped sessions Server-scoped sessions are recommended for SQL managed instances. For more information, see EVENT SESSION code examples The ID of the event session. Is not nullable. The ID of the object this field is associated with. Is not nullable. The name of the field. Is not nullable. The value of the field. Is not nullable. Requires the VIEW DATABASE PERFORMANCE STATE permission. This view has the following relationship cardinalities.

## Syntax

`sys.database_event_session_fields`

## Remarks

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure SQL Managed

SQL database in Microsoft Fabric

dynamic management view (DMV) returns a row for each

customizable column that was explicitly set on

in a database-scoped event session.

Azure SQL Database and SQL database in Fabric support only

database-scoped sessions

Azure SQL Managed Instance supports both database-scoped sessions and

server-scoped sessions

Server-scoped sessions are recommended for SQL managed instances. For more information, see

EVENT SESSION code examples

Column name

Description

The ID of the event session. Is not nullable.

The ID of the object this field is associated with. Is not nullable.

The name of the field. Is not nullable.

sql_variant

The value of the field. Is not nullable.

Requires the VIEW DATABASE PERFORMANCE STATE permission.

This view has the following relationship cardinalities.

Relationship

Many to one

Many to one

Many to one

Expand table

Expand table

Related content
