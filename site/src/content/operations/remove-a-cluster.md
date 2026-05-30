---
title: "Remove a cluster"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Use this procedure to uninstall an Always On SQL Server failover cluster instance.

  Consider the following important points before you uninstall a SQL
tags:
  - "high-availability"
  - "remove-a-cluster"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

Use this procedure to uninstall an Always On SQL Server failover cluster instance.

Consider the following important points before you uninstall a SQL Server failover cluster

instance:

If SQL Server Native Client is uninstalled by accident, SQL Server resources will fail to start.

To reinstall SQL Server Native Client, run the SQL Server Setup program to install SQL

Server prerequisites.

If you uninstall a failover cluster that has more than one SQL IP cluster resource, you must

remove the additional SQL IP resources using Failover Cluster Manager or PowerShell.

For information about command prompt syntax, see

Install SQL Server 2016 from the

Command Prompt

.

1. To uninstall a SQL Server failover cluster, use the Remove Node functionality provided by

SQL Server Setup to remove each node individually. For more information, see

Add or

Remove Nodes in an Always On Failover Cluster (Setup)

.

View and Read SQL Server Setup Log Files

）

Important

To update or remove a SQL Server failover cluster, you must be a local administrator with

permission to login as a service on all nodes of the Windows Server failover cluster.
