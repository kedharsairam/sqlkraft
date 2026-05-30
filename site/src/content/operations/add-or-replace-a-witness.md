---
title: "Add or replace a witness"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  If the database mirroring endpoints use Windows Authentication, you can use SQL Server

  Management Studio to add or replace a witness. Adding a witness in Management Studio al
tags:
  - "high-availability"
  - "add-or-replace-a-witness"
pubDate: 2025-12-01
---

Applies to:

SQL Server

If the database mirroring endpoints use Windows Authentication, you can use SQL Server

Management Studio to add or replace a witness. Adding a witness in Management Studio also

changes the operating mode to high-safety mode with automatic failover.

1. After connecting to the principal server instance, in Object Explorer, click the server name

to expand the server tree.

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

７

Note

We strongly recommend that the witness reside on a separate computer from either of

the partners. The service account used by the witness must be in the same domain as the

service accounts used by the principal and mirror server instances, or it must be in a

trusted domain.
