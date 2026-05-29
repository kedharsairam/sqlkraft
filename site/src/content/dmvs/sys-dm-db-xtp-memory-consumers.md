---
name: 'sys.dm_db_xtp_memory_consumers'
title: 'sys.dm_db_xtp_memory_consumers'
category: 'in-memory'
description: 'Reports the database-level memory consumers in the In-Memory OLTP database engine. The view returns a row for each memory consumer that the database engine uses. Use this DMV to see how the memory is distributed across different internal objects. In-Memory OLTP overview and usage scenarios ID (internal) of the memory consumer. 0 = Aggregation. (Aggregates memory usage of two or more consumers. It '
tags: ["in-memory", "dmv"]
pubDate: 2026-05-29
syntax: 'memory_consumer_type_desc'
---

## Description

Reports the database-level memory consumers in the In-Memory OLTP database engine. The view returns a row for each memory consumer that the database engine uses. Use this DMV to see how the memory is distributed across different internal objects. In-Memory OLTP overview and usage scenarios ID (internal) of the memory consumer. 0 = Aggregation. (Aggregates memory usage of two or more consumers. It shouldn't be displayed.)

## Syntax

```sql
memory_consumer_type_desc
```
