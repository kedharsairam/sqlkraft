---
title: "Rebuild System Databases"
topic: "collation"
description: |
  Article

  •

  07/22/2024

  Applies to:

  SQL Server

  System databases must be rebuilt to fix corruption problems in the

  master

  ,

  model

  ,

  msdb

  , or

  resource

  system databases, or to modify the defau
tags:
  - "collation"
  - "rebuild-system-databases"
pubDate: 2025-12-01
---

Article

•

07/22/2024

Applies to:

SQL Server

System databases must be rebuilt to fix corruption problems in the

master

,

model

,

msdb

, or

resource

system databases, or to modify the default server-level collation. This article provides

step-by-step instructions to rebuild system databases in SQL Server.

This article is unrelated to

rebuilding indexes

.

When the

,

,

, and

system databases are rebuilt, the databases are

dropped and recreated in their original location. If a new collation is specified in the rebuild

statement, the system databases are created using that collation setting. Any user

modifications to these databases are lost. For example, you might have user-defined objects in

the

database, scheduled jobs in

, or changes to the default database settings in

the

database.

Perform the following tasks before you rebuild the system databases to ensure that you can

restore the system databases to their current settings.

1. Record all server-wide configuration values.

2. Record all hotfixes applied to the instance of SQL Server and the current collation. You

must reapply these hotfixes after rebuilding the system databases.

```sql
master model msdb tempdb master msdb model
SELECT
*
FROM sys.configurations;
SELECT
SERVERPROPERTY(
'ProductVersion '
)
AS
ProductVersion,
SERVERPROPERTY(
'ProductLevel'
)
AS
ProductLevel,
SERVERPROPERTY(
'ResourceVersion'
)
AS
ResourceVersion,
SERVERPROPERTY(
'ResourceLastUpdateDateTime'
)
AS
ResourceLastUpdateDateTime,
SERVERPROPERTY(
'Collation'
)
AS
Collation
;
```
