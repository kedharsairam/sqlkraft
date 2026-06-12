---
title: "Configure read-scale availability group"
topic: "high-availability"
description: "You can configure a SQL Server Always On availability group for read-scale workloads on Windows. There are two types of architecture for availability"
tags: ["high-availability","configure-read-scale-availability-group"]
pubDate: 2025-12-01
---

You can configure a SQL Server Always On availability group for read-scale workloads on

Windows. There are two types of architecture for availability groups:

An architecture for high availability that uses a cluster manager to provide improved

business continuity and that can include readable-secondary replicas. To create this high-

availability architecture, see

Create and configure availability groups on Windows.

An architecture that supports only read-scale workloads.

This article explains how to create an availability group without a cluster manager for read-

scale workloads. This architecture provides read-scale only. It doesn't provide high availability.

Before you create the availability group, you need to:

Set your environment so that all the servers that will host availability replicas can

communicate.

Install SQL Server. See

Install SQL Server

for details.

７

Note

An availability group with

can include replicas that are hosted on a

variety of operating system platforms. It cannot support high availability. For the Linux

operating system, see.

７

Note

The following command utilizes cmdlets from the sqlserver module that's published in the

PowerShell Gallery. You can install this module by using the Install-Module command.

```cmd
CLUSTER_TYPE = NONE
```
