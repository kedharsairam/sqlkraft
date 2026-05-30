---
title: "Upgrading replica instances"
topic: "high-availability"
description: |
  08/15/2025

  Applies to:

  SQL Server

  When upgrading a SQL Server instance that hosts an Always On availability group (AG) to a

  new SQL Server version, to a new SQL Server service pack or cumulative u
tags:
  - "high-availability"
  - "upgrading-replica-instances"
pubDate: 2025-12-01
---

08/15/2025

Applies to:

SQL Server

When upgrading a SQL Server instance that hosts an Always On availability group (AG) to a

new SQL Server version, to a new SQL Server service pack or cumulative update, or when

installing to a new Windows service pack or cumulative update, you can reduce downtime for

the primary replica to only a single manual failover by performing a rolling upgrade (or two

manual failovers if failing back to the original primary).

During the upgrade process, a secondary replica won't be available for failover or for read-only

operations, and after the upgrade, it might take some time for the secondary replica to catch

up with the primary replica node depending upon the volume of activity on the primary replica

node (so expect high network traffic).

Also be aware that after the initial failover to a secondary replica running a newer version of

SQL Server, the databases in that AG will run through an upgrade process to bring them to the

latest version. During this time, there will be no readable replicas for any of these databases.

Downtime after the initial failover will depend on the number of databases in the AG. If you

plan on failing back to the original primary, this step won't be repeated when you fail back.

Before you begin, review the following important information:

Supported version and edition upgrades

: Verify that you can upgrade to the latest version

of SQL Server from your version of the Windows operating system and version of SQL

Server. For example, if you upgrade directly from a SQL Server 2005 instance, your

database compatibility level is upgraded.

Choose a database engine upgrade method

: To upgrade in the correct order, select the

appropriate upgrade method and steps based on your review of supported version and

７

Note

This article limits the discussion to the upgrade of SQL Server itself. It doesn't cover

upgrading the operating system containing the Windows Server Failover Cluster (WSFC).

Upgrading the Windows operating system hosting the failover cluster isn't supported for

operating systems before Windows Server 2012 R2. To upgrade a cluster node running on

Windows Server 2012 R2, see

.
