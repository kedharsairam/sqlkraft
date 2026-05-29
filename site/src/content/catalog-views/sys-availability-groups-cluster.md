---
name: 'sys.availability_groups_cluster'
title: 'sys.availability_groups_cluster (Transact-'
category: 'objects'
description: '2: Prefer Secondary. Performing backups on a'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
2: Prefer Secondary. Performing backups on a

secondary replica is preferable, but performing

backups on the primary replica is acceptable if no

secondary replica is available for backup

operations. This is the default behavior.

3: Any Replica. No preference about whether

backups are performed on the primary replica or

on a secondary replica.

For more information, see

Offload supported

backups to secondary replicas of an availability

group

.


## Description of
, one

of:

PRIMARY

SECONDARY_ONLY

SECONDARY

NONE

In a Windows Server Failover Cluster (WSFC), the cluster columns display the Windows cluster

details. In cases where there's no Windows cluster, such as

read-scale availability groups

, or

availability groups on Linux

, columns related to the cluster might display data about an internal

default cluster. These columns are for internal use only and can be disregarded.

Requires VIEW ANY DEFINITION permission on the server instance.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

sys.availability_replicas (Transact-SQL)

What is an Always On availability group?


## Permissions for SQL Server 2022 and later
Related content

Monitor Availability Groups (Transact-SQL)

Last updated on 03/03/2026

```sql
automated_backup_preference_desc
```

```sql
automated_backup_preference
```
