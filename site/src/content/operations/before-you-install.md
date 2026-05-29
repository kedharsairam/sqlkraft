---
title: "Before you install"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/28/2023
  
  Applies to:
  
  SQL Server
  
  Before you install a SQL Server failover cluster, you must select the hardware and the operating
  
  system on which SQL Server will run. You must also co
tags:
  - "high-availability"
  - "before-you-install"
pubDate: 2025-12-01
---

Article

•

09/28/2023

Applies to:

SQL Server

Before you install a SQL Server failover cluster, you must select the hardware and the operating

system on which SQL Server will run. You must also configure Windows Server Failover

Clustering (WSFC) and review network, security, and considerations for other software that will

run on your failover cluster.

If a Windows cluster has a local disk drive and the same drive letter is used on one or more

cluster nodes as a shared drive, you can't install SQL Server on that drive. This restriction

applies to both SQL Server failover cluster instances and standalone instances on a server that

is part of a Windows Failover Cluster Instance.

You may also want to review the following articles to learn more about SQL Server failover

clustering concepts, features and tasks.

Describes SQL Server failover clustering concepts, and provides links

to associated content and tasks.

Always On Failover Cluster

Instances (SQL Server)

Describes SQL Server failover policy concepts, and provides links to

configuring the failover policy to suit your organizational

requirements.

Failover Policy for Failover Cluster

Instances

Describes how to maintain and your existing SQL Server failover

cluster.

Failover Cluster Instance

Administration and Maintenance

Explains how to install Analysis Services on a Windows Server Failover

Cluster (WSFC).

How to Cluster SQL Server

Analysis Services

Review the release notes for

SQL Server 2019

and

SQL Server 2022

.

Install prerequisite software. Before running Setup to install or upgrade, install the following

prerequisites to reduce installation time. You can install prerequisite software on each failover

cluster node and then restart nodes once before running Setup.

Windows PowerShell is no longer installed by SQL Server Setup. Windows PowerShell is a

prerequisite for installing SQL Server Database Engine components and SQL Server

ﾉ

Expand table