---
name: "sys.fn_cdc_is_bit_set"
title: "sys.fn_cdc_is_bit_set"
category: "change-data-capture"
description: "Indicates whether a captured column has been updated by checking whether its ordinal position is set within a provided bitmask. Is the ordinal position in the mask to check. Is the mask identifying updated columns. This function is typically used as part of a change data query to indicate whether a column has changed. In this scenario, the function sys.fn_cdc_get_co"
tags: ["change-data-capture","function"]
pubDate: 2026-05-29
syntax: "sys.fn_cdc_is_bit_set ( position , update_mask )"
---

## Description

Indicates whether a captured column has been updated by checking whether its ordinal position is set within a provided bitmask. Is the ordinal position in the mask to check. Is the mask identifying updated columns. This function is typically used as part of a change data query to indicate whether a column has changed. In this scenario, the function sys.fn_cdc_get_column_ordinal is used before the query to obtain the required column ordinal. is then applied to each row of change data that is returned, providing the column-specific information as part of the returned We recommend using this function instead of the function sys.fn_cdc_has_column_changed when determining whether columns have changed for all rows of a returned result set.

## Syntax

```sql
sys.fn_cdc_is_bit_set ( position , update_mask )
```

## Remarks

Indicates whether a captured column has been updated by checking whether its ordinal

position is set within a provided bitmask.

Is the ordinal position in the mask to check.

update_mask

Is the mask identifying updated columns.

update_mask

This function is typically used as part of a change data query to indicate whether a column has

changed. In this scenario, the function

sys.fn_cdc_get_column_ordinal

is used before the query

to obtain the required column ordinal.

is then applied to each row of

change data that is returned, providing the column-specific information as part of the returned

result set.

We recommend using this function instead of the function

sys.fn_cdc_has_column_changed

when determining whether columns have changed for all rows of a returned result set.

## Examples

### Example 1

`sys.fn_cdc_is_bit_set`

### Example 2

`cdc.fn_cdc_get_all_changes_HR_Department`

### Example 3

`IsGroupNmUpdated`

### Example 4

```sql
__$update_mask
```

### Example 5

```sql
USE AdventureWorks2022;
GO
DECLARE @from_lsn binary(10), @to_lsn binary(10), @GroupNm_ordinal int;
SET @from_lsn = sys.fn_cdc_get_min_lsn('HR_Department');
SET @to_lsn = sys.fn_cdc_get_max_lsn();
SET @GroupNm_ordinal = sys.fn_cdc_get_column_ordinal('HR_Department','GroupName');
SELECT sys.fn_cdc_is_bit_set(@GroupNm_ordinal,__$update_mask) as
'IsGroupNmUpdated', *
FROM cdc.fn_cdc_get_all_changes_HR_Department( @from_lsn, @to_lsn, 'all')
WHERE __$operation = 4;
GO
```
