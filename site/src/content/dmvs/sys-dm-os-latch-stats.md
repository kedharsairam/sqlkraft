---
name: "sys.dm_os_latch_stats"
title: "sys.dm_os_latch_stats"
category: "os"
description: "Returns information about all latch waits organized by class. Number of waits on latches in this class. This counter is incremented at the start of a latch wait. Total wait time, in milliseconds, on latches in this class. This column is updated every five minutes during a latch wait and at the end of a latch wait."
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: "##MS_ServerStateReader##"
---

## Description

Analytics Platform System (PDW) Returns information about all latch waits organized by class. Number of waits on latches in this class. This counter is incremented at the start of a latch wait. Total wait time, in milliseconds, on latches in this class. This column is updated every five minutes during a latch wait and at the end of a latch wait. Maximum time a memory object has waited on this latch.

## Syntax

```sql
##MS_ServerStateReader##
```

## Permissions

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns information about all latch waits organized by class. latch_class Name of the latch class. waiting_requests_count Number of waits on latches in this class. This counter is incremented at the start of a latch wait. wait_time_ms Total wait time, in milliseconds, on latches in this class. This column is updated every five minutes during a latch wait and at the end of a latch wait. max_wait_time_ms Maximum time a memory object has waited on this latch. If this value is unusually high, it might indicate an internal deadlock. pdw_node_id : Azure Synapse Analytics, Analytics Platform System (PDW) The identifier for the node that this distribution is on. On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, ７ To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the name. This syntax is not supported by serverless SQL pool in Azure Synapse Analytics. ﾉ The following table contains brief descriptions of the various latch classes. ALLOC_CREATE_RINGBUF Used internally by SQL Server to initialize the synchronization of the creation of an allocation ring buffer. ALLOC_CREATE_FREESPACE_CACHE Used to initialize the synchronization of internal free space caches for heaps. ALLOC_CACHE_MANAGER Used to synchronize internal coherency tests. ALLOC_FREESPACE_CACHE Used to synchronize the access to a cache of pages with available space for heaps and binary large objects (BLOBs). Contention on latches of this class can occur when multiple connections try to insert rows into a heap or BLOB at the same time. You can reduce this contention by partitioning the object. Each partition has its own latch. Partitioning will distribute the inserts across multiple latches. ALLOC_EXTENT_CACHE Used to synchronize the access to a cache of extents that contains pages that are not allocated. Contention on latches of this class can occur when multiple connections try to allocate data pages in the same allocation unit at the same time. This contention can be reduced by partitioning the object of which this allocation unit is a part. ACCESS_METHODS_DATASET_PARENT Used to synchronize child dataset access to the parent dataset during parallel operations. ACCESS_METHODS_HOBT_FACTORY Used to synchronize access to an internal hash table. ACCESS_METHODS_HOBT Used to synchronize access to the in-memory representation of a HoBt. ７ does not track latch requests that were granted immediately, or that failed without waiting. ﾉ
