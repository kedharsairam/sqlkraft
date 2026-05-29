---
title: "Deploy a Pacemaker cluster"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This tutorial describes the tasks required to deploy a Linux Pacemaker cluster for a SQL Server

  Always On availability group (AG) or failover cluster instance (FCI)
tags:
  - "linux-operations"
  - "deploy-a-pacemaker-cluster"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This tutorial describes the tasks required to deploy a Linux Pacemaker cluster for a SQL Server

Always On availability group (AG) or failover cluster instance (FCI). Unlike the tightly coupled

Windows Server / SQL Server stack, you can create a Pacemaker cluster and configure an

availability group (AG) on Linux before or after installing SQL Server. You configure the

integration and resources for the Pacemaker portion of an AG or FCI deployment after the

cluster is configured.

Install SQL Server on Linux

.

Use the following syntax to install the packages that make up the high availability (HA) add-on

for each distribution of Linux.

）

Important

An AG with a cluster type of None doesn't require a Pacemaker cluster and can't be

managed by Pacemaker.

Install the high availability add-on and install Pacemaker.

＂

Prepare the nodes for Pacemaker (RHEL and Ubuntu only).

＂

Create the Pacemaker cluster.

＂

Install the SQL Server HA and SQL Server Agent packages.

＂

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.

Red Hat Enterprise Linux (RHEL)
