---
name: 'sys.fn_hadr_distributed_ag_database_replic'
title: 'sys.fn_hadr_distributed_ag_database_replic'
category: 'system'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["function"]
pubDate: 2026-05-29
---

## Description
<captured source

table columns>

varies

The remaining columns returned by the function are the columns

from the source table that were identified as captured columns

when the capture instance was created. If no columns were

specified in the captured column list, all columns in the source

table are returned.

Requires membership in the sysadmin fixed server role or db_owner fixed database role. For all

other users, requires SELECT permission on all captured columns in the source table and, if a

gating role for the capture instance was defined, membership in that database role. When the

caller does not have permission to view the source data, the function returns a row with NULL

values for all the columns.

Modifications on the unique identifier of a row will cause

to show the

initial UPDATE command with a DELETE and then INSERT command instead. This behavior is

necessary to track the key both before and after the change.

Error 313 is expected if LSN range supplied is not appropriate when calling

or

. If the

parameter is beyond the

time of lowest LSN or highest LSN, then execution of these functions will return in error 313:

. This error should be handled by the developer.

The following example uses the function

to report

the net changes made to the source table

during a specific time

interval.

First, the

function is used to mark the beginning of the time interval. After several DML

statements are applied to the source table, the

function is called again to identify the

end of the time interval. The function

sys.fn_cdc_map_time_to_lsn

is then used to map the time

interval to a change data capture query range bounded by LSN values. Finally, the function

is queried to obtain the net changes to the source

table for the time interval. Notice that the row that is inserted and then deleted does not

appear in the result set returned by the function. This is because a row that is first added and

then deleted within a query window produces no net change on the source table for the

interval.

SQL

cdc.fn_cdc_get_all_changes_<capture_instance> (Transact-SQL)

７

Note

Before you run this example, you must first run example B in

to enable CDC on the table

. In the below

example, HR_Department is the name of the CDC capture instance, as specified in

.

See Also

sys.fn_cdc_map_time_to_lsn (Transact-SQL)

sys.sp_cdc_enable_table (Transact-SQL)

sys.sp_cdc_help_change_data_capture (Transact-SQL)

About Change Data Capture (SQL Server)

```sql
fn_cdc_get_net_changes
```

```sql
cdc.fn_cdc_get_all_changes_<capture_instance>
```

```sql
cdc.fn_cdc_get_net_changes_<capture_instance>
```

```sql
lsn_value
```

```sql
Msg 313, Level 16, State 3, Line 1 An insufficient number of arguments were supplied for
the procedure or function
```

```sql
cdc.fn_cdc_get_net_changes_HR_Department
```

```sql
HumanResources.Department
```

```sql
GETDATE
```

```sql
GETDATE
```

```sql
cdc.fn_cdc_get_net_changes_HR_Department
```

```sql
HumanResources.Department
```

```sql
sys.sp_cdc_enable_table
```

```sql
USE
AdventureWorks2022;
GO
DECLARE
@begin_time datetime, @end_time datetime, @from_lsn
binary
(10), @to_lsn
binary
(10);
-- Obtain the beginning of the time interval.
SET
@begin_time =
DATEADD
(
day
, -1,
GETDATE
()) ;
-- DML statements to produce changes in the HumanResources.Department table.
INSERT
INTO
HumanResources.Department (
Name
, GroupName)
VALUES
(N
'MyDept'
, N
'MyNewGroup'
);
UPDATE
HumanResources.Department
SET
GroupName = N
'Resource Control'
WHERE
GroupName = N
'Inventory Management'
;
DELETE
FROM
HumanResources.Department
WHERE
Name
= N
'MyDept'
;
-- Obtain the end of the time interval.
SET
@end_time =
GETDATE
();
-- Map the time interval to a change data capture query range.
SET
@from_lsn = sys.fn_cdc_map_time_to_lsn(
'smallest greater than or equal'
,
@begin_time);
SET
@from_lsn =
ISNULL
(sys.fn_cdc_map_time_to_lsn(
'smallest greater than or
equal'
, @begin_time), [
sys
].[fn_cdc_get_min_lsn](
'HR_Department'
) );
SET
@to_lsn = sys.fn_cdc_map_time_to_lsn(
'largest less than or equal'
, @end_time);
-- Return the net changes occurring within the query window.
SELECT
*
FROM
cdc.fn_cdc_get_net_changes_HR_Department(@from_lsn, @to_lsn,
'all'
);
```
