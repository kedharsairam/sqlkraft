---
name: "sys.sp_polybase_leave_group"
title: "sp_polybase_leave_group"
category: "general"
description: "2016 (13.x) and later versions Removes a SQL Server instance from a PolyBase group for scale-out computation. The SQL Server instance must have the feature installed. PolyBase enables the integration of non-SQL Server data sources, such as Hadoop and Azure Blob Storage. See also sp_polybase_join_group Requires CONTROL SERVER permission."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_polybase_leave_group;"
---

## Description

2016 (13.x) and later versions Removes a SQL Server instance from a PolyBase group for scale-out computation. The SQL Server instance must have the feature installed. PolyBase enables the integration of non-SQL Server data sources, such as Hadoop and Azure Blob Storage. See also sp_polybase_join_group Requires CONTROL SERVER permission. You can only remove a compute node from a group. After running the stored procedure, restart the PolyBase engine and PolyBase Data Movement Service on the machine. To verify, run the following DMV on the head node:

## Syntax

```sql
sp_polybase_leave_group;
```

## Remarks

2016 (13.x) and later versions

Removes a SQL Server instance from a PolyBase group for scale-out computation.

The SQL Server instance must have the

feature installed. PolyBase enables the

integration of non-SQL Server data sources, such as Hadoop and Azure Blob Storage. See also

sp_polybase_join_group

(success) or

Requires CONTROL SERVER permission.

You can only remove a compute node from a group.

After running the stored procedure, restart the PolyBase engine and PolyBase Data Movement

Service on the machine. To verify, run the following DMV on the head node:

## Examples

### Example 1

```sql
EXECUTE sys.dm_exec_compute_nodes;
```

### Example 2

```sql
EXECUTE sp_polybase_leave_group;
```
