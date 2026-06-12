---
title: "Configure with HPE Serviceguard"
topic: "linux-operations"
description: "on Linux This tutorial explains how to configure SQL Server availability groups with HPE Serviceguard for Linux, running on on-premises virtual machines (VMs) or in Azure-ba"
tags: ["linux-operations","configure-with-hpe-serviceguard"]
pubDate: 2025-12-01
---

on Linux

This tutorial explains how to configure SQL Server availability groups with HPE Serviceguard for

Linux, running on on-premises virtual machines (VMs) or in Azure-based Virtual Machines.

For an overview of the HPE Serviceguard clusters, see

HPE Serviceguard Clusters.

This tutorial consists of the following tasks:

In Azure, create three Linux-based VMs (Virtual Machines). To create Linux-based virtual

machines in Azure, see

Quickstart: Create Linux virtual machine in Azure portal. When

deploying the VMs, make sure to use HPE Serviceguard supported Linux distributions.

You can also deploy the VMs locally in an on-premises environment if you prefer.

For an example of a supported distribution, see

HPE Serviceguard for Linux. Check with

HPE for information about support for public cloud environments.

The instructions in this tutorial are validated against HPE Serviceguard for Linux. A trial

edition is available for download from

HPE.

７

Note

Microsoft supports data movement, the availability group, and the SQL Server

components. Contact HPE for support related to the documentation of HPE Serviceguard

cluster and quorum management.

Install SQL Server on all three VMs that you plan to include in the availability group.

＂

Install HPE Serviceguard on the VMs.

＂

Create the HPE Serviceguard cluster.

＂

Create the load balancer in the Azure portal.

＂

Create the availability group and add a sample database to the availability group.

＂

Deploy the SQL Server workload on the availability group through Serviceguard cluster

manager.

＂

Perform an automatic failover and join the node back to cluster.

＂
