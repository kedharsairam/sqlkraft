---
title: "Query data"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  When you want to get latest (current) state of data in a temp
tags:
  - "tables"
  - "query-data"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

When you want to get latest (current) state of data in a temporal table, you can query the same

way as you query a non-temporal table. If the

columns aren't hidden, their values

appear in a

query. If you specified

columns as

, their values don't

appear in a

query. When the

columns are hidden, you must reference the

columns specifically in the

clause to return the values for these columns.

To perform any type of time-based analysis, use the new

clause with four

temporal-specific subclauses to query data across the current and history tables. For more

information on these clauses, see

Temporal tables

and

FROM clause plus JOIN, APPLY, PIVOT

can be specified independently for each table in a query. It can be used inside

common table expressions, table-valued functions, and stored procedures. When using a table

alias with a temporal table, the

clause must be included between the

temporal table name and the alias (see

Query for a specific time using the AS OF subclause

second example).

Use the

subclause when you need to reconstruct state of data as it was at any specific

time in the past. You can reconstruct the data with the precision of datetime2 type that was

specified in

column definitions.

The

subclause can be used with constant literals or with variables, so that you can

dynamically specify the time condition. The values provided are interpreted as UTC time.

This first example returns the state of the dbo.Department table

a specific date in the

past.

```sql
PERIOD
SELECT *
PERIOD
HIDDEN
SELECT *
PERIOD
PERIOD
SELECT
FOR SYSTEM_TIME
AS OF <date_time>
FROM <start_date_time> TO <end_date_time>
BETWEEN <start_date_time> AND <end_date_time>
CONTAINED IN (<start_date_time>, <end_date_time>)
ALL
FOR SYSTEM_TIME
FOR SYSTEM_TIME
AS OF
PERIOD
AS OF
AS OF
```
