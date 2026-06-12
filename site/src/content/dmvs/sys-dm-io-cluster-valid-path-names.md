---
name: "sys.dm_io_cluster_valid_path_names"
title: "sys.dm_io_cluster_valid_path_names"
category: "io"
description: "Returns information on all valid shared disks, including clustered shared volumes, for a SQL Server failover cluster instance. If the instance isn't clustered, an empty rowset is returned. Volume mount point or drive path that can be used as a root directory for database and log files. Not nullable. Current owner of the drive. For cluster shared volumes (CSV), the owner is the node which is hostin"
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "is_cluster_shared_volume"
---

## Description

Returns information on all valid shared disks, including clustered shared volumes, for a SQL Server failover cluster instance. If the instance isn't clustered, an empty rowset is returned. Volume mount point or drive path that can be used as a root directory for database and log files. Not nullable. Current owner of the drive. For cluster shared volumes (CSV), the owner is the node which is hosting the MetaData

## Syntax

`is_cluster_shared_volume`

## Permissions

Article • 02/28/2023 If the current server is a clustered server, returns the drive name of the shared drives. If the current server instance is not a clustered server, returns an empty rowset. returns a list of shared drives used by this clustered server. These shared drives belong to the same cluster group as the Microsoft SQL Server resource. Further, the SQL Server resource is dependent on these drives. This function is helpful in identifying drives available to users. The user must have VIEW SERVER STATE permission for the SQL Server instance. ） Important This SQL Server system function is included for backward compatibility. We recommend that you use instead.

## Examples

### Example 1

`path_name`

### Example 2

`cluster_owner_node`

### Example 3

`is_cluster_shared_volume`

### Example 4

```sql
1
```

### Example 5

```sql
0
```

### Example 6

```sql
VIEW SERVER STATE
```

### Example 7

```sql
VIEW SERVER PERFORMANCE STATE
```
