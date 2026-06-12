---
title: "Rename Columns"
topic: "tables"
description: "2016 (13.x) and later versions Azure SQL Managed Instance You can rename a table column in SQL Server by using SQL Serv"
tags: ["tables","rename-columns"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

You can rename a table column in SQL Server by using SQL Server Management Studio or

Transact-SQL.

Renaming a column doesn't automatically rename references to that column. You must modify

any objects that reference the renamed column manually. For example, if you rename a table

column and that column is referenced in a trigger, you must modify the trigger to reflect the

new column name. Use

sys.sql_expression_dependencies

to list dependencies on the object

before renaming it.

Renaming a column doesn't automatically update the metadata for any objects which

all columns (using

) from that table. For example, if you rename a table column, and that

column is referenced by a non-schema-bound view or function that selects all columns (using

), the metadata for the view or function continues to reflect the original column name.

Refresh the metadata using

sp_refreshsqlmodule

or

sp_refreshview.

Requires

permission on the object.

1. In

, connect to an instance of Database Engine.

2. In

, right-click the table in which you want to rename columns and choose.

3. Type a new column name.

1. In

, right-click the table to which you want to rename columns and

choose.

```sql
SELECT
*
*
ALTER
```
