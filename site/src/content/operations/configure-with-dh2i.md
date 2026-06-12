---
title: "Configure with DH2i"
topic: "linux-operations"
description: |
  Article

  •

  02/13/2023

  Applies to:

  SQL Server on Azure VM

  This tutorial explains how to configure a SQL Server Always On availability group with DH2i

  DxEnterprise running on Linux-based Azure Virt
tags:
  - "linux-operations"
  - "configure-with-dh2i"
pubDate: 2025-12-01
---

Article

•

02/13/2023

on Azure VM

This tutorial explains how to configure a SQL Server Always On availability group with DH2i

DxEnterprise running on Linux-based Azure Virtual Machines (VMs).

For more information about DxEnterprise, see

DH2i DxEnterprise.

In this tutorial, you'll set up a DxEnterprise cluster using

DxAdmin Client UI. Optionally, you

can also set up the cluster using the

DxCLI

command-line interface. For this example, we've

used four VMs. Three of those VMs are running Ubuntu 18.04, and are part of the three node

cluster. The fourth VM is running Windows 10 with the DxAdmin tool to manage and configure

the cluster.

This tutorial consists of the following steps:

Create four virtual machines in Azure. Follow the

Quickstart: Create Linux virtual machine

in Azure portal

article to create Linux based virtual machines. Similarly, for creating the

Windows based virtual machine, follow the

Quickstart: Create a Windows virtual machine

in the Azure portal

article.

Install.NET 3.1 on all the Linux-based VMs that are going to be part of the cluster. For

instructions for the Linux operating system that you choose, see

Install.NET on Linux

distributions.

７

Note

Microsoft supports data movement, availability groups, and the SQL Server components.

Contact DH2i for support related to the documentation of DH2i DxEnterprise cluster, for

the cluster and quorum management.

Install SQL Server on all virtual machines that will be part of the availability group.

＂

Install DxEnterprise on all the virtual machines and configure the DxEnterprise cluster.

＂

Create the virtual hosts to provide failover support and high availability and add an

availability group and database to the availability group.

＂

Create the internal Azure Load Balancer for availability group listener (optional).

＂

Perform a manual or automatic failover.

＂
