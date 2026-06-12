---
title: "CLUSTER.LOG"
topic: "high-availability"
description: ""
tags: ["high-availability","clusterlog"]
pubDate: "2025-12-01"
---

As a failover cluster resource, there are external interactions between SQL Server, the Windows

Server Failover Cluster service (WSFC) cluster, and the SQL Server resource DLL (hadrres.dll),

that cannot be monitored within SQL Server. The WSFC log, CLUSTER.LOG, can diagnose issues

in the WSFC cluster or in the SQL Server resource DLL.

You can generate the cluster logs in two ways:

1. Use the

command at the command prompt. This command generates

the cluster logs to the \windows\cluster\reports directory on each WSFC node. The

advantage of this method is that you can specify the level of detail in the generated logs

by using the

option. The disadvantage is that you cannot specify the destination

directory for the generated cluster logs. For more information, see

How to create the

cluster.log in Windows Server 2008 Failover Clustering.

2. Use the

Get-ClusterLog

PowerShell cmdlet. The advantage of this method is that you can

generate the cluster log from all nodes to one destination directory on the node that you

run the cmdlet. The disadvantage is that you cannot specify the level of detail in the

generated logs.

The following PowerShell commands generate the cluster logs from all cluster nodes from the

last 15 minutes and place them in the current directory. Run the commands in a PowerShell

window with Administrative privileges.

PowerShell

You can increase the verbosity of the logs in CLUSTER.LOG for an availability group. To modify

the verbosity, follow the steps below:

```cmd
cluster /log /g
/level
Import-Module
FailoverClusters
Get-ClusterLog
-TimeSpan
15
-Destination.
```
