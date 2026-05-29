---
title: "Fabric mirrored databases"
topic: "high-availability"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  You can mirror databases from SQL Server (2016-2025), Azure S
tags:
  - "high-availability"
  - "fabric-mirrored-databases"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

You can mirror databases from SQL Server (2016-2025), Azure SQL Database, and Azure SQL

Managed Instance to Microsoft Fabric. You can continuously replicate your existing data estate

directly into Fabric's OneLake.

For more information and tutorials, see:

Mirroring Azure SQL Database

Mirroring Azure SQL Managed Instance

Mirroring SQL Server

For more information, see:

Microsoft Fabric mirrored databases

Microsoft Fabric mirrored databases monitoring

Explore data in your mirrored database using Microsoft Fabric

Mirroring in Fabric provides an easy experience to speed the time-to-value for insights and

decisions, and to break down data silos between technology solutions, without developing

expensive Extract, Transform, and Load (ETL) processes to move data.

With the most up-to-date data in a queryable format in OneLake, you can now use all the

different services in Fabric, such as running analytics with Spark, executing notebooks, data

engineering, visualizing through Power BI Reports, and more.

With Mirroring in Fabric, you don't need to piece together different services from multiple

vendors. Instead, you can enjoy a highly integrated, end-to-end, and easy-to-use product that

is designed to simplify your analytics needs, and built for openness and collaboration between

technology solutions that can read the open-source Delta Lake table format.

The Fabric mirrored database feature uses similar change feed technology as the Azure

Synapse Link, and shares some system objects.

Enabling Mirroring via the Fabric portal will create a

database user, a

schema, and several tables within the

schema in your source database. Do not alter

```cmd
changefeed
changefeed
changefeed
```
