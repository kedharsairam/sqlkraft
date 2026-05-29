---
name: 'sys.sp_cdc_enable_table'
title: 'sys.sp_cdc_enable_table'
category: 'general'
description: 'Enables change data capture for the specified source table in the current database. When a'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## A. Enable change data capture by specifying only required

## parameters

Before you can enable a table for change data capture, the database must be enabled. To

determine whether the database is enabled for change data capture, query the

column in the

sys.databases

catalog view. To enable the database, use the

sys.sp_cdc_enable_db

stored procedure.

When change data capture is enabled for a table, a change table and one or two query

functions are generated. The change table serves as a repository for the source table changes

extracted from the transaction log by the capture process. The query functions are used to

extract data from the change table. The names of these functions are derived from the

@capture_instance

parameter in the following ways:

All changes function:

Net changes function:

also creates the capture and cleanup jobs for the database if the

source table is the first table in the database to be enabled for change data capture and no

transactional publications exist for the database. It sets the

column in the

sys.tables

catalog view to

.

SQL Server Agent doesn't have to be running when CDC is enabled for a table. However, the

capture process doesn't process the transaction log and write entries to the change table

unless SQL Server Agent is running.

Requires membership in the

fixed database role.

The following example enables change data capture for the

table.

Only the required parameters are specified.

SQL

## B. Enable change data capture by specifying additional

## optional parameters

The following example enables change data capture for the

table.

All parameters except

@allow_partition_switch

are specified.

SQL

sys.sp_cdc_disable_table (Transact-SQL)

sys.sp_cdc_help_change_data_capture (Transact-SQL)

cdc.fn_cdc_get_all_changes_<capture_instance> (Transact-SQL)

cdc.fn_cdc_get_net_changes_<capture_instance> (Transact-SQL)

sys.sp_cdc_help_jobs (Transact-SQL)

Related content

```sql
is_cdc_enabled
```

```sql
cdc.fn_cdc_get_all_changes_<capture_instance>
```

```sql
cdc.fn_cdc_get_net_changes_<capture_instance>
sys.sp_cdc_enable_table
```

```sql
is_tracked_by_cdc
```

```sql
1
```

```sql
HumanResources.Employee
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_enable_table
@source_schema = N
'HumanResources'
,
```

```sql
HumanResources.Department
```

```sql
@source_name = N
'Employee'
,
@role_name = N
'cdc_Admin'
;
GO
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_enable_table
@source_schema = N
'HumanResources'
,
@source_name = N
'Department'
,
@role_name = N
'cdc_admin'
,
@capture_instance = N
'HR_Department'
,
@supports_net_changes = 1,
@index_name = N
'AK_Department_Name'
,
@captured_column_list = N
'DepartmentID, Name, GroupName'
,
@filegroup_name = N
'PRIMARY'
;
GO
```
