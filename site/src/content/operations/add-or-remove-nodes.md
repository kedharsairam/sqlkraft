---
title: "Add or remove nodes"
topic: "high-availability"
description: "Use this procedure to manage nodes to an existing SQL Server failover cluster instance."
tags: ["high-availability","add-or-remove-nodes"]
pubDate: 2025-12-01
---

Use this procedure to manage nodes to an existing SQL Server failover cluster instance.

To update or remove a SQL Server FCI, you must be a local administrator with permission to

log in as a service on all nodes of the underlying Windows Server failover cluster (WSFC). For

local installations, you must run Setup as an administrator. If you install SQL Server from a

remote share, you must use a domain account that has read and execute permissions on the

remote share.

To add a node to an existing SQL Server FCI, you must run SQL Server Setup on the node that

is to be added to the SQL Server failover cluster instance. Do not run Setup on the active node.

To remove a node from an existing SQL Server FCI, you must run SQL Server Setup on the node

that is to be removed from the SQL Server failover cluster instance.

To view procedural steps to add or remove nodes, select one of the following operations:

Add a node to an existing Always On failover cluster instance

Remove a node from an existing Always On failover cluster instance

1. Insert the SQL Server installation media, and from the root folder, double-click Setup.exe.

To install from a network share, navigate to the root folder on the share, and then

double-click Setup.exe.

2. The Installation Wizard will launch the SQL Server Installation Center. To add a node to an

existing failover cluster instance, click

in the left-hand pane. Then, select

）

Important

The operating system drive letter for SQL Server install locations must match on all the

nodes added to the SQL Server failover cluster instance.
