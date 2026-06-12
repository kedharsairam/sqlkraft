---
title: "Operate an AG"
topic: "linux-operations"
description: |
  07/03/2025

  Applies to:

  SQL Server

  - Linux

  Before you upgrade an availability group, review the patterns and practices at

  Upgrade

  availability group replicas

  .

  The following sections explain ho
tags:
  - "linux-operations"
  - "operate-an-ag"
pubDate: 2025-12-01
---

07/03/2025

SQL Server

- Linux

Before you upgrade an availability group, review the patterns and practices at

Upgrade

availability group replicas.

The following sections explain how to perform a rolling upgrade with SQL Server instances on

Linux with availability groups.

When availability group replicas are on instances of SQL Server in Linux, the cluster type of the

availability group is either

or. An availability group that is managed by a cluster

manager besides Windows Server Failover Cluster (WSFC) is. Pacemaker with

Corosync is an example of an external cluster manager. An availability group with no cluster

manager has cluster type

The upgrade steps outlined here are specific for availability

groups of cluster type

or.

The order in which you upgrade instances depends on if their role is secondary and whether or

not they host synchronous or asynchronous replicas. Upgrade instances of SQL Server that host

asynchronous secondary replicas first. Then upgrade instances that host synchronous

secondary replicas.

Before you begin, back up each database.

1. Stop the resource on the node hosting the secondary replica targeted for upgrade.

Before running the upgrade command, stop the resource so the cluster will not monitor it

and fail it unnecessarily. The following example adds a location constraint on the node

７

Note

If an availability group only has asynchronous replicas, to avoid any data loss change one

replica to synchronous and wait until it's synchronized. Then upgrade this replica.

```cmd
EXTERNAL
NONE
EXTERNAL
NONE
EXTERNAL
```
