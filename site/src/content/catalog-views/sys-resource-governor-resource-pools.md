---
name: 'sys.resource_governor_resource_pools'
title: 'sys.resource_governor_resource_pools'
category: 'compatibility'
description: 'Returns the stored resource pool configuration. Each row represents a resource pool. Unique ID of the resource pool. Not nullable. Name of the resource pool. Not nullable. Guaranteed average CPU bandwidth for all requests in the resource pool when there is CPU contention. Not nullable. Maximum average CPU bandwidth allowed for all requests in the resource pool when there is CPU contention. Not nul'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns the stored resource pool configuration. Each row represents a resource pool. Unique ID of the resource pool. Not nullable. Name of the resource pool. Not nullable. Guaranteed average CPU bandwidth for all requests in the resource pool when there is CPU contention. Not nullable. Maximum average CPU bandwidth allowed for all requests in the resource pool when there is CPU contention. Not nullable.

## Code Blocks


```sql
pool_id
```


```sql
name
```


```sql
min_cpu_percent
```


```sql
max_cpu_percent
```


```sql
min_memory_percent
```
