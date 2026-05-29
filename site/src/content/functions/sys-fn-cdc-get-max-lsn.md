---
name: 'sys.fn_cdc_get_max_lsn'
title: 'sys.fn_cdc_get_max_lsn'
category: 'system'
description: 'Returns the maximum log sequence number (LSN) from the start_lsn column in the'
tags: ["function"]
pubDate: 2026-05-29
returnType: 'A. Returning the maximum LSN value'
---

Article

•

08/10/2023

Applies to:

SQL Server


## Returns the maximum log sequence number (LSN) from the start_lsn column in the
cdc.lsn_time_mapping

system table. You can use this function to return the high endpoint of

the change data capture timeline for any capture instance.

Transact-SQL syntax conventions

This function returns the maximum LSN in the start_lsn column of the

cdc.lsn_time_mapping

table. As such, it is the last LSN processed by the capture process when changes are

propagated to the database change tables. It serves as the high endpoint for the all timelines

that are associated with capture instances defined for the database.

The function is typically used to obtain an appropriate high endpoint for a query interval.

Requires membership in the public database role.

## B. Setting the high endpoint of a query range

The following example returns the maximum LSN for all capture instances in the

AdventureWorks2022 database.

The following example uses the maximum LSN returned by

to set the

high endpoint for a query range for the capture instance

.

sys.fn_cdc_get_min_lsn (Transact-SQL)

The Transaction Log (SQL Server)

See Also

```sql
sys.fn_cdc_get_max_lsn ()
```

```sql
sys.fn_cdc_get_max_lsn
```

```sql
HumanResources_Employee
```

```sql
USE AdventureWorks2022;
GO
SELECT sys.fn_cdc_get_max_lsn()AS max_lsn;
```

```sql
USE AdventureWorks2022;
GO
DECLARE @from_lsn binary(10), @to_lsn binary(10);
SET @from_lsn = sys.fn_cdc_get_min_lsn(N'HumanResources_Employee');
SET @to_lsn = sys.fn_cdc_get_max_lsn();
SELECT * FROM cdc.fn_cdc_get_all_changes_HumanResources_Employee(@from_lsn,
@to_lsn, 'all');
GO
```
