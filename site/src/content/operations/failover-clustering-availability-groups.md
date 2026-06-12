---
title: "Failover clustering & availability groups"
topic: "high-availability"
description: "08/26/2025 - Windows only Always On availability groups, the high availability and disaster recovery solution introduced in SQL Server 2012 (11.x), requires Windows Server"
tags: ["high-availability","failover-clustering-availability-groups"]
pubDate: 2025-12-01
---

- Windows only

Always On availability groups, the high availability and disaster recovery solution introduced in

2012 (11.x), requires Windows Server Failover Clustering (WSFC). Also, though

Always On availability groups isn't dependent upon SQL Server failover clustering, you can use

a failover clustering instance (FCI) to host an availability replica for an availability group. It's

important to know the role of each clustering technology, and to know what considerations are

necessary as you design your Always On availability groups environment.

Deploying Always On availability groups requires a Windows Server Failover Cluster (WSFC). To

be enabled for Always On availability groups, an instance of SQL Server must reside on a WSFC

node, and the WSFC and node must be online. Furthermore, each availability replica of a given

availability group must reside on a different node of the same WSFC. The only exception is that

while being migrated to another WSFC, an availability group can temporarily straddle two

clusters.

Always On availability groups relies on the Windows Server Failover Cluster (WSFC) to monitor

and manage the current roles of the availability replicas that belong to a given availability

group and to determine how a failover event affects the availability replicas. A WSFC resource

group is created for every availability group that you create. The WSFC monitors this resource

group to evaluate the health of the primary replica.

The quorum for Always On availability groups is based on all nodes in the WSFC regardless of

whether a given cluster node hosts any availability replicas. In contrast to database mirroring,

there's no witness role in Always On availability groups.

７

Note

For information about Always On availability groups concepts, see
