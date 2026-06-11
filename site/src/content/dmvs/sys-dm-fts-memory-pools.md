---
name: "sys.dm_fts_memory_pools"
title: "sys.dm_fts_memory_pools"
category: "full-text"
description: "SQL database in Microsoft Fabric Returns information about the shared memory pools available to the Full-Text Gatherer component for a full-text crawl or a full-text crawl range."
tags: ["full-text", "dmv"]
pubDate: 2026-05-29
syntax: "##MS_ServerStateReader##"
---

## Description

SQL database in Microsoft Fabric Returns information about the shared memory pools available to the Full-Text Gatherer component for a full-text crawl or a full-text crawl range. ID of the allocated memory pool. Size of each allocated buffer in the memory pool. Minimum number of buffers allowed in the memory pool. Maximum number of buffers allowed in the memory pool. Current number of shared memory buffers in the memory pool.

## Syntax

```sql
##MS_ServerStateReader##
```
