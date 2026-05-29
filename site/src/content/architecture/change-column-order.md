---
title: "Change Column Order"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  Analytics Platform System (PDW)

  SQL database in Microsoft

  Fabric

  You can change the order of
tags:
  - "tables"
  - "change-column-order"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

You can change the order of columns in

in SQL Server Management Studio

(SSMS). By default, a safety mechanism of SSMS blocks changing the column order. Though it

isn't recommended, you can change the column order in a table by re-creating the table.

Adding columns to a table

by default adds them to the end of the table, as is recommended.

Best practices with table column order:

To change the order of columns displayed in a result set, report, or application, use the

column order in a

SELECT (Transact-SQL)

statement. Always specify the columns by name

in your queries and applications in the order in which you would like them to appear.

Don't use

in applications. Added or removed columns could cause unexpected

behavior or errors in applications.

Add new columns to the end of tables.

Though not recommended, you can change the order of columns in a table using SQL Server

Management Studio (SSMS). This requires recreating the table.

Ｕ

Caution

Changing the column order of a table may affect code and applications that depend on

the specific order of columns. These include queries, views, stored procedures, user-

defined functions, and client applications. Carefully consider any changes you want to

make to column order.

）

Important

```sql
SELECT *
```
