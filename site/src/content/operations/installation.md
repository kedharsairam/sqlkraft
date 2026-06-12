---
title: "Installation"
topic: "high-availability"
description: "08/26/2025 To install a SQL Server failover cluster, you must create and configure a failover cluster instance by running SQL Server Setup. To install a failover cluster, y"
tags: ["high-availability","installation"]
pubDate: "2025-12-01"
---

To install a SQL Server failover cluster, you must create and configure a failover cluster instance

by running SQL Server Setup.

To install a failover cluster, you must use a domain account that has local administrator rights

and permission to sign on as a service and act as part of the operating system on all nodes in

the failover cluster.

1. To install, configure, and maintain a SQL Server failover cluster, use SQL Server Setup.

Identify the information you need to create your failover cluster instance (for

example, cluster disk resource, IP addresses, and network name) and the nodes

available for failover. For more information, see:

Before installing failover clustering

Security considerations for a SQL Server installation

You must complete the configuration steps before you run the SQL Server Setup

program. Use the Windows Cluster Administrator to complete them. You must have

one Windows server failover cluster group for each failover cluster instance that you

want to configure.

You must ensure that your system meets minimum requirements. For more

information on specific requirements for a SQL Server failover cluster, see

Before

installing failover clustering.

2. Add or remove nodes from a failover cluster configuration without affecting the other

cluster nodes. For more information, see

Add or remove nodes in a SQL Server failover

cluster (Setup).

All nodes in a failover cluster must be of the same platform, either 32-bit or 64-bit,

and must run the same operating system edition and version. Also, 64-bit SQL

Server editions must be installed on 64-bit hardware running the 64-bit versions of

Windows operating systems. There's no WoW64 support for failover clustering in

this release.
