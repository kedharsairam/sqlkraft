---
name: 'sys.sp_cdc_get_captured_columns'
title: 'sys.sp_cdc_get_captured_columns'
category: 'general'
description: 'Returns change data capture metadata information for the captured source columns tracked'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

Requires membership in the

fixed database role. For all other users, requires SELECT

permission on all captured columns in the source table and, if a gating role for the capture

instance was defined, membership in that database role. When the caller doesn't have

permission to view the source data, the function returns Error 22981 (

).

The following example returns information about the captured columns in the

capture instance.

SQL

sys.sp_cdc_help_change_data_capture (Transact-SQL)

Related content

```sql
Object doesn't exist or
access is denied.
```

```sql
HumanResources_Employee
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_get_captured_columns @capture_instance =
N
'HumanResources_Employee'
;
GO
```
