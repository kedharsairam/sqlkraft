---
name: 'sys.fn_cdc_map_lsn_to_time'
title: 'sys.fn_cdc_map_lsn_to_time'
category: 'date-time'
description: 'Returns the date and time value from the'
tags: ["function"]
pubDate: 2026-05-29
---

Article

•

08/10/2023

Applies to:

SQL Server


## Returns the date and time value from the
column in the

cdc.lsn_time_mapping

system table for the specified log sequence number (LSN). You can use this function to

systematically map LSN ranges to date ranges in a change table.

Transact-SQL syntax conventions

lsn_value

Is the LSN value to match against.

lsn_value

is

.

This function can be used to determine the time that a change was committed based upon the

value returned in the row of change data.

Requires membership in the

role.

The following example uses the function

to determine the commit

time associated with the last change processed in the specified LSN interval for the

capture instance.

cdc.lsn_time_mapping (Transact-SQL)

sys.fn_cdc_map_time_to_lsn (Transact-SQL)

cdc.fn_cdc_get_net_changes_<capture_instance> (Transact-SQL)

cdc.fn_cdc_get_all_changes_<capture_instance> (Transact-SQL)

See Also

```sql
sys.fn_cdc_map_lsn_to_time ( lsn_value )
```

```sql
sys.fn_cdc_map_lsn_to_time
```

```sql
HumanResources_Employee
```

```sql
USE AdventureWorks2022;
GO
DECLARE @max_lsn binary(10);
SELECT @max_lsn = MAX(__$start_lsn)
FROM cdc.fn_cdc_get_all_changes_HumanResources_Employee(@from_lsn, @to_lsn,
'all');
SELECT sys.fn_cdc_map_lsn_to_time(@max_lsn);
GO
```
