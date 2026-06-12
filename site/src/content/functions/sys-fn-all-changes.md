---
name: "sys.fn_all_changes_"
title: "sys.fn_all_changes_<capture_instance>"
category: "system"
description: "function serves as a wrapper for the query function. The stored procedure is used to generate the script to create the Wrapper functions are not created automatically. There are two things you must do to create wrapper functions: 1. Run the stored procedure to generate the script to create the wrapper. 2. Execute the script to actually create the wrapper function."
tags: ["system","function"]
pubDate: 2026-05-29
syntax: "sys.sp_cdc_generate_wrapper_function"
---

## Description

function serves as a wrapper for the query function. The stored procedure is used to generate the script to create the Wrapper functions are not created automatically. There are two things you must do to create wrapper functions: 1. Run the stored procedure to generate the script to create the wrapper. 2. Execute the script to actually create the wrapper function. Wrapper functions enable users to systematically query for changes that occurred within an interval bounded by values instead of by LSN values. The wrapper functions perform all the required conversions between the provided values and the LSN values needed internally as arguments to the query functions. When the wrapper functions are used serially to process a stream of change data, they ensure that no data is lost or repeated provided that the scripts for all of the wrapper functions for a schema's defined query functions. The template operation column, \_\_CDC_OPERATION, which is a one- or two-character column that identifies

## Syntax

`sys.sp_cdc_generate_wrapper_function`

## Remarks

function serves as a wrapper for the

query function. The

stored procedure is used to generate the script to create the

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

wrapper function returns the \_\_$start_lsn and

**$seqval columns of the change table as columns **CDC_STARTLSN and \_\_CDC_SEQVAL,

respectively. It follows these with only those tracked columns that appeared in the

@column_list

parameter when the wrapper was generated. If

@column_list

is NULL, all tracked

source columns are returned. The source columns are followed by an operation column,

\_\_CDC_OPERATION, which is a one- or two-character column that identifies the operation.

Bit flags are then appended to the result set for each column that is identified in the

@update_flag_list parameter. For the

wrapper, the bit flags will always be NULL if

**CDC_OPERATION is 'D', 'I', or 'UO'. If **CDC_OPERATION is 'UN', the flag will be set to 1 or 0,

depending on whether the update operation caused a change to the column.

The change data capture configuration template 'Instantiate CDC Wrapper TVFs for Schema'

shows how to use the

stored procedure to obtain CREATE

scripts for all of the wrapper functions for a schema's defined query functions. The template

then creates those scripts. For more information about templates, see

Template Explorer

The wrapper functions

are dependent on the system functions. Error 313 is expected if LSN range supplied is

not appropriate when calling

parameter is beyond the

time of lowest LSN or highest LSN, then execution of these functions will return in error 313:. This error should be handled by the developer.

sys.fn*net_changes*<capture_instance>

sys.sp_cdc_generate_wrapper_function (Transact-SQL)

cdc.fn*cdc_get_all_changes*<capture_instance> (Transact-SQL)

operation column, \_\_CDC_OPERATION, which is a one- or two-character column that identifies

the operation.

Bit flags are then appended to the result set for each column that is identified in the parameter

@update_flag_list. For the

wrapper, the bit flags will always be NULL if the

@row_filter_option that is used in the call to the wrapper function is 'all' or 'all with merge'. If

the @row_filter_option is set to 'all with mask', and \_\_CDC_OPERATION is 'D' or 'I', the value of

the flag will also be NULL. If \_\_CDC_OPERATION is 'UN', the flag will be set to 1 or 0, depending

on whether the

update operation caused a change to the column.

The change data capture configuration template 'Instantiate CDC Wrapper TVFs for Schema'

shows how to use the

stored procedure to obtain CREATE

scripts for all of the wrapper functions for a schema's defined query functions. The template

then creates those scripts. For more information about templates, see

Template Explorer

The wrapper functions

are dependent on the system functions. Error 313 is expected if LSN range supplied is

not appropriate when calling

parameter is beyond the

time of lowest LSN or highest LSN, then execution of these functions will return in error 313:. This error should be handled by the developer.

sys.fn*all_changes*<capture_instance>

sys.sp_cdc_generate_wrapper_function (Transact-SQL)

cdc.fn*cdc_get_net_changes*<capture_instance> (Transact-SQL)
