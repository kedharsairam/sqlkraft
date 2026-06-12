---
title: "Upgrade SQL Server on Linux"
topic: "linux-operations"
description: |
  To minimize downtime and risk, you should consider several approaches when planning to

  upgrade the SQL Server Database Engine from an earlier release of SQL Server on Linux.

  Upgrade in place

  Minute
tags:
  - "linux-operations"
  - "upgrade-sql-server-on-linux"
pubDate: 2025-12-01
---

To minimize downtime and risk, you should consider several approaches when planning to

upgrade the SQL Server Database Engine from an earlier release of SQL Server on Linux.

Upgrade in place

Minutes or hours

No

Migrate to a new instance

Seconds or minutes (cutover only)

Yes

The amount of downtime depends on the size of your database and the speed of your I/O

subsystem. Upgrading a database with memory-optimized tables can take extra time. For more

information, see

Plan and test the Database Engine upgrade plan on Windows.

Make sure that your high availability and disaster recovery (HADR) strategy includes a fallback

scenario. The complexity of your environment and your organization's service-level agreement

(SLA) dictates which process to follow, and the associated risks.

For a list of features supported by the editions of SQL Server on Linux, see:

Editions and supported features of SQL Server 2025

Editions and supported features of SQL Server 2022

Editions and supported features of SQL Server 2019

Editions and supported features of SQL Server 2017

ﾉ

Expand table

７

Note

The downtime estimate for migration refers to the cutover window when you redirect users

to the new instance. The total elapsed time for building and preparing the new environment

is longer.
