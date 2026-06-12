---
title: "Upgrade a cluster"
topic: "high-availability"
description: "ﾃ Summarize this article for me SQL Server supports upgrading a failover cluster to a new version of SQL Server, to a new SQL Server service pack or cumulative update, or w"
tags: ["high-availability","upgrade-a-cluster"]
pubDate: "2025-12-01"
---

ﾃ

Summarize this article for me

supports upgrading a failover cluster to a new version of SQL Server, to a new SQL

Server service pack or cumulative update, or when installing to a new Windows service pack or

cumulative update separately on all failover cluster nodes, with downtime limited to a single

manual failover (or two manual failovers if failing back to the original primary).

Upgrading the Windows Server operating system of a node containing a failover cluster

instance isn't supported for operating systems before Windows Server 2012 R2. To upgrade a

Windows Server failover cluster node running on Windows Server 2012 R2 or later versions, see

Perform a rolling upgrade or update.

Support details are as follows:

upgrade is supported both through the user interface and from the command

prompt. You can run upgrade from the command prompt on each failover cluster node,

or by using the SQL Server setup UI to upgrade each cluster node. For more information,

see:

Install a new SQL Server failover cluster instance

Install and configure SQL Server on Windows from the command prompt

The following scenarios aren't supported as part of a SQL Server upgrade:

You can't upgrade from a stand-alone instance of SQL Server to a failover cluster

instance.

You can't add features to a failover cluster instance. For example, you can't add the

Database Engine to an existing Analysis Services-only failover cluster instance.

You can't downgrade a failover cluster instance to a stand-alone instance on any node

of the Windows Server failover cluster.

Changing the edition of the failover cluster instance is limited to certain scenarios. For

more information, see

Supported version & edition upgrades (SQL Server 2016).

During the failover cluster instance upgrade, downtime is limited to failover time and the

time that is required for upgrade scripts to run. If you follow this failover cluster instance

rolling upgrade process, and meet all prerequisites on all nodes before you begin the

upgrade process, your downtime is minimal. Upgrading SQL Server when memory-
