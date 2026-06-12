---
name: "sys.availability_read_only_routing_lists"
title: "sys.availability_read_only_routing_lists"
category: "compatibility"
description: "Returns a row for the read-only routing list of each availability replica in an Always On availability group in the WSFC failover cluster. Unique ID of the availability replica that owns the routing list. Priority order for routing (1 is first, 2 is second, and so forth). Unique ID of the availability replica to which a read-only The visibility of the metadata in catalog views is limited to secura"
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
---

## Description

Returns a row for the read-only routing list of each availability replica in an Always On availability group in the WSFC failover cluster. Unique ID of the availability replica that owns the routing list. Priority order for routing (1 is first, 2 is second, and so forth). Unique ID of the availability replica to which a read-only The visibility of the metadata in catalog views is limited to securables that a user either owns,

## Permissions

ﾃ Summarize this article for me Description Unique ID of the availability replica that owns the routing list. Priority order for routing (1 is first, 2 is second, and so forth). Unique ID of the availability replica to which a read-only workload is routed. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. Requires VIEW SERVER PERFORMANCE STATE permission on the server. Always On Availability Groups Dynamic Management Views and Functions (Transact-SQL) Always On Availability Groups Catalog Views (Transact-SQL) Monitor Availability Groups (Transact-SQL) What is an Always On availability group? ﾉ Expand table Permissions for SQL Server 2022 and later
## Code Blocks

`replica_id`

`routing_priority`

`read_only_replica_id`
