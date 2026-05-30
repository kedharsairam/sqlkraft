---
title: "Work with change data capture"
topic: "change-data-capture"
description: |
  08/22/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Change data is made available to change data capture consumers through table-valued

  functions (TVFs). All queries of these functions r
tags:
  - "change-data-capture"
  - "work-with-change-data-capture"
pubDate: 2025-12-01
---

08/22/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Change data is made available to change data capture consumers through table-valued

functions (TVFs). All queries of these functions require two parameters to define the range of

Log Sequence Numbers (LSNs) that are eligible for consideration when developing the

returned result set. Both the upper and lower LSN values that bound the interval are

considered to be included within the interval.

Several functions are provided to help determine appropriate LSN values for use in querying a

TVF. The function

sys.fn_cdc_get_min_lsn

returns the smallest LSN that is associated with a

capture instance validity interval. The validity interval is the time interval for which change data

is currently available for its capture instances. The function

sys.fn_cdc_get_max_lsn

returns the

largest LSN in the validity interval. The functions

sys.fn_cdc_map_time_to_lsn

and

sys.fn_cdc_map_lsn_to_time

are available to help place LSN values on a conventional timeline.

Because change data capture uses closed query intervals, it is sometimes necessary to generate

the next LSN value in a sequence to ensure that changes are not duplicated in consecutive

query windows. The functions

sys.fn_cdc_increment_lsn

and

sys.fn_cdc_decrement_lsn

are

useful when an incremental adjustment to an LSN value is required.

We recommend validating the LSN boundaries that are to be used in a TVF query before their

use. Null endpoints or endpoints that lie outside the validity interval for a capture instance will

force an error to be returned by a change data capture TVF.

For example, the following error is returned for a query for all changes when a parameter that

is used to define the query interval is not valid, or is out of range, or the row filter option is

invalid.

The corresponding error returned for a

query is the following:

```sql
Msg 313, Level 16, State 3, Line 1
An insufficient number of arguments were supplied for the procedure or function cdc.fn_cdc_get_all_changes_ ...
Msg 313, Level 16, State 3, Line 1
```
