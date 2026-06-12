---
title: "Take availability group offline"
topic: "high-availability"
description: "This topic describes how to take an Always On availability group from the ONLINE state to the OFFLINE state by using Transact-SQL in SQL Server 2012 S"
tags: ["high-availability","take-availability-group-offline"]
pubDate: "2025-12-01"
---

This topic describes how to take an Always On availability group from the ONLINE state to the

OFFLINE state by using Transact-SQL in SQL Server 2012 SP1 (11.0.3x) and later versions. There

is no data loss for synchronous-commit databases because if any synchronous-commit replica

is not synchronized, the OFFLINE operation raises an error and leaves the availability group

ONLINE. Keeping the availability group online protects unsynchronized synchronous-commit

databases from possible data loss. After an availability group goes offline, its databases

become unavailable to clients and you cannot bring the availability group back online.

Therefore, take an availability group offline only to migrate the availability group resources

from one WSFC cluster to another.

During a cross-cluster migration of Always On availability groups, if any applications connect

directly to the primary replica of an availability group, the availability group must be taken

offline. Cross-cluster migration of Always On availability groups supports OS upgrade with

minimal downtime of availability groups. The typical scenario is to use cross-cluster migration

of Always On availability groups with SQL Server 2012 SP1 (11.0.3x) and later versions. For

more information, see

Cross-Cluster Migration of Always On Availability Groups for OS

Upgrade.

The server instance on which you enter the OFFLINE command must be running SQL

Server 2012 SP1 (11.0.3x) or above (Enterprise edition or above).

The availability group must currently be online.

Before you take the availability group offline, delete the availability group listener or listeners.

For more information, see

Remove an Availability Group Listener (SQL Server).

Ｕ

Caution

Use the OFFLINE option for a cross-cluster migration of availability group resources or for

failing over a read-scale availability group.
