---
name: 'sys.availability_group_listener_ip_addresses'
title: 'sys.availability_group_listener_ip_addresses'
category: 'objects'
description: 'IP resource ONLINE/OFFLINE state from the WSFC'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Permissions


## Description
IP resource ONLINE/OFFLINE state from the WSFC

cluster, one of:

1 = Online. IP resource is online.

0 = Offline. IP resource is offline.

2 = Online Pending. IP resource is offline but is being

brought online.

3 = Failed. IP resource was being brought online but

failed.


## Description of
, one of:

ONLINE

OFFLINE

ONLINE_PENDING

FAILED

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

Querying the SQL Server System Catalog FAQ

Catalog Views (Transact-SQL)


## Permissions for SQL Server 2022 and later
Related content

Last updated on 03/03/2026

```sql
state
```

```sql
state_desc
```

```sql
state
```
