---
title: "Enable & disable"
topic: "high-availability"
description: |
  ﾃ

  Summarize this article for me

  Applies to:

  SQL Server

  Before you can create and configure an Always On availability group, you must enable the

  Always On availability groups feature on each insta
tags:
  - "high-availability"
  - "enable-disable"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

SQL Server

Before you can create and configure an Always On availability group, you must enable the

Always On availability groups feature on each instance of SQL Server that hosts an availability

replica.

In SQL Server 2016 (13.x), the instance must reside on a Windows Server Failover Cluster

(WSFC) node to enable the availability group feature.

In SQL Server 2017 (14.x) and later versions, to support

read-scale availability groups

, you

can enable the availability group feature even if the SQL Server instance doesn't reside on

a Windows Server Failover Cluster.

The server instance must run an edition of SQL Server that supports Always On availability

groups. For more information, see

Editions and supported features of SQL Server 2025.

Enable availability groups on only one server instance at a time. After enabling availability

groups, wait until the SQL Server service restarts before you proceed to another server

instance.

For more information, see

Prerequisites, Restrictions, and Recommendations for Always

On Availability Groups (SQL Server).

When you enable availability groups on an instance of SQL Server, the server instance has full

control over the WSFC cluster.

）

Important

If you delete and re-create a WSFC cluster, you must disable and re-enable the Always On

availability groups feature on each instance of SQL Server that hosted an availability

replica on the original WSFC cluster.
