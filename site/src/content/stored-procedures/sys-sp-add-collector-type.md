---
name: "sys.sp_add_collector_type"
title: "core.sp_add_collector_type"
category: "general"
description: "warehouse database. The procedure must be executed in the context of the management data Transact-SQL syntax conventions The GUID for the collector type. (with EXECUTE permission) fixed database role. The following example adds the Generic T-SQL Query collector type to the view. By default, the Generic T-SQL Query collector type already exists. Therefore, if you run this code on a default installa"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "core.supported_collector_types"
---

## Description

warehouse database. The procedure must be executed in the context of the management data Transact-SQL syntax conventions The GUID for the collector type. (with EXECUTE permission) fixed database role. The following example adds the Generic T-SQL Query collector type to the view. By default, the Generic T-SQL Query collector type already exists. Therefore, if you run this code on a default installation, you see a message that

## Syntax

`core.supported_collector_types`

## Examples

### Example 1

`core.supported_collector_types`

### Example 2

```sql
0
```

### Example 3

```sql
1
```

### Example 4

`core.supported_collector_types`

### Example 5

```sql
core.sp_add_collector_type [ @collector_type_uid = ]
'collector_type_uid'
[ ; ]
```
