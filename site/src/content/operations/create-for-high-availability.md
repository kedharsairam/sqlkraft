---
title: "Create for high availability"
topic: "linux-operations"
description: "10/20/2025 - Linux This article presents supported deployment configurations for SQL Server Always On availability groups on Linux servers. An availability group supports h"
tags: ["linux-operations","create-for-high-availability"]
pubDate: "2025-12-01"
---

- Linux

This article presents supported deployment configurations for SQL Server Always On

availability groups on Linux servers. An availability group supports high availability and data

protection. Automatic failure detection, automatic failover, and transparent reconnection after

failover provide high availability. Synchronized replicas provide data protection.

On a Windows Server Failover Cluster (WSFC), a common configuration for high availability

uses two synchronous replicas and a third server or file share to provide quorum. The file-share

witness validates the availability group configuration - status of synchronization, and the role

of the replica, for example. This configuration ensures that the secondary replica chosen as the

failover target has the latest data and availability group configuration changes.

The WSFC synchronizes configuration metadata for failover arbitration between the availability

group replicas and the file-share witness. When an availability group isn't on a WSFC, the SQL

Server instances store configuration metadata in the

database.

For example, an availability group on a Linux cluster has. There's no

WSFC to arbitrate failover. In this case, the configuration metadata is managed and maintained

by the SQL Server instances. Because there's no witness server in this cluster, a third SQL Server

instance is required to store configuration state metadata. All three SQL Server instances

together provide distributed metadata storage for the cluster.

The cluster manager can query the instances of SQL Server in the availability group, and

orchestrate failover to maintain high availability. In a Linux cluster, Pacemaker is the cluster

manager.

Starting with SQL Server 2017 (14.x) CU 1, high availability for an availability group with

is enabled for two synchronous replicas plus a configuration only

replica. The configuration only replica can be hosted on any edition of SQL Server 2017 (14.x)

CU 1 or later versions (including SQL Server Express edition). The configuration only replica

maintains configuration information about the availability group in the

database but

doesn't contain the user databases in the availability group.

```cmd
master
CLUSTER_TYPE = EXTERNAL
CLUSTER_TYPE = EXTERNAL master
```
