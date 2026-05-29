---
name: 'sys.fn_cdc_increment_lsn'
title: 'sys.fn_cdc_increment_lsn'
category: 'system'
description: 'Returns the next log sequence number (LSN) in the sequence based upon the specified LSN.'
tags: ["function"]
pubDate: 2026-05-29
---

Requires membership in the

database role.

The following example uses

to generate a new lower bound value

for a change data capture query based on the upper bound saved from a previous query and

saved in the variable

.

SQL

sys.fn_cdc_decrement_lsn (Transact-SQL)

cdc.fn_cdc_get_all_changes_<capture_instance> (Transact-SQL)

cdc.fn_cdc_get_net_changes_<capture_instance> (Transact-SQL)

The Transaction Log (SQL Server)

About Change Data Capture (SQL Server)

７

Note

Error 313 is expected if LSN range supplied is not appropriate when calling

or

. If the

parameter is beyond

the time of lowest LSN or highest LSN, then execution of these functions will return in

error 313:

. This error should be handled by the developer.

See Also

```sql
sys.fn_cdc_increment_lsn
```

```sql
@save_to_lsn
```

```sql
USE
AdventureWorks2022;
GO
DECLARE
@from_lsn
binary
(10), @to_lsn
binary
(10), @save_to_lsn
binary
(10);
SET
@save_to_lsn = <previous_upper_bound_value>;
SET
@from_lsn = sys.fn_cdc_increment_lsn(@save_to_lsn);
SET
@to_lsn = sys.fn_cdc_get_max_lsn();
SELECT
*
from
cdc.fn_cdc_get_all_changes_HumanResources_Employee( @from_lsn,
@to_lsn,
'all'
);
GO
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
Msg 313, Level 16, State 3, Line 1 An insufficient number of arguments were
supplied for the procedure or function
```
