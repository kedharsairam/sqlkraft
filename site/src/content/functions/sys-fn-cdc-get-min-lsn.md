---
name: "sys.fn_cdc_get_min_lsn"
title: "sys.fn_cdc_get_min_lsn"
category: "change-data-capture"
description: "Returns the start_lsn column value for the specified capture instance from the cdc.change_tables system table. This value represents the low endpoint of the validity interval for the capture instance. Transact-SQL syntax conventions capture_instance_name Is the name of the capture instance."
tags: ["change-data-capture", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_cdc_get_min_lsn ( 'capture_instance_name' )"
---

## Description

Returns the start_lsn column value for the specified capture instance from the cdc.change_tables system table. This value represents the low endpoint of the validity interval for the capture instance. Transact-SQL syntax conventions capture_instance_name Is the name of the capture instance. capture_instance_name Returns 0x00000000000000000000 when the capture instance does not exist or when the caller is not authorized to access the change data associated with the capture instance. This function is typically used to identify the low endpoint of the change data capture timeline associated with a capture instance. You can also use this function to validate that the endpoints of a query range fall within the capture instance timeline before requesting change data. It is important to perform such checks because the low endpoint of a capture instance changes

## Syntax

```sql
sys.fn_cdc_get_min_lsn ( 'capture_instance_name' )
```

## Remarks

Applies to:

Returns the start_lsn column value for the specified capture instance from the

cdc.change_tables

system table. This value represents the low endpoint of the validity interval

for the capture instance.

Transact-SQL syntax conventions

capture_instance_name

Is the name of the capture instance.

capture_instance_name

Returns 0x00000000000000000000 when the capture instance does not exist or when the caller

is not authorized to access the change data associated with the capture instance.

This function is typically used to identify the low endpoint of the change data capture timeline

associated with a capture instance. You can also use this function to validate that the endpoints

of a query range fall within the capture instance timeline before requesting change data. It is

important to perform such checks because the low endpoint of a capture instance changes

when cleanup is performed on the change tables. If the time between requests for change data

is significant, even a low endpoint that is set to the high endpoint of the previous change data

request might lie outside the current timeline.
