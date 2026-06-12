---
title: "Quorum Modes & Voting"
topic: "high-availability"
description: "Both SQL Server Always On availability groups and Always On Failover Cluster Instances (FCI) take advantage of Windows Server Failover Clustering (WSF"
tags: ["high-availability","quorum-modes-voting"]
pubDate: "2025-12-01"
---

Both SQL Server Always On availability groups and Always On Failover Cluster Instances (FCI)

take advantage of Windows Server Failover Clustering (WSFC) as a platform technology. WSFC

uses a quorum-based approach to monitoring overall cluster health and maximize node-level

fault tolerance. A fundamental understanding of WSFC quorum modes and node voting

configuration is very important to designing, operating, and troubleshooting your Always On

high availability and disaster recovery solution.

Each node in a WSFC cluster participates in periodic heartbeat communication to share the

node's health status with the other nodes. Unresponsive nodes are considered to be in a failed

state.

A

quorum

node set is a majority of the voting nodes and witnesses in the WSFC cluster. The

overall health and status of a WSFC cluster is determined by a periodic

quorum vote. The

presence of a quorum means that the cluster is healthy and able to provide node-level fault

tolerance.

The absence of a quorum indicates that the cluster is not healthy. Overall WSFC cluster health

must be maintained in order to ensure that healthy secondary nodes are available for primary

nodes to fail over to. If the quorum vote fails, the WSFC cluster will be set offline as a

precautionary measure. This will also cause all SQL Server instances registered with the cluster

to be stopped.

）

Important

If a WSFC cluster is set offline because of quorum failure, manual intervention is required

to bring it back online.

For more information, see:.
