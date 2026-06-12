---
title: "Failover cluster instances"
topic: "high-availability"
description: ""
tags: ["high-availability","failover-cluster-instances"]
pubDate: 2025-12-01
---

A failover cluster is a combination of one or more physical disks in a Microsoft Cluster Service

(MSCS) cluster group, known as a resource group, that are participating nodes of the cluster.

The resource group is configured as a failover clustered instance that hosts an instance of SQL

Server. A SQL Server failover clustered instance appears on the network as if it were a single

computer, but has functionality that provides failover from one node to another if one node

becomes unavailable. For more information, see

Always On Failover Cluster Instances (SQL

Server).

Failover clusters provide high-availability support for an entire Microsoft SQL Server instance,

in contrast to database mirroring, which provides high-availability support for a single

database. Database mirroring works between failover clusters and, also, between a failover

cluster and a nonclustered host.

Typically, when mirroring is used with clustering, the principal server and mirror server both

reside on clusters, with the principal server running on the failover clustered instance of one

cluster and the mirror server running on the failover clustered instance of a different cluster.

You can establish a mirroring session in which one partner resides on the failover clustered

instance of a cluster and the other partner resides on a separate, unclustered computer,

however.

If a cluster failover makes a principal server temporarily unavailable, client connections are

disconnected from the database. After the cluster failover completes, clients can reconnect to

the principal server on the same cluster, or on a different cluster or an unclustered computer,

depending on the

operating mode. Therefore, when deciding how to configure database

mirroring in a clustered environment, the operating mode you use for mirroring is significant.

７

Note

For an introduction to database mirroring, see.
