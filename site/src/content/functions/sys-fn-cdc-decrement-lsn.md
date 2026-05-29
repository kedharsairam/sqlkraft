---
name: 'sys.fn_cdc_decrement_lsn'
title: 'sys.fn_cdc_decrement_lsn'
category: 'system'
description: 'Returns the previous log sequence number (LSN) in the sequence based upon the specified'
tags: ["function"]
pubDate: 2026-05-29
---

Article

•

07/02/2024

Applies to:

SQL Server


## Returns the previous log sequence number (LSN) in the sequence based upon the specified
LSN.

Transact-SQL syntax conventions


## syntaxsql
LSN value.

lsn_value

is

.

The LSN returned by the function is always less than the specified value, and no LSN values can

exist between the two values.

Requires membership in the

database role.

The following example uses

to set the upper LSN boundary in a

query that returns change data rows that have LSN values less than the maximum LSN value.

SQL

sys.fn_cdc_increment_lsn (Transact-SQL)

sys.fn_cdc_get_min_lsn (Transact-SQL)

sys.fn_cdc_get_max_lsn (Transact-SQL)

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
sys.fn_cdc_decrement_lsn ( lsn_value )
```

```sql
sys.fn_cdc_decrement_lsn
```

```sql
Use
AdventureWorks2022;
GO
DECLARE
@from_lsn
binary
(10), @to_lsn
binary
(10);
SET
@from_lsn = sys.fn_cdc_get_min_lsn(
'HumanResources_Employee'
);
SET
@to_lsn = sys.fn_cdc_decrement_lsn(sys.fn_cdc_get_max_lsn());
SELECT
*
FROM
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
