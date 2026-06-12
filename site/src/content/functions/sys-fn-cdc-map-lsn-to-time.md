---
name: "sys.fn_cdc_map_lsn_to_time"
title: "sys.fn_cdc_map_lsn_to_time"
category: "date-time"
description: "Returns the date and time value from the system table for the specified log sequence number (LSN). You can use this function to systematically map LSN ranges to date ranges in a change table. Is the LSN value to match against. This function can be used to determine the time that a change was committed based upon the value returned in the row of change data."
tags: ["date-time","function"]
pubDate: 2026-05-29
syntax: "sys.fn_cdc_map_lsn_to_time ( lsn_value )"
---

## Description

Returns the date and time value from the system table for the specified log sequence number (LSN). You can use this function to systematically map LSN ranges to date ranges in a change table. Is the LSN value to match against. This function can be used to determine the time that a change was committed based upon the value returned in the row of change data.

## Syntax

```sql
sys.fn_cdc_map_lsn_to_time ( lsn_value )
```

## Examples

### Example 1

```sql
sys.fn_cdc_map_lsn_to_time ( lsn_value )
```

### Example 2

`sys.fn_cdc_map_lsn_to_time`

### Example 3

`HumanResources_Employee`

### Example 4

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
