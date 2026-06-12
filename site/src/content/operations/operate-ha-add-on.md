---
title: "Operate (HA add-on)"
topic: "linux-operations"
description: "on Linux This document describes how to do the following tasks for SQL Server on a shared disk failover cluster with Red Hat Enterprise Linux. Manually fail over the cluste"
tags: ["linux-operations","operate-ha-add-on"]
pubDate: 2025-12-01
---

on Linux

This document describes how to do the following tasks for SQL Server on a shared disk failover

cluster with Red Hat Enterprise Linux.

Manually fail over the cluster

Monitor a failover cluster SQL Server service

Add a cluster node

Remove a cluster node

Change the SQL Server resource monitoring frequency

The clustering layer is based on Red Hat Enterprise Linux (RHEL)

HA add-on

built on top of

Pacemaker. Corosync and Pacemaker coordinate cluster communications and resource

management. The SQL Server instance is active on either one node or the other.

The following diagram illustrates the components in a Linux cluster with SQL Server.

For more information on cluster configuration, resource agents options, and management, visit

RHEL reference documentation.

The

command creates a constraint forcing the resource to start on the target

node. After executing the

command, executing resource

will remove the constraint

so it's possible to move the resource again, or have the resource automatically fail over.

```cmd
resource move move clear
```
