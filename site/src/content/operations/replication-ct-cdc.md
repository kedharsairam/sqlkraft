---
title: "Replication, CT, & CDC"
topic: "high-availability"
description: |
  Article

  •

  01/03/2025

  Applies to:

  SQL Server

  SQL Server Replication, change data capture (CDC), and change tracking (CT) are supported on

  Always On availability groups. Always On availability gro
tags:
  - "high-availability"
  - "replication-ct-cdc"
pubDate: 2025-12-01
---

Article

•

01/03/2025

Applies to:

SQL Server

SQL Server Replication, change data capture (CDC), and change tracking (CT) are supported on

Always On availability groups. Always On availability groups helps provide high availability and

other database recovery capabilities.

When a published database is aware of Always On availability groups, the distributor that

provides agent access to the publishing database is configured with redirected_publishers

entries. These entries redirect the originally configured publisher/database pair, making use of

an availability group listener name to connect to the publisher and publishing database.

Established connections through the availability group listener name fail on failover. When the

replication agent restarts after failover, the connection is automatically redirected to the new

primary.

In an availability group (AG), a secondary database can't be a publisher. Republishing is only

supported when transactional replication is combined with Always On availability groups.

If a published database is a member of an availability group and the publisher is redirected, it

must be redirected to an availability group listener name associated with the availability group.

It might not be redirected to an explicit node.

７

Note

After failover to a secondary replica, Replication Monitor is unable to adjust the name of

the publishing instance of SQL Server and continues to display replication information

under the name of the original primary instance of SQL Server. After failover, a tracer

token can't be entered by using the Replication Monitor, however a tracer token entered

on the new publisher by using Transact-SQL, is visible in Replication Monitor.
