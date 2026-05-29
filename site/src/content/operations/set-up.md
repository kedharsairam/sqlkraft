---
title: "Set up"
topic: "high-availability"
description: |
  Applies to:
  
  SQL Server
  
  This topic describes the prerequisites and recommendations for setting up database mirroring.
  
  For an introduction to database mirroring, see
  
  Database Mirroring (SQL Server)
  
tags:
  - "high-availability"
  - "set-up"
pubDate: 2025-12-01
---

Applies to:

SQL Server

This topic describes the prerequisites and recommendations for setting up database mirroring.

For an introduction to database mirroring, see

Database Mirroring (SQL Server)

.

For each database mirroring session:

1. The principal server, mirror server, and witness, if any, must be hosted by separate server

instances, which should be on separate host systems. Each of the server instances

requires a database mirroring endpoint. If you need to create a database mirroring

endpoint, ensure that it is accessible to the other server instances.

The form of authentication used for database mirroring by a server instance is a property

of its database mirroring endpoint. Two types of transport security are available for

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