---
name: 'sys.sp_cdc_disable_table'
title: 'sys.sp_cdc_disable_table'
category: 'general'
description: 'Disables change data capture for the specified source table and capture instance in the current'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

The name of the capture instance to disable for the specified source table.

@capture_instance

is

and can't be

.

When

is specified, all capture instances defined for

@source_name

are disabled.

(success) or

(failure).

None.

drops the change data capture change table and system functions

associated with the specified source table and capture instance. It deletes any rows associated

with the specified capture instance from the change data capture system tables and sets the

column for the table entry in the

sys.tables

catalog view to

.

Requires membership in the

fixed database role.

The following example disables change data capture for the

table.

SQL

Related content

sys.sp_cdc_enable_table (Transact-SQL)

```sql
NULL
```

```sql
all
```

```sql
0
```

```sql
1
```

```sql
sys.sp_cdc_disable_table
```

```sql
is_tracked_by_cdc
```

```sql
0
```

```sql
HumanResources.Employee
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_disable_table
@source_schema = N
'HumanResources'
,
@source_name = N
'Employee'
,
@capture_instance = N
'HumanResources_Employee'
;
```
