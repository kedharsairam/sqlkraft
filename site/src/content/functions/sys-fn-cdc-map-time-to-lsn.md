---
name: 'sys.fn_cdc_map_time_to_lsn'
title: 'sys.fn_cdc_map_time_to_lsn'
category: 'date-time'
description: 'Returns the log sequence number (LSN) value from the'
tags: ["function"]
pubDate: 2026-05-29
---

Requires membership in the

role.

The following example uses the

function to determine whether

there are any rows in the

cdc.lsn_time_mapping

table with a

value that is greater

than or equal to midnight. This query can be used to determine, for example, whether the

capture process has already processed the changes committed through midnight of the

previous day, so that the extraction of change data for that day can proceed.

SQL

cdc.lsn_time_mapping (Transact-SQL)

sys.fn_cdc_map_lsn_to_time (Transact-SQL)

cdc.fn_cdc_get_net_changes_<capture_instance> (Transact-SQL)

cdc.fn_cdc_get_all_changes_<capture_instance> (Transact-SQL)

See also

```sql
sys.fn_cdc_map_time_to_lsn
```

```sql
tran_end_time
```

```sql
DECLARE
@extraction_time DATETIME,
@lsn
BINARY
(10);
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
some
action
>
END
```
