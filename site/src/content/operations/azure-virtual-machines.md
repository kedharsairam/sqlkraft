---
title: "Azure virtual machines >"
topic: "high-availability"
description: |
  Applies to:
  
  SQL Server on Azure VM
  
  This article introduces Always On availability groups (AG) for SQL Server on Azure Virtual
  
  Machines (VMs).
  
  To get started, see the
  
  Availability group tutorial
  
  
tags:
  - "high-availability"
  - "azure-virtual-machines"
pubDate: 2025-12-01
---

Applies to:

SQL Server on Azure VM

This article introduces Always On availability groups (AG) for SQL Server on Azure Virtual

Machines (VMs).

To get started, see the

Availability group tutorial

.

Always On availability groups on Azure Virtual Machines are similar to

Always On availability

groups on-premises

and rely on the underlying

Windows Server Failover Cluster

. However,

since the virtual machines are hosted in Azure, there are a few additional considerations as

well, such as VM redundancy and routing traffic on the Azure network.

The following diagram illustrates an availability group for SQL Server on Azure VMs:

７

Note

It's now possible to lift and shift your availability group solution to SQL Server on Azure

VMs using Azure Migrate. See

to learn more.