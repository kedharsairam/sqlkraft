---
name: 'sys.dm_os_cluster_nodes'
title: 'sys.dm_os_cluster_nodes'
category: 'os'
description: 'Analytics Platform System (PDW) Returns one row for each node in the failover cluster instance configuration. If the current instance is a failover clustered instance, it returns a list of nodes on which this failover cluster instance (formerly "virtual server") has been defined. If the current server instance is not a failover clustered instance, it returns an empty rowset. Name of a node in the '
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT NodeName, status, status_description, is_current_owner
  FROM sys.dm_os_cluster_nodes;
---

## Description

Analytics Platform System (PDW) Returns one row for each node in the failover cluster instance configuration. If the current instance is a failover clustered instance, it returns a list of nodes on which this failover cluster instance (formerly "virtual server") has been defined. If the current server instance is not a failover clustered instance, it returns an empty rowset. Name of a node in the SQL Server failover cluster instance (virtual

## Syntax

```sql
SELECT NodeName, status, status_description, is_current_owner
FROM sys.dm_os_cluster_nodes;
```

## Examples

### Example 1

```sql
SELECT NodeName, status, status_description, is_current_owner
FROM sys.dm_os_cluster_nodes;
```

### Example 2

```sql
fn_virtualservernodes
```

### Example 3

```sql
fn_virtualservernodes()
```

### Example 4

```sql
sys.numbered_procedures
sys.numbered_procedure_parameters
```

### Example 5

```sql
sys.dm_os_cluster_nodes
sys.dm_io_cluster_shared_drives
```

### Example 6

```sql
sys.sql_dependencies
sys.sql_expression_dependencies
sys.sql_dependencies
```

### Example 7

```sql
sp_db_vardecimal_storage_format
```

### Example 8

```sql
sp_db_vardecimal_storag
```

### Example 9

```sql
sp_estimated_rowsize_reduction_for_vardecimal
```

### Example 10

```sql
sp_estimate_data_compression_savings
sp_estimated_rowsize_re
```
