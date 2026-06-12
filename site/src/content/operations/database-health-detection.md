---
title: "Database health detection"
topic: "high-availability"
description: |
  Article

  •

  05/25/2023

  Applies to:

  SQL Server

  Starting in SQL Server 2016, database level health detection (DB_FAILOVER) option is available

  when configuring an Always On availability group. The d
tags:
  - "high-availability"
  - "database-health-detection"
pubDate: 2025-12-01
---

Article

•

05/25/2023

SQL Server

Starting in SQL Server 2016, database level health detection (DB_FAILOVER) option is available

when configuring an Always On availability group. The database level health detection notices

when a database is no longer in the online status, when something goes wrong, and will

trigger the automatic failover of the availability group. Examples that may trigger the health

detection include database in suspect mode, database is offline, database in recovery (failed to

recover). For more information see

State column in sys.databases.

The database level health detection is enabled for the availability group as a whole, therefore

database level health detection monitors every database in the availability group. It cannot be

enabled selectively for specific databases in the availability group.

The availability group database level health detection option is widely recommended as a good

option to help guarantee the high availability for your databases. You should consider turning

it on for all availability groups. If your application depends on several databases to be highly

available, group them into an availability group with the database health option turned on.

For example, with database level health detection option on, if SQL Server was unable to write

to the transaction log file for one of the databases, the status of that database would change

to indicate failure, and the availability group would soon fail over, and your application could

reconnect and continue working with minimal interruption once the databases are online

again.

Though it is generally recommended, the Database Health option is

, in effort to

keep backward compatibility with the default settings in prior versions.

There are several easy ways to enable database level health detection setting:

1. In SQL Server Management Studio, connect to your SQL Server database engine. Using

the Object Explorer window, right-click on the Always On High Availability node, and run

the. Check the

checkbox on the Specify Name page. Then complete the rest of the pages in the wizard.
