---
name: "The modify method"
title: "The modify method"
category: "statements"
description: "JSON function support was first introduced in SQL Server 2016 (13.x). The native"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

JSON function support was first introduced in SQL Server 2016 (13.x). The native

type was

introduced in Azure SQL Database and Azure SQL Managed Instance, and is also available in

2025 (17.x).

The

data type is available under all database compatibility levels.

The

data type supports the

method. Use

to modify JSON documents

stored in a column. The

method has optimizations to perform in-place modifications to

the data where possible, and is the preferred way to modify a JSON document in a

column.

For JSON strings, if the new value is less than or equal to the existing value, then in-place

modification is possible.

For JSON numbers, if the new value is of the same type, or within the range of the existing

value, then in-place modification is possible.

７

Note

The

:

is generally available for Azure SQL Database and Azure SQL Managed Instance with

the

2025

or.

is in preview for SQL Server 2025 (17.x) and SQL database in Fabric.

７

Note

The

method is currently in preview and only available in SQL Server 2025 (17.x).

### json

### json

`modify`

`modify`

`modify`

```sql
CREATE
TABLE
Orders (
order_id
INT
,
order_details
JSON
NOT
NULL
CHECK (JSON_PATH_EXISTS(order_details,
'$.basket'
) = 1)
);
```

`modify`
