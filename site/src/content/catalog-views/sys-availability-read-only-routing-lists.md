---
name: 'sys.availability_read_only_routing_lists'
title: 'sys.availability_read_only_routing_lists'
category: 'objects'
description: 'Summarize this article for me'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

ﾃ

Summarize this article for me

Applies to:

SQL Server


## Returns a row for the read-only routing list of each availability replica in an Always On
availability group in the WSFC failover cluster.


## Description
Unique ID of the availability replica that owns the routing list.

Priority order for routing (1 is first, 2 is second, and so forth).

Unique ID of the availability replica to which a read-only

workload is routed.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

Always On Availability Groups Dynamic Management Views and Functions (Transact-SQL)

Always On Availability Groups Catalog Views (Transact-SQL)

Monitor Availability Groups (Transact-SQL)

What is an Always On availability group?

Last updated on 03/03/2026

ﾉ

Expand table


## Permissions for SQL Server 2022 and later
Related content

```sql
replica_id
```

```sql
routing_priority
```

```sql
read_only_replica_id
```
