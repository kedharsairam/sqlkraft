---
name: "sys.dm_io_cluster_shared_drives"
title: "sys.dm_io_cluster_shared_drives"
category: "io"
description: "Azure SQL Managed Instance Analytics Platform System This view returns the drive name of each of the shared drives if the current server instance is a clustered server. If the current server instance is not a clustered instance it returns an empty The name of the drive (the drive letter) that represents an individual disk taking part in the cluster shared disk array. Column is not nullable. The id"
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "SELECT * FROM sys.dm_io_cluster_shared_drives;"
---

## Description

Azure SQL Managed Instance Analytics Platform System This view returns the drive name of each of the shared drives if the current server instance is a clustered server. If the current server instance is not a clustered instance it returns an empty The name of the drive (the drive letter) that represents an individual disk taking part in the cluster shared disk array. Column is not nullable. The identifier for the node that this distribution is on. When clustering is enabled, the failover cluster instance requires data and log files to be on shared disks so that they may be accessed after the instance fails over to another node. Each of the rows in this view represents a single shared disk which is used by this clustered SQL Server instance. Only disks listed by this view can be used to store data or log files for this instance of

## Syntax

```sql
SELECT * FROM sys.dm_io_cluster_shared_drives;
```

## Remarks

Azure SQL Managed Instance

Analytics Platform System

This view returns the drive name of each of the shared drives if the current server instance is a

clustered server. If the current server instance is not a clustered instance it returns an empty

The name of the drive (the drive letter) that represents an individual disk

taking part in the cluster shared disk array. Column is not nullable.

The identifier for the node that this distribution is on.

When clustering is enabled, the failover cluster instance requires data and log files to be on

shared disks so that they may be accessed after the instance fails over to another node. Each of

the rows in this view represents a single shared disk which is used by this clustered SQL Server

instance. Only disks listed by this view can be used to store data or log files for this instance of

SQL Server. The disks listed in this view are those that are in the cluster resource group

associated with the instance.

To call this from Analytics Platform System (PDW), use the name
