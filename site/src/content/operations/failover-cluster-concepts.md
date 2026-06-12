---
title: "Failover cluster concepts"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This article explains the concepts related to SQL Server failover cluster instances (FCI) on Linux.

  To create a SQL Server FCI on Linux, see

  Configure failover clu
tags:
  - "linux-operations"
  - "failover-cluster-concepts"
pubDate: 2025-12-01
---

SQL Server

on Linux

This article explains the concepts related to SQL Server failover cluster instances (FCI) on Linux.

To create a SQL Server FCI on Linux, see

Configure failover cluster instance - SQL Server on Linux

(RHEL)

In Red Hat Enterprise Linux (RHEL), the clustering layer is based on Red Hat Enterprise Linux

(RHEL)

HA add-on.

In SUSE Linux Enterprise Server (SLES), the clustering layer is based on SUSE Linux Enterprise

High Availability Extension (HAE).

For more information on cluster configuration, resource agent options, management, best

practices, and recommendations, see

SUSE Linux Enterprise High Availability Extension 15.

Both the RHEL HA add-on and the SUSE HAE are built on

Pacemaker.

As the following diagram shows, storage is presented to two servers. Clustering components -

Corosync and Pacemaker - coordinate communications and resource management. One of the

servers has the active connection to the storage resources and the SQL Server. When Pacemaker

detects a failure, the clustering components are responsible for moving the resources to the

other node.

７

Note

Access to Red Hat HA add-on and documentation requires a subscription.
