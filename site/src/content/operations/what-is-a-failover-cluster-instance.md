---
title: "What is a failover cluster instance?"
topic: "high-availability"
description: |
  08/26/2025

  Applies to:

  SQL Server

  SQL Server Always On failover cluster instances use Windows Server Failover Clustering (WSFC)

  to provide local high availability. A failover cluster instance (FCI
tags:
  - "high-availability"
  - "what-is-a-failover-cluster-instance"
pubDate: 2025-12-01
---

08/26/2025

SQL Server

Always On failover cluster instances use Windows Server Failover Clustering (WSFC)

to provide local high availability. A failover cluster instance (FCI) is redundant at the server-

instance level. An FCI is a single instance of SQL Server that's installed across Windows Server

cluster nodes and, possibly, across multiple subnets. On the network, an FCI appears as an

instance of SQL Server running on a single computer, but the FCI provides failover from one

WSFC node to another if the current node becomes unavailable.

An FCI can use

Always On availability groups

to provide remote disaster recovery at the

database level. For more information, see

Failover clustering and Always On availability groups

(SQL Server).

failover cluster instances support Storage Spaces Direct for cluster storage

resources, which was introduced in Windows Server 2016 Datacenter edition. For more

information, see

Storage Spaces Direct in Windows Server.

Failover cluster instances also support Cluster Shared Volumes (CSV). For more information, see

Understanding Cluster Shared Volumes in a failover cluster.

When there's server hardware or software failure, the applications or clients connecting to the

server experience downtime. Redundant nodes protect the availability of the SQL Server

instance when it's an FCI instead of a standalone instance. Only one of the nodes in the FCI

owns the WSFC resource group at a time. If a failure occurs (such as hardware failure, operating

system failure, application or service failure), or during a planned upgrade, the cluster moves

the resource group ownership to another WSFC node. This process is transparent to the client

or application connecting to SQL Server. The process minimizes the downtime the application

or clients experience during a failure. Here are some key benefits that SQL Server failover

cluster instances provide:

７

Note

2025 (17.x) Preview introduces support to

to your

failover cluster instance.
