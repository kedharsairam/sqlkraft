---
name: "Compatibility levels and database engine upgrades"
title: "Compatibility levels and database engine upgrades"
category: "operators"
description: "performance differences of your most important queries between two different compatibility"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

performance differences of your most important queries between two different compatibility

levels on Azure SQL Database, see

Improved Query Performance with Compatibility Level 130

in Azure SQL Database

. This article refers to compatibility level 130 and SQL Server, but the

same methodology applies for upgrades to 140 or higher levels in SQL Server and Azure SQL

Database.

Not all features that vary by compatibility level are supported on Azure SQL Database.

To determine the current compatibility level, query the

column of

sys.databases

.

To determine the version of the Database Engine that you're connected to, execute the

following query.

Database compatibility level is a valuable tool to help with database modernization by allowing

the SQL Server Database Engine to be upgraded while keeping the same functional status for

connecting applications by maintaining the same pre-upgrade database compatibility level.

This means that it's possible to upgrade from an older version of SQL Server (such as SQL

Server 2008 (10.0.x)) to SQL Server or Azure SQL Database (including Azure SQL Managed

Instance) with no application changes (except for database connectivity). For more information,

see

Compatibility certification

.

As long as the application doesn't need to use enhancements that are only available in a higher

database compatibility level, it's a valid approach to upgrade the SQL Server Database Engine

and maintain the previous database compatibility level. For more information on using

compatibility level for backward compatibility, see

Compatibility certification

.

### Discontinued

### not

### Breaking changes

### might not

### not

### protected

`compatibility_level`

```sql
SELECT
[
name
],
compatibility_level
FROM sys.databases;
SELECT
SERVERPROPERTY(
'ProductVersion'
);
```
