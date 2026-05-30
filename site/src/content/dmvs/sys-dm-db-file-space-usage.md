---
name: "sys.dm_db_file_space_usage"
title: "sys.dm_db_file_space_usage"
category: "file"
description: "Analytics Platform System (PDW) Returns space usage information for each data file in the database. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a : SQL Server 2012 (11.x) and later versions. : SQL Server 2012 (11.x) and later versions. Total number of pages in the data file. : SQL Server 2012 (11.x) and later versions. Total number of pa"
tags: ["file", "dmv"]
pubDate: 2026-05-29
syntax: "allocated_extent_page_count"
---

## Description

Analytics Platform System (PDW) Returns space usage information for each data file in the database. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a : SQL Server 2012 (11.x) and later versions. : SQL Server 2012 (11.x) and later versions. Total number of pages in the data file. : SQL Server 2012 (11.x) and later versions. Total number of pages in the allocated extents in the

## Syntax

`allocated_extent_page_count`

## Examples

### Example 1

`tempdb`

### Example 2

`sys.dm_db_file_space_usage.database_id`

### Example 3

```sql
file_id sys.dm_io_virtual_file_stats.database_id
```

### Example 4

`file_id`

### Example 5

```sql
VIEW
SERVER STATE
```

### Example 6

```sql
##MS_ServerStateReader##
```

### Example 7

```sql
VIEW DATABASE STATE
```

### Example 8

```sql
##MS_ServerStateReader##
```
