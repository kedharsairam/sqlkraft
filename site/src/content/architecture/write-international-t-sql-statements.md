---
title: "Write International T-SQL Statements"
topic: "collation"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  SQL database in Microsoft

  Fabric

  Databases and database application
tags:
  - "collation"
  - "write-international-t-sql-statements"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

Databases and database applications that use Transact-SQL statements will become more

portable from one language to another, or will support multiple languages, if the following

guidelines are followed:

Starting with SQL Server 2019 (15.x) and in Azure SQL Database, use either:

The

,

, and

data types with a

UTF-8

enabled collation, and

data is encoded using UTF-8.

The

,

, and

data types with

supplementary character (SC)

enabled collation, and data is encoded using UTF-16. Using a non-SC collation results

in data being encoded using UCS-2.

This avoids code page conversion issues. For other considerations, see

Storage

differences between UTF-8 and UTF-16

.

Up to SQL Server 2017 (14.x), replace all uses of the

,

, and

data

types with

,

, and

. If using a

supplementary character (SC)

enabled collation, data is encoded using UTF-16. Using a non-SC collation results in data

being encoded using UCS-2. This avoids code page conversion issues. For more

information, see

Collation and Unicode Support

.

When doing month and day-of-week comparisons and operations, use the numeric date

parts instead of the name strings. Different language settings return different names for

the months and weekdays. For example,

returns

when

the language is set to U.S. English, returns

when the language is set to German, and

returns

when the language is set to French. Instead, use a function such as

DATEPART

that uses the number of the month instead of the name. Use the DATEPART names when

you build result sets to be displayed to a user, because the date names are frequently

more meaningful than a numeric representation. However, don't code any logic that

depends on the displayed names being from a specific language.

）

Important

The

data type is deprecated and should not be used in new development work.

Plan to convert

data to

.

```sql
DATENAME(MONTH,GETDATE())
May
Mai mai
```
