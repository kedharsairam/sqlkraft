---
title: "Add Dependencies resource"
topic: "high-availability"
description: "This topic describes how to add dependencies to an Always On failover cluster instance (FCI) resource by using the Failover Cluster Manager snap-in. T"
tags: ["high-availability","add-dependencies-resource"]
pubDate: 2025-12-01
---

This topic describes how to add dependencies to an Always On failover cluster instance (FCI)

resource by using the Failover Cluster Manager snap-in. The Failover Cluster Manager snap-in

is the cluster management application for the Windows Server Failover Clustering (WSFC)

service.

Limitations and Restrictions

,

Windows Failover Cluster

Manager

It is important to note that if you add any other resources to the SQL Server group, those

resources must always have their own unique SQL network name resources and their own SQL

IP address resources.

Do not use the existing SQL network name resources and SQL IP address resources for

anything other than SQL Server. If SQL Server resources are shared with other resources, the

following problems may occur:

Outages that are not expected may occur.

Service pack installations may not be successful.

The SQL Server Setup program may not be successful. If this problem occurs, you cannot

install additional instances of SQL Server or perform routine maintenance.

Consider these additional issues:

FTP with SQL Server replication: For instances of SQL Server that use FTP with SQL Server

replication, your FTP service must use one of the same physical disks as the installation of

that is set up to use the FTP service.

resource dependencies: If you add a resource to a SQL Server group and you

have a dependency on the SQL Server resource to make sure that SQL Server is available,
