---
title: "Use the Trustworthy Property"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  When a database is backed up, the TRUSTWORTHY database property is set to OFF. Therefore,

  on a new mirror database TRUSTWORTHY is always OFF. If the database needs to be

  tru
tags:
  - "high-availability"
  - "use-the-trustworthy-property"
pubDate: 2025-12-01
---

Applies to:

SQL Server

When a database is backed up, the TRUSTWORTHY database property is set to OFF. Therefore,

on a new mirror database TRUSTWORTHY is always OFF. If the database needs to be

trustworthy after a failover, extra setup steps are necessary after mirroring begins.

For information about this database property, see

TRUSTWORTHY Database Property

.

1. On the principal server instance, verify that the principal database has the Trustworthy

property turned on.

For more information, see

sys.databases (Transact-SQL)

.

Ｕ

Caution

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

For high availability, use Always On availability groups instead.

）

Important

Database Mirroring in SQL Server is a distinct technology from

. Mirroring to Fabric provides better analytical performance, the ability to unify

your data estate with OneLake in Fabric, and open access to your data in Delta Parquet

format.

With Mirroring to Microsoft Fabric, you can continuously replicate your existing data

estate directly into OneLake in Fabric, including data from SQL Server 2016+, Azure SQL

Database, Azure SQL Managed Instance, Cosmos DB, Oracle, Snowflake, and more.

```cmd
SELECT name, database_id, is_trustworthy_on FROM sys.databases
```
