---
name: 'sys.dm_os_memory_nodes'
title: 'sys.dm_os_memory_nodes'
category: 'os'
description: 'Analytics Platform System (PDW) Allocations that are internal to SQL Server use the SQL Server memory manager. Tracking the difference between process memory counters from counters can indicate memory use from external components in the SQL Server memory space. Nodes are created per physical NUMA memory nodes. These might be different from the CPU No allocations done directly through Windows memor'
tags: ["os", "dmv"]
pubDate: 2026-05-29
---

## Description

Analytics Platform System (PDW) Allocations that are internal to SQL Server use the SQL Server memory manager. Tracking the difference between process memory counters from counters can indicate memory use from external components in the SQL Server memory space. Nodes are created per physical NUMA memory nodes. These might be different from the CPU No allocations done directly through Windows memory allocations routines are tracked. The
