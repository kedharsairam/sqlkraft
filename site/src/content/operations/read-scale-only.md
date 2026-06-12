---
title: "Read-scale only"
topic: "high-availability"
description: |
  Article

  •

  10/20/2023

  Applies to:

  SQL Server

  An availability group is a comprehensive solution that brings high-availability capabilities to

  SQL Server and offers integrated scaling solutions as
tags:
  - "high-availability"
  - "read-scale-only"
pubDate: 2025-12-01
---

Article

•

10/20/2023

SQL Server

An availability group is a comprehensive solution that brings high-availability capabilities to

and offers integrated scaling solutions as well. In a typical database application,

multiple clients run various types of workloads. Sometimes bottlenecks can develop due to

resource constraints.

In the context of an availability group, read-scale is offloading read workloads to one or more

secondary replicas. You can free up resources and achieve higher throughput for the OLTP

workload. You also can deliver higher performance and scale on read-only workloads. Take

advantage of the fastest replication technology for SQL Server and create a group of replicated

databases to offload reporting and analytics workloads to read-only replicas.

With availability groups, one or more secondary replicas can be configured to support read-

only access to secondary databases.

The client applications that run analytics or reporting workloads can directly connect to

secondary databases. You also can set up a read-only routing list and connect to the primary

database. It then forwards the connection request to each of the secondary replicas from the

routing list in a round-robin fashion.

In SQL Server 2016 (13.x) and earlier versions, all availability groups required a cluster. The

cluster provided business continuity for high availability and disaster recovery (HADR). In

addition, secondary replicas were configured for read operations. If high availability wasn't the

goal, considerable operational overhead was expended to configure and operate a cluster. SQL

Server 2017 (14.x) introduces read-scale availability groups without a cluster.

７

Note

In availability groups that don't utilize Windows Server Failover Clustering (WSFC), such as

read-scale availability groups, or

, columns in the

related to the cluster might display data about an internal default cluster.

These columns are for internal use only and can be disregarded.
