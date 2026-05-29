---
title: "Modified Features"
topic: "collation"
description: |
  Article

  •

  04/15/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  The following features have been modified to be supported by a partially contained database.

  Features are usually modified
tags:
  - "collation"
  - "modified-features"
pubDate: 2025-12-01
---

Article

•

04/15/2024

Applies to:

SQL Server

Azure SQL Managed Instance

The following features have been modified to be supported by a partially contained database.

Features are usually modified so they do not cross the database boundary.

For more information, see

Contained Databases

.

When using the ALTER DATABASE statement from inside of a contained database, the syntax

differs from that used for a non-contained database. This difference includes restrictions of

elements of the statement that extend beyond the database to the instance. For more

information, see

ALTER DATABASE (Transact-SQL)

.

The syntax for the ALTER DATABASE when used outside of a contained database differs from

that used for non-contained databases. These changes prevent crossing the database

boundary. For more information, see

ALTER DATABASE (Transact-SQL)

.

The CREATE DATABASE syntax for a contained database differs from that for a non-contained

database. See

CREATE DATABASE (SQL Server Transact-SQL)

for information about new syntax

requirements and allowances.

Local temporary tables are permitted within a contained database, but their behavior differs

from those in non-contained databases. In non-contained databases, temporary table data is

collated in the collation of

. In a contained database temporary table data is collated in

the collation of the contained database.

All metadata associated with temporary tables (for example, table and column names, indexes,

and so on) will be in the catalog collation.
