---
title: "Database mirroring"
topic: "high-availability"
description: |
  09/02/2025
  
  Applies to:
  
  SQL Server
  
  Database mirroring
  
  is a solution for increasing the availability of a SQL Server database.
  
  Mirroring is implemented on a per-database basis and works only with d
tags:
  - "high-availability"
  - "database-mirroring"
pubDate: 2025-12-01
---

09/02/2025

Applies to:

SQL Server

Database mirroring

is a solution for increasing the availability of a SQL Server database.

Mirroring is implemented on a per-database basis and works only with databases that use the

full recovery model.

Database mirroring is a simple strategy that offers the following benefits:

Increases availability of a database.

In the event of a disaster, in high-safety mode with automatic failover, failover quickly

brings the standby copy of the database online (without data loss). In the other operating

modes, the database administrator has the alternative of forcing service (with possible

data loss) to the standby copy of the database. For more information, see

Role Switching

,

later in this topic.

Increases data protection.

Database mirroring provides complete or almost complete redundancy of the data,

depending on whether the operating mode is high-safety or high-performance. For more

information, see

Operating Modes

, later in this topic.

７

Note

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Always On availability groups instead. Database Mirroring in SQL Server is a distinct

technology from

.

）

Important

For information about support for database mirroring, restrictions, prerequisites,

recommendations for configuring partner servers, and recommendations for deploying

database mirroring, see

Prerequisites, Restrictions, and Recommendations for Database

.