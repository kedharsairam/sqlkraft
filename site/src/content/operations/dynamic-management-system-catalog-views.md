---
title: "Dynamic management & system catalog views"
topic: "high-availability"
description: |
  Dynamic management views and system

  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  This topic shows you some of the common queries on the Always On dynamic management

  views (DMV) that you can use
tags:
  - "high-availability"
  - "dynamic-management-system-catalog-views"
pubDate: 2025-12-01
---

Dynamic management views and system

Article

•

03/03/2023

Applies to:

SQL Server

This topic shows you some of the common queries on the Always On dynamic management

views (DMV) that you can use to monitor and troubleshoot availability groups.

For more information on the availability group DMVs, see

Always On Availability Groups

dynamic management views and functions (Transact-SQL)

. For more information on the

availability groups catalog views, see

Always On Availability Groups catalog views (Transact-

SQL)

.

The following Transact-SQL (T-SQL) query retrieves the status of all the nodes in the current

Windows Server Failover Clustering (WSFC) cluster.

SQL

This result set reports the status of each member node of the current WSFC cluster. If the

quorum is defined as

, even the file share is reported. You can

see the status of each node, including the voting weight of each node (the

number_of_quorum_votes

value).



Tip

In the Always On Dashboard, you can easily configure the GUI to display many of the

DMVs for the availability replicas and availability databases by right-clicking the respective

table header and selecting the DMV you wish to display or hide.

```cmd
use
master
go
select
*
from
sys.dm_hadr_cluster_members
go
```
