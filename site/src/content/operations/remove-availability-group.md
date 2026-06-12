---
title: "Remove availability group"
topic: "high-availability"
description: |
  Article

  •

  09/04/2024

  Applies to:

  SQL Server

  This article describes how to delete (drop) an Always On availability group by using SQL Server

  Management Studio, Transact-SQL, or PowerShell in SQL
tags:
  - "high-availability"
  - "remove-availability-group"
pubDate: 2025-12-01
---

Article

•

09/04/2024

SQL Server

This article describes how to delete (drop) an Always On availability group by using SQL Server

Management Studio, Transact-SQL, or PowerShell in SQL Server. If a server instance that hosts

one of the availability replicas is offline when you delete an availability group, after coming

online, the server instance will drop the local availability replica. Dropping an availability group

deletes any associated availability group listener.

Note that, if necessary, you can drop an availability group from any Windows Server Failover

Clustering (WSFC) node that possesses the correct security credentials for the availability

group. This enables you to delete an availability group when none of its availability replicas

remain.

When the availability group is online, deleting it from a secondary replica causes the

primary replica to transition to the RESTORING state. Therefore, if possible, remove the

availability group only from the server instance that hosts the primary replica.

If you delete an availability group from a computer that has been removed or evicted

from the WSFC failover cluster, the availability group is only deleted locally.

Avoid dropping an availability group when the Windows Server Failover Clustering

(WSFC) cluster has no quorum. If you must drop an availability group while the cluster

lacks quorum, the metadata availability group that is stored in the cluster is not removed.

After the cluster regains quorum, you will need to drop the availability group again to

remove it from the WSFC cluster.

On a secondary replica, DROP AVAILABILITY GROUP should only be used only for

emergency purposes. This is because dropping an availability group takes the availability

group offline. If you drop the availability group from a secondary replica, the primary

replica cannot determine whether the OFFLINE state occurred because of quorum loss, a

）

Important

If possible, remove the availability group only while connected to the server instance that

hosts the primary replica. When the availability group is dropped from the primary replica,

changes are allowed in the former primary databases (without high availability protection).

Deleting an availability group from a secondary replica leaves the primary replica in the

RESTORING state, and changes are not allowed on the databases.
