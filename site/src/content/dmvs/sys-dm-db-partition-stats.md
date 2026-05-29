---
name: 'sys.dm_db_partition_stats'
title: 'sys.dm_db_partition_stats'
category: 'io'
description: 'Analytics Platform System (PDW) Returns page and row-count information for every partition in the current database. ID of the partition. This is unique within a database. This is catalog view except for Azure Synapse Analytics. Object ID of the table or indexed view that the partition is ID of the heap or index the partition is part of. 1-based partition number within the index or heap. Number of '
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: 'in_row_data_page_count'
---

## Description

Analytics Platform System (PDW) Returns page and row-count information for every partition in the current database. ID of the partition. This is unique within a database. This is catalog view except for Azure Synapse Analytics. Object ID of the table or indexed view that the partition is ID of the heap or index the partition is part of. 1-based partition number within the index or heap. Number of pages in use for storing in-row data in this

## Syntax

```sql
in_row_data_page_count
```
