---
name: "sys.fn_cdc_map_time_to_lsn"
title: "sys.fn_cdc_map_time_to_lsn"
category: "date-time"
description: "Returns the log sequence number (LSN) value from the system table for the specified time. You can use this function to systematically map datetime ranges into the LSN-based range needed by the change data cdc.fn_cdc_get_all_changes_<capture_instance> cdc.fn_cdc_get_net_changes_<capture_instance> to return data changes within that range. Used to identify a distinct L"
tags: ["date-time","function"]
pubDate: 2026-05-29
syntax: |
  sys.fn_cdc_map_time_to_lsn (
            '<relational_operator>'
            , tracking_time )
            <relational_operator>
            ::=
            { largest less than
            | largest less than or equal
            | smallest greater than
            | smallest greater than or equal
            }
---

## Description

Returns the log sequence number (LSN) value from the system table for the specified time. You can use this function to systematically map datetime ranges into the LSN-based range needed by the change data cdc.fn*cdc_get_all_changes*<capture*instance> cdc.fn_cdc_get_net_changes*<capture_instance> to return data changes within that range.

## Syntax

```sql
sys.fn_cdc_map_time_to_lsn (
'<relational_operator>'
, tracking_time )
<relational_operator>
::=
{ largest less than
| largest less than or equal
| smallest greater than
| smallest greater than or equal
}
```

## Permissions

To understand how the function can be used to map ranges to LSN ranges, consider the following scenario. Assume that a consumer wants to extract change data on a daily basis. That is, the consumer wants only changes for a given day up to and including midnight. The lower bound of the time range would be up to but not including midnight of the previous day. The upper bound would be up to and including midnight of the given day. The following example shows how the function can be used to systematically map this time-based range into the LSN-based range needed by the change data capture enumeration functions to return all changes within that range. SQL The relational operator is used to restrict changes to those that occurred after midnight on the previous day. If multiple entries with different LSN values share the value identified as the lower bound in the cdc.lsn_time_mapping table, the function will return the smallest LSN ensuring that all entries are included. For the upper bound, the relational operator is used to ensure that the range includes all entries for the day including those that have midnight as their value. If multiple entries with different LSN values share the value identified as the upper bound, the function will return the largest LSN ensuring that all entries are included.

## Examples

### Example 1

`sys.fn_cdc_map_time_to_lsn`

### Example 2

`tran_end_time`

### Example 3

```sql
DECLARE
@extraction_time DATETIME,
@lsn
BINARY (10);
SET
@extraction_time =
'2007-01-01 12:00:00.000'
;
SELECT
@lsn = sys.fn_cdc_map_time_to_lsn(
'smallest greater than or equal'
,
@extraction_time);
IF @lsn IS NOT NULL
BEGIN
<
some action
>
END
```
