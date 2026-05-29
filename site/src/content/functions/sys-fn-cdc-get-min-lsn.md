---
name: 'sys.fn_cdc_get_min_lsn'
title: 'sys.fn_cdc_get_min_lsn'
category: 'system'
description: 'Returns the start_lsn column value for the specified capture instance from the'
tags: ["function"]
pubDate: 2026-05-29
returnType: 'A. Returning the minimum LSN value for a specified capture'
---

## instance

## B. Verifying the low endpoint of a query range

Requires membership in the sysadmin fixed server role or db_owner fixed database role. For all

other users, requires SELECT permission on all captured columns in the source table and, if a

gating role for the capture instance was defined, membership in that database role.

The following example returns the minimum LSN value for the capture instance

in the AdventureWorks2022 database.

The following example uses the minimum LSN value returned by

to

verify that the proposed low endpoint for a change data query is valid for the current timeline

for the capture instance

. This example assumes that the previous

high endpoint LSN for the capture instance was saved and is available to set the

variable. For the purposes of this example,

is set to 0x000000000000000000 to

force the error-handling section to run.

sys.fn_cdc_get_max_lsn (Transact-SQL)

The Transaction Log (SQL Server)

See Also

```sql
HumanResources_Employee
```

```sql
sys.fn_cdc_get_min_lsn
```

```sql
HumanResources_Employee
```

```sql
@save_to_lsn
```

```sql
@save_to_lsn
```

```sql
USE AdventureWorks2-12;
GO
SELECT sys.fn_cdc_get_min_lsn ('HumanResources_Employee')AS min_lsn;
```

```sql
USE AdventureWorks2022;
GO
DECLARE @min_lsn binary(10), @from_lsn binary(10),@save_to_lsn binary(10), @to_lsn
binary(10);
-- Sets @save_to_lsn to the previous high endpoint saved from the last change data
request.
SET @save_to_lsn = 0x000000000000000000;
-- Sets the upper endpoint for the query range to the current maximum LSN.
SET @to_lsn = sys.fn_cdc_get_max_lsn();
-- Sets the @min_lsn parameter to the current minimum LSN for the capture
instance.
```

```sql
SET @min_lsn = sys.fn_cdc_get_min_lsn ('HumanResources_Employee');
-- Sets the low endpoint for the query range to the LSN that follows the previous
high endpoint.
SET @from_lsn = sys.fn_cdc_increment_lsn(@save_to_lsn);
-- Tests to verify the low endpoint is valid for the current capture instance.
IF (@from_lsn < @min_lsn)
BEGIN
RAISERROR('Low endpoint of the request interval is invalid.', 16, -1);
END
ELSE
-- Return the changes occurring within the query range.
SELECT * FROM cdc.fn_cdc_get_all_changes_HumanResources_Employee(@from_lsn,
@to_lsn, 'all');
GO
```
