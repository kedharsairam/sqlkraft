---
title: "Add using Windows authentication"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  To set up a witness for a database, the database owner assigns a Database Engine instance to

  the role of witness server. The witness server instance can run on the same compu
tags:
  - "high-availability"
  - "add-using-windows-authentication"
pubDate: 2025-12-01
---

Applies to:

SQL Server

To set up a witness for a database, the database owner assigns a Database Engine instance to

the role of witness server. The witness server instance can run on the same computer as the

principal or mirror server instance, but this substantially reduces the robustness of automatic

failover.

We strongly recommend that the witness reside on a separate computer. A given server can

participate in multiple concurrent database mirroring sessions with the same or different

partners. A given server can be a partner in some sessions and a witness in other sessions.

The witness is intended exclusively for high-safety mode with automatic failover. Before you set

a witness, we strongly recommend that you ensure that the SAFETY property is currently set to

FULL.

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

）

Important

We recommend that you configure database mirroring during off-peak hours because

configuration can impact performance.
