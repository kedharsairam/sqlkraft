---
title: "Change the HADR cluster context"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/27/2023
  
  Applies to:
  
  SQL Server
  
  - Windows only
  
  This topic describes how to switch the HADR cluster context of an instance of SQL Server by
  
  using Transact-SQL in SQL Server 2012 SP1 
tags:
  - "high-availability"
  - "change-the-hadr-cluster-context"
pubDate: 2025-12-01
---

Article

•

09/27/2023

Applies to:

SQL Server

- Windows only

This topic describes how to switch the HADR cluster context of an instance of SQL Server by

using Transact-SQL in SQL Server 2012 SP1 (11.0.3x) and later versions. The

HADR cluster

context

determines which Windows Server Failover Clustering (WSFC) cluster manages the

metadata for availability replicas hosted by the server instance.

Switch the HADR cluster context only during a cross-cluster migration of Always On availability

groups to an instance of SQL Server 2012 SP1 (11.0.3x) on a new WSFC cluster. Cross-cluster

migration of Always On availability groups supports OS upgrade to Windows 8 or Windows

Server 2012 with minimal downtime of availability groups. For more information, see

Cross-

Cluster Migration of Always On Availability Groups for OS Upgrade

.

You can switch the HADR cluster context only from the local WSFC cluster to a remote

cluster and then back from the remote cluster to the local cluster. You cannot switch the

HADR cluster context from one remote cluster to another remote cluster.

The HADR cluster context can be switched to a remote cluster only when the instance of

SQL Server is not hosting any availability replicas.

A remote HADR cluster context can be switched back to the local cluster at any time.

However, the context cannot be switched again as long as the server instance is hosting

any availability replicas.

Ｕ

Caution

Switch the HADR cluster context only during cross-cluster migration of Always On

availability groups deployments.