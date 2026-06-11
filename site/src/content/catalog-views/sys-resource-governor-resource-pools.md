---
name: "sys.resource_governor_resource_pools"
title: "sys.resource_governor_resource_pools"
category: "compatibility"
description: "Returns the stored resource pool configuration. Each row represents a resource pool. Unique ID of the resource pool. Not nullable."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns the stored resource pool configuration. Each row represents a resource pool. Unique ID of the resource pool. Not nullable. Name of the resource pool. Not nullable. Guaranteed average CPU bandwidth for all requests in the resource pool when there is CPU contention. Not nullable. Maximum average CPU bandwidth allowed for all requests in the resource pool when there is CPU contention. Not nullable.

## Code Blocks

`pool_id`

`name`

`min_cpu_percent`

`max_cpu_percent`

`min_memory_percent`
