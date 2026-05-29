---
title: 'Enable and disable'
topic: 'query-processing'
description: 'The following table summarizes the availability and the enabled state of optimized locking'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

The following table summarizes the availability and the enabled state of optimized locking

across SQL platforms.

Azure SQL Database

Yes

Yes (always enabled)

SQL database in Microsoft Fabric

Yes

Yes (always enabled)

Azure SQL Managed Instance

Yes

Yes (always enabled)

Azure SQL Managed Instance

Yes

Yes (always enabled)

Azure SQL Managed Instance

No

N/A

SQL Server 2025 (17.x)

Yes

No (can be enabled per database)

SQL Server 2022 (16.x) and older versions

No

N/A

To enable or disable optimized locking for a SQL Server database, use the

command. For more information, see

ALTER DATABASE SET

options

.

Optimized locking builds on other database features:

You must enable

accelerated database recovery (ADR)

on a database before you can

enable optimized locking. Conversely, to disable ADR, you must disable optimized locking

first if it's enabled.

For the most benefit from optimized locking,

read committed snapshot isolation (RCSI)

should be enabled for the database. The

LAQ

component of optimized locking is in effect

only if RCSI is enabled.

ADR is always enabled in Azure SQL Database, Azure SQL Managed Instance, and SQL

database in Microsoft Fabric. RCSI is enabled by default in Azure SQL Database and SQL

database in Microsoft Fabric.

To verify that these options are enabled for your current database, connect to the database and

run the following T-SQL query:

ﾉ

Expand table

AUTD

2025

2022

```sql
ALTER DATABASE ...
SET OPTIMIZED_LOCKING = ON | OFF
```
