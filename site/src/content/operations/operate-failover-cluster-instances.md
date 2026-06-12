---
title: "Operate failover cluster instances"
topic: "linux-operations"
description: "on Linux This article explains how to operate a SQL Server failover cluster instance (FCI) on Linux. If you haven't created a SQL Server FCI on Linux, see Configure failove"
tags: ["linux-operations","operate-failover-cluster-instances"]
pubDate: "2025-12-01"
---

on Linux

This article explains how to operate a SQL Server failover cluster instance (FCI) on Linux. If you

haven't created a SQL Server FCI on Linux, see

Configure failover cluster instance - SQL Server

on Linux (RHEL).

Failover for FCIs is similar to a Windows Server failover cluster (WSFC). If the cluster node

hosting the FCI experiences some sort of failure, the FCI should automatically fail over to

another node. Unlike a WSFC, there's no way to set preferred owners, so Pacemaker picks the

node that will be the new host for the FCI.

There are times you might want to manually fail the FCI to another node. The process isn't the

same as with FCIs on a WSFC. On a WSFC, you fail over resources at the role level. In

Pacemaker, you choose a resource to move, and assuming all the constraints are correct,

everything else will move as well.

The way to failover depends on the Linux distribution. Follow the instructions for your linux

distribution.

RHEL or Ubuntu

SLES

To perform a manual failover on Red Hat Enterprise Linux (RHEL) or Ubuntu servers, execute

the following steps.

1. Issue the following command:

Bash

<FCIResourceName> is the Pacemaker resource name for the SQL Server FCI.

<NewHostNode> is the name of the cluster node that you want to host the FCI.

```cmd
sudo pcs resource move <FCIResourceName> <NewHostNode>
```
