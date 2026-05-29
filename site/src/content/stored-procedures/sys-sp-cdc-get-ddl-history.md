---
name: 'sys.sp_cdc_get_ddl_history'
title: 'sys.sp_cdc_get_ddl_history'
category: 'general'
description: 'Returns the data definition language (DDL) change history associated with the specified'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## Description
Name of the capture instance.

Indicates the DDL change required a column in the change

table to be altered to reflect a data type change made to the

source column.

The DDL statement applied to the source table.

Log sequence number (LSN) associated with the DDL change.

Time associated with the DDL change.

DDL modifications to the source table that change the source table column structure, such as

adding or dropping a column, or changing the data type of an existing column, are maintained

in the

cdc.ddl_history

table. These changes can be reported by using this stored procedure.

Entries in

are made at the time the capture process reads the DDL transaction

in the log.

Requires membership in the

fixed database role to return rows for all capture

instances in the database. For all other users, requires SELECT permission on all captured

columns in the source table and, if a gating role for the capture instance was defined,

membership in that database role.

The following example adds a column to the source table

and then

runs the

stored procedure to report the DDL changes that apply

to the source table associated with the capture instance

.

SQL

sys.sp_cdc_help_change_data_capture (Transact-SQL)

Related content

```sql
capture_instance
```

```sql
required_column_update
```

```sql
ddl_command
```

```sql
ddl_lsn
```

```sql
ddl_time
```

```sql
cdc.ddl_history
```

```sql
HumanResources.Employee
```

```sql
sys.sp_cdc_get_ddl_history
```

```sql
HumanResources_Employee
```

```sql
USE
AdventureWorks2022;
GO
ALTER
TABLE
HumanResources.Employee
ADD
Test_Column
INT
NULL
;
GO
```

```sql
-- Pause 10 seconds to allow the event to be logged.
WAITFOR DELAY '00:00:10';
GO
EXECUTE
sys.sp_cdc_get_ddl_history @capture_instance =
'HumanResources_Employee'
;
GO
```
