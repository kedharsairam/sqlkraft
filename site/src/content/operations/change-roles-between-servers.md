---
title: "Change roles between servers"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  After you have failed over a SQL Server log shipping configuration to a secondary server, you

  can configure your secondary database to act as the prim
tags:
  - "high-availability"
  - "change-roles-between-servers"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

After you have failed over a SQL Server log shipping configuration to a secondary server, you

can configure your secondary database to act as the primary database. Then, you will be able

to swap primary and secondary databases as needed.

The first time you want to fail over to the secondary database and make it your new primary

database, there is a series of steps you must take. After you have followed these initial steps,

you will be able to swap roles between the primary database and the secondary database

easily.

1. Manually fail over from the primary database to a secondary database. Be sure to back up

the active transaction log on your primary server with NORECOVERY. For more

information, see

Fail Over to a Log Shipping Secondary (SQL Server)

.

2. Disable the log shipping backup job on the original primary server, and the copy and

restore jobs on the original secondary server.

3. On your secondary database (the database you want to be the new primary), configure

log shipping using SQL Server Management Studio. For more information, see

Configure

Log Shipping (SQL Server)

. Include the following steps:

a. Use the same share for creating backups that you created for the original primary

server.

b. When adding the secondary database, in the

dialog box,

enter the name of the original primary database in the

box.

c. In the

dialog box, select

.

4. If log shipping monitoring was enabled on your former log shipping configuration,

reconfigure log shipping monitoring to monitor the new log shipping configuration.

Setting the threshold_alert_enabled to 1 specifies that an alert will be raised when
