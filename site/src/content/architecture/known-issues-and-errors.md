---
title: "Known issues and errors"
topic: "change-data-capture"
description: |
  10/07/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article explains known limitations, issues, and errors with change data capture (CDC) for

  SQL Server

  and

  .

  For Azure SQL Datab
tags:
  - "change-data-capture"
  - "known-issues-and-errors"
pubDate: 2025-12-01
---

10/07/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article explains known limitations, issues, and errors with change data capture (CDC) for

SQL Server

and

.

For Azure SQL Database, see

Known issues with CDC in Azure SQL Database

.

For CDC to function properly, you shouldn't manually modify any CDC metadata such as

, change tables, CDC system stored procedures, default

permissions

(

sys.database_principals

) or rename the

.

Any objects in

sys.objects

with

property set to

shouldn't be modified.

It's important to be aware of a situation where you have different collations between the

database and the columns of a table configured for change data capture. CDC uses interim

storage to populate side tables. If a table has

or

columns with collations that are

different from the database collation, and if those columns store non-ASCII characters (such as

double byte DBCS characters), CDC might not be able to persist the changed data consistent

with the data in the base tables. This is because the interim storage variables can't have

collations associated with them.

Consider one of the following approaches to ensure captured change data is consistent with

base tables:

```sql
CDC schema cdc user cdc user is_ms_shipped
1
SELECT name
AS object_name
,SCHEMA_NAME(schema_id)
AS schema_name
,type_desc
,is_ms_shipped
FROM sys.objects
WHERE is_ms_shipped= 1
AND
SCHEMA_NAME(schema_id) =
'cdc'
```
