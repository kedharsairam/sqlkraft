---
title: "Force a cluster to start without a Quorum"
topic: "high-availability"
description: "This topic describes how to force a Windows Server Failover Clustering (WSFC) cluster node to start without a quorum. This may be required in disaster"
tags: ["high-availability","force-a-cluster-to-start-without-a-quorum"]
pubDate: "2025-12-01"
---

This topic describes how to force a Windows Server Failover Clustering (WSFC) cluster node to

start without a quorum. This may be required in disaster recovery and multi-subnet scenarios

to recover data and fully re-establish high-availability for Always On availability groups and

Failover Cluster Instances.

Recommendations

,

Security

Using Failover Cluster Manager

,

Using Powershell

,

Using Net.exe

Follow Up: After Forcing Cluster to Start without a Quorum

Except where explicitly directed, the procedures in this topic should work if you execute them

from any node in the WSFC cluster. However, you may obtain better results, and avoid

networking issues, by executing these steps from the node that you intend to force to start

without a quorum.

The user must be a domain account that is member of the local Administrators group on each

node of the WSFC cluster.

1. Open a Failover Cluster Manager and connect to the desired cluster node to force online.

2. In the

pane, click

, and then click.

To force a cluster to start without a quorum
