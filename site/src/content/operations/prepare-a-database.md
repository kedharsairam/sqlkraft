---
title: "Prepare a database"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  Before a database mirroring session can start, the database owner or system administrator

  must make sure that the mirror database has been created and is ready for mirroring.
tags:
  - "high-availability"
  - "prepare-a-database"
pubDate: 2025-12-01
---

SQL Server

Before a database mirroring session can start, the database owner or system administrator

must make sure that the mirror database has been created and is ready for mirroring. Creating

a new mirror database minimally requires taking a full backup of the principal database and a

subsequent log backup and restoring them both onto the mirror server instance, using WITH

NORECOVERY.

This topic describes how to prepare a mirror database in SQL Server by using SQL Server

Management Studio or Transact-SQL.

Requirements

Limitations and Restrictions

Recommendations

Security

To Prepare an Existing Mirror Database to Restart Mirroring

Ｕ

Caution

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

For high availability, use Always On availability groups instead.

）

Important

Database Mirroring in SQL Server is a distinct technology from. Mirroring to Fabric provides better analytical performance, the ability to unify

your data estate with OneLake in Fabric, and open access to your data in Delta Parquet

format.

With Mirroring to Microsoft Fabric, you can continuously replicate your existing data

estate directly into OneLake in Fabric, including data from SQL Server 2016+, Azure SQL

Database, Azure SQL Managed Instance, Cosmos DB, Oracle, Snowflake, and more.
