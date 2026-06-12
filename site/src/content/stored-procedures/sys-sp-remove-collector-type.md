---
name: "sys.sp_remove_collector_type"
title: "core.sp_remove_collector_type"
category: "general"
description: "warehouse database. The procedure must be executed in the context of the management data view shows the registered collector types that can upload data to the management data warehouse. The GUID for the collector type. (with EXECUTE permission) fixed database role."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "core.supported_collector_types"
---

## Description

warehouse database. The procedure must be executed in the context of the management data view shows the registered collector types that can upload data to the management data warehouse. The GUID for the collector type. (with EXECUTE permission) fixed database role.

## Syntax

`core.supported_collector_types`

## Examples

### Example 1

`core.supported_collector_types`

### Example 2

`core.supported_collector_types`

### Example 3

```sql
0
```

### Example 4

```sql
1
```

### Example 5

```sql
core.sp_remove_collector_type [ @collector_type_uid = ]
'collector_type_uid'
[ ; ]
```

### Example 6

`core.sp_remove_collector_type`

### Example 7

```sql
USE
<management_data_warehouse>;
GO
DECLARE
@RC
INT
;
DECLARE
@collector_type_uid UNIQUEIDENTIFIER;
SELECT
@collector_type_uid = (
SELECT collector_type_uid
FROM msdb.dbo.syscollector_collector_types
WHERE name
= N
'Generic T-SQL Query Collector Type'
);
EXECUTE
@RC = core.sp_add_collector_type @collector_type_uid;
```
