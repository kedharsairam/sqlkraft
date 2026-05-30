---
name: "sys.fn_cdc_decrement_lsn"
title: "sys.fn_cdc_decrement_lsn"
category: "change-data-capture"
description: "Returns the previous log sequence number (LSN) in the sequence based upon the specified Transact-SQL syntax conventions The LSN returned by the function is always less than the specified value, and no LSN values can"
tags: ["change-data-capture", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_cdc_decrement_lsn ( lsn_value )"
---

## Description

Returns the previous log sequence number (LSN) in the sequence based upon the specified Transact-SQL syntax conventions The LSN returned by the function is always less than the specified value, and no LSN values can

## Syntax

```sql
sys.fn_cdc_decrement_lsn ( lsn_value )
```

## Examples

### Example 1

```sql
sys.fn_cdc_decrement_lsn ( lsn_value )
```

### Example 2

```sql
sys.fn_cdc_decrement_lsn
```

### Example 3

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

### Example 4

```sql
cdc.fn_cdc_get_all_changes_<capture_instance>
```

### Example 5

```sql
cdc.fn_cdc_get_net_changes_<capture_instance>
```

### Example 6

```sql
lsn_value
```

### Example 7

```sql
Msg 313, Level 16, State 3, Line 1 An insufficient number of arguments were
supplied for the procedure or function
```
