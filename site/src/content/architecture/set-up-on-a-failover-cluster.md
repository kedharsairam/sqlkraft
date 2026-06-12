---
title: "Set Up on a Failover Cluster"
topic: "filestream"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  This topic describes how to enable FILESTREAM on a failover cluster. Before you try this

  procedure, you should understand

  failover clustering

  and ha
tags:
  - "filestream"
  - "set-up-on-a-failover-cluster"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

This topic describes how to enable FILESTREAM on a failover cluster. Before you try this

procedure, you should understand

failover clustering

and have FILESTREAM enabled. For

information about how to enable FILESTREAM, see

Enable and Configure FILESTREAM.

1. Set up the primary node for the failover cluster.

After the setup finishes, enable FILESTREAM on the primary node by using

SQL Server. This enables the settings that require Windows Admin privileges.

If remote access is required, select. This will create a file-share cluster resource.

2. Set up a passive node.

After the setup finishes, enable FILESTREAM on the passive node by using

SQL Server. The name that you specify for

must be

the same across all nodes in the cluster.

3. To add more passive nodes, repeat step 2.

4. After all the nodes are added, complete the process by executing the sp_configure stored

procedure on each instance of SQL Server.

5. To add and enable additional nodes to the cluster at any time, you can repeat steps 2, 3,

and 4.

Server Configuration Options (SQL Server)

Create a New SQL Server Failover Cluster (Setup)

Remove a SQL Server Failover Cluster Instance (Setup)

Add or Remove Nodes in a SQL Server Failover Cluster (Setup)
