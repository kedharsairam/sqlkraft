---
title: "WSFC cluster service is offline"
topic: "high-availability"
description: "- Windows only : WSFC Cluster State : WSFC cluster service is offline. : : Instance of SQL Server This policy checks the state of the Windows Serv"
tags: ["high-availability","wsfc-cluster-service-is-offline"]
pubDate: 2025-12-01
---

- Windows only

: WSFC Cluster State

: WSFC cluster service is offline.

:

: Instance of SQL Server

This policy checks the state of the Windows Server Failover Cluster (WSFC). The policy is in an

unhealthy state and an alert is raised when the WSFC cluster is offline or in the forced quorum

state. All availability groups hosted within this cluster are offline or a disaster recovery action is

required.

The policy state is healthy when the cluster state is in the normal quorum.

This issue can be caused by a cluster service issue or by the loss of the quorum in the cluster.

Use the Cluster Administrator tool to perform the forced quorum or disaster recovery

workflow. If you cannot resolve the issue by performing the forced quorum or disaster

recovery, contact your cluster administrator to help resolve this issue. For more information,

see

Force a WSFC Cluster to Start Without a Quorum

in SQL Server Books Online.

Overview of Always On Availability Groups (SQL Server)

Use the Always On Dashboard (SQL Server Management Studio)

Description
