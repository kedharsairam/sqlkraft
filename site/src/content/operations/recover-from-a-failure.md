---
title: "Recover from a failure"
topic: "high-availability"
description: "This topic describes how to recover from cluster failures by using the Failover Cluster Manager snap-in after a failover occurs in SQL Server. The Fai"
tags: ["high-availability","recover-from-a-failure"]
pubDate: "2025-12-01"
---

This topic describes how to recover from cluster failures by using the Failover Cluster Manager

snap-in after a failover occurs in SQL Server. The Failover Cluster Manager snap-in is the cluster

management application for the Windows Serer Failover Clustering (WSFC) service.

Recover from an irreparable failure

Recover from a software failure

Use the following steps to recover from an irreparable failure. The failure could be caused, for

example, by the failure of a disk controller or the operating system. In this case, failure is

caused by hardware failure in Node 1 of a two-node cluster.

1. After Node 1 fails, the SQL Server FCI fails over to Node 2.

2. Evict Node 1 from the FCI. To do this, from Node 2, open the Failover Cluster Manager

snap-in, right-click Node1, click

, and then click.

3. Verify that Node 1 has been evicted from the cluster definition.

4. Install new hardware to replace the failed hardware in Node 1.

5. Using the Failover Cluster Manager snap-in, add Node 1 to the existing cluster. For more

information, see

Before Installing Failover Clustering.

6. Ensure that the administrator accounts are the same on all cluster nodes.

7. Run SQL Server Setup to add Node 1 to the FCI. For more information, see

Add or

Remove Nodes in a SQL Server Failover Cluster (Setup).

Us the following steps to recover from a reparable failure. In this case, failure is caused by

Node 1 being down or offline but not irretrievably broken. This could be caused by an

operating system failure, hardware failure, or failure in the SQL Server instance itself.
