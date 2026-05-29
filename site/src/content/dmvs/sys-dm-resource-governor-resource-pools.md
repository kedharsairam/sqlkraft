---
name: "sys.dm_resource_governor_resource_pools"
title: "sys.dm_resource_governor_resource_pools"
category: "resource-governor"
description: "Analytics Platform System (PDW) Returns information about the current resource pool state, the current configuration of resource pools, and resource pool statistics. The ID of the resource pool. Not nullable. The name of the resource pool. Not nullable. The time when statistics was reset for this pool. The cumulative CPU usage in milliseconds since the resource governor statistics were reset. Not "
tags: ["resource-governor", "dmv"]
pubDate: 2026-05-29
syntax: "statistics_start_time"
---

## Description

Analytics Platform System (PDW) Returns information about the current resource pool state, the current configuration of resource pools, and resource pool statistics. The ID of the resource pool. Not nullable. The name of the resource pool. Not nullable. The time when statistics was reset for this pool. The cumulative CPU usage in milliseconds since the resource governor statistics were reset. Not The current total cache memory usage in

## Syntax

```sql
statistics_start_time
```

## Permissions

This catalog view displays the stored metadata. To see the currently effective resource governor configuration, use the corresponding dynamic management view, sys.dm_resource_governor_resource_pools (Transact-SQL) . Requires the permission. Resource governor catalog views (Transact-SQL) sys.dm_resource_governor_resource_pools (Transact-SQL) Resource governor sys.resource_governor_external_resource_pools (Transact-SQL) Related content
