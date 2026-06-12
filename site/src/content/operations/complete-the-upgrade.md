---
title: "Complete the upgrade"
topic: "upgrade"
description: |
  06/04/2025

  Applies to:

  SQL Server

  - Windows only

  After upgrading the Database Engine, complete the following tasks:

  Perform a full backup of each database.

  In SQL Server 2016 (13.x) and later ve
tags:
  - "upgrade"
  - "complete-the-upgrade"
pubDate: 2025-12-01
---

06/04/2025

SQL Server

- Windows only

After upgrading the Database Engine, complete the following tasks:

Perform a full backup of each database.

In SQL Server 2016 (13.x) and later versions, some changes are only enabled once the

level for a database is changed to 130 or greater. For more

information and for the recommended workflow, see

Change the database compatibility

level and use the Query Store. If your database has memory-optimized tables created in

2014 (12.x), review

Statistics for Memory-Optimized Tables.

Migrate Integration Services packages to the latest format. For more information, see

Upgrade Integration Services Packages.

For a new installation upgrade, restore the Reporting Services encryption Keys. For more

information, see

Back up and restore SQL Server Reporting Services (SSRS) encryption

keys.

Upgrade the Master Data Services (MDS) database schema and create the SQL Server

2019 (15.x) web application. For more information, see

Upgrade Master Data Services.

Upgrade the Data Quality Services (DQS) databases schema and verify the DQS databases

schema upgrade. For more information, see

Upgrade Data Quality Services.

７

Note

MDS is discontinued in SQL Server 2025 (17.x) Preview.

```cmd
DATABASE_COMPATIBILITY
```
