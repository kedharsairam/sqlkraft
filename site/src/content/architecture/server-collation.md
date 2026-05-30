---
title: "Server Collation"
topic: "collation"
description: |
  Article

  •

  04/05/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  The server collation acts as the default collation for all system databases that are installed with

  the instance of SQL Se
tags:
  - "collation"
  - "server-collation"
pubDate: 2025-12-01
---

Article

•

04/05/2024

Applies to:

SQL Server

Azure SQL Managed Instance

The server collation acts as the default collation for all system databases that are installed with

the instance of SQL Server, and also any newly created user databases.

You should carefully consider the server-level collation, because it can affect:

Sorting and comparison rules in

,

,

and other operators that compare

textual data.

Collation of the

,

,

, and

columns in system views, system

functions, and the objects in

(for example, temporary tables).

Names of the variables, cursors, and

labels. For example, the variables

and

are considered as different variables if the server-level collation is case-sensitive, and the

same variables if the server-level collation is case-insensitive.

The server collation is specified during SQL Server installation. The default server-level collation

is based upon the locale of the operating system.

For example, the default collation for systems using US English (en-US) is

SQL_Latin1_General_CP1_CI_AS

. For more information, including the list of OS locale to default

collation mappings, see the "Server-level collations" section of

Collation and Unicode Support

.

Changing the default collation for an instance of SQL Server can be a complex operation.

７

Note

The server-level collation for SQL Server Express LocalDB is

SQL_Latin1_General_CP1_CI_AS

and cannot be changed, either during or after installation.

７

Note

Instead of changing the default collation of an instance of SQL Server, you can specify a

default collation for each new database you create via the

clause of the

```sql
=
JOIN
ORDER BY
CHAR
VARCHAR
NCHAR
NVARCHAR
tempdb
GOTO
@pi
@PI
COLLATE
CREATE
```
