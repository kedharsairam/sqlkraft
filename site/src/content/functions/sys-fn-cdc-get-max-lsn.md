---
name: "sys.fn_cdc_get_max_lsn"
title: "sys.fn_cdc_get_max_lsn"
category: "change-data-capture"
description: "Returns the maximum log sequence number (LSN) from the start_lsn column in the system table. You can use this function to return the high endpoint of the change data capture timeline for any capture instance. This function returns the maximum LSN in the start_lsn column of the table."
tags: ["change-data-capture", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_cdc_get_max_lsn ()"
---

## Description

Returns the maximum log sequence number (LSN) from the start_lsn column in the system table. You can use this function to return the high endpoint of the change data capture timeline for any capture instance. This function returns the maximum LSN in the start_lsn column of the table. As such, it is the last LSN processed by the capture process when changes are propagated to the database change tables. It serves as the high endpoint for the all timelines

## Syntax

```sql
sys.fn_cdc_get_max_lsn ()
```
