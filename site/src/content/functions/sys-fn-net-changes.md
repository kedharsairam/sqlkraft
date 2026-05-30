---
name: "sys.fn_net_changes_"
title: "sys.fn_net_changes_<capture_instance>"
category: "system"
description: "'D' - delete operation 'M' - either insert operation or update operation @update_flag_list> A bit flag that is named by appending _uflag to the column name. The flag takes on a non-NULL value only when row_filter_option and __CDC_OPERATION . It is set to 1 if the corresponding column was modified within the query window. function serves as a wrapper for the query function. The stored procedure is "
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "sys.sp_cdc_generate_wrapper_function"
---

## Description

'D' - delete operation 'M' - either insert operation or update operation @update_flag_list> A bit flag that is named by appending \_uflag to the column name. The flag takes on a non-NULL value only when row_filter_option and \_\_CDC_OPERATION . It is set to 1 if the corresponding column was modified within the query window. function serves as a wrapper for the query function. The stored procedure is used to create the script for the wrapper. Wrapper functions are not created automatically. There are two things you must do to create wrapper functions: 1. Run the stored procedure to generate the script to create the wrapper. 2. Execute the script to actually create the wrapper function. Wrapper functions enable users to systematically query for changes that occurred within an interval bounded by

## Syntax

`sys.sp_cdc_generate_wrapper_function`

## Remarks

Description

'D' - delete operation

'M' - either insert operation or update operation

<columns from

@update_flag_list>

A bit flag that is named by appending \_uflag to the column name.

The flag takes on a non-NULL value only when

row_filter_option

and \_\_CDC_OPERATION

. It is set to 1 if the

corresponding column was modified within the query window.

Otherwise, 0.

function serves as a wrapper for the

query function. The

stored procedure is used to create the script for the wrapper.

Wrapper functions are not created automatically. There are two things you must do to create

wrapper functions:

1. Run the stored procedure to generate the script to create the wrapper.

2. Execute the script to actually create the wrapper function.

Wrapper functions enable users to systematically query for changes that occurred within an

interval bounded by

values instead of by LSN values. The wrapper functions perform

all the required conversions between the provided

values and the LSN values needed

internally as arguments to the query functions. When the wrapper functions are used serially to

process a stream of change data, they ensure that no data is lost or repeated provided that the

following convention is followed: the @end_time value of the interval associated with one call

is supplied as the @start_time value for the interval associated with the subsequent call.

By using the @closed_high_end_point parameter when you create the script, you can generate

wrappers to support either a closed upper bound or an open upper bound on the specified

query window. That is, you can decide whether entries that have a commit time equal to the

upper bound of the extraction interval are to be included in the interval. By default, the upper

bound is included.

The result set that is returned by the

wrapper function returns only those tracked

columns that were in the @column_list when the wrapper was generated. If @column_list is

NULL, all tracked source columns are returned. The source columns are followed by an
