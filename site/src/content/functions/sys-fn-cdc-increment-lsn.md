---
name: "sys.fn_cdc_increment_lsn"
title: "sys.fn_cdc_increment_lsn"
category: "change-data-capture"
description: "Returns the next log sequence number (LSN) in the sequence based upon the specified LSN. Transact-SQL syntax conventions The LSN value returned by the function is always greater than the specified value, and no LSN values exist between the two values. To systematically query a stream of change data over time, you can repeat the query function call periodically, each time specifying a new query int"
tags: ["change-data-capture", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_cdc_increment_lsn"
---

## Description

Returns the next log sequence number (LSN) in the sequence based upon the specified LSN. Transact-SQL syntax conventions The LSN value returned by the function is always greater than the specified value, and no LSN values exist between the two values. To systematically query a stream of change data over time, you can repeat the query function call periodically, each time specifying a new query interval to bound the changes returned in the query. To help insure that no data is lost, the upper bound for the previous query is often used to generate the lower bound for the subsequent query. Because the query interval is a closed interval, the new lower bound must be larger than the previous upper bound, but small enough to ensure no changes have LSN values that lie between this value and the old upper

## Syntax

`sys.fn_cdc_increment_lsn`

## Remarks

Applies to:

Returns the next log sequence number (LSN) in the sequence based upon the specified LSN.

Transact-SQL syntax conventions

The LSN value returned by the function is always greater than the specified value, and no LSN

values exist between the two values.

To systematically query a stream of change data over time, you can repeat the query function

call periodically, each time specifying a new query interval to bound the changes returned in

the query. To help insure that no data is lost, the upper bound for the previous query is often

used to generate the lower bound for the subsequent query. Because the query interval is a

closed interval, the new lower bound must be larger than the previous upper bound, but small

enough to ensure no changes have LSN values that lie between this value and the old upper

bound. The function

is used to obtain this value.

## Examples

### Example 1

`sys.fn_cdc_increment_lsn`

### Example 2

```sql
@save_to_lsn
```

### Example 3

```sql
USE
AdventureWorks2022;
GO
DECLARE
@from_lsn binary (10), @to_lsn binary (10), @save_to_lsn binary (10);
SET
@save_to_lsn = <previous_upper_bound_value>;
SET
@from_lsn = sys.fn_cdc_increment_lsn(@save_to_lsn);
SET
@to_lsn = sys.fn_cdc_get_max_lsn();
SELECT
*
from cdc.fn_cdc_get_all_changes_HumanResources_Employee( @from_lsn,
@to_lsn,
'all'
);
GO
```

### Example 4

```sql
cdc.fn_cdc_get_all_changes_<capture_instance>
```

### Example 5

```sql
cdc.fn_cdc_get_net_changes_<capture_instance>
```

### Example 6

`lsn_value`

### Example 7

```sql
Msg 313, Level 16, State 3, Line 1 An insufficient number of arguments were supplied for the procedure or function
```
