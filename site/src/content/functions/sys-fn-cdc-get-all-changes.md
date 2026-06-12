---
name: "sys.fn_cdc_get_all_changes_"
title: "cdc.fn_cdc_get_all_changes_<capture_instance>"
category: "change-data-capture"
description: "function serves as a wrapper for the query function. The stored procedure is used to generate the script to create the Wrapper functions are not created automatically. There are two things you must do to create wrapper functions: 1. Run the stored procedure to generate the script to create the wrapper. 2. Execute the script to actually create the wrapper function."
tags: ["change-data-capture","function"]
pubDate: 2026-05-29
syntax: "cdc.fn_cdc_get_all_changes_<capture_instance>"
---

## Description

function serves as a wrapper for the query function. The stored procedure is used to generate the script to create the Wrapper functions are not created automatically. There are two things you must do to create wrapper functions: 1. Run the stored procedure to generate the script to create the wrapper. 2. Execute the script to actually create the wrapper function. Wrapper functions enable users to systematically query for changes that occurred within an interval bounded by values instead of by LSN values. The wrapper functions perform all the required conversions between the provided values and the LSN values needed internally as arguments to the query functions.

## Syntax

```sql
cdc.fn_cdc_get_all_changes_<capture_instance>
```

## Arguments

Before you can enable a table for change data capture, the database must be enabled. To

determine whether the database is enabled for change data capture, query the

column in the

sys.databases

catalog view. To enable the database, use the

sys.sp_cdc_enable_db

stored procedure.

When change data capture is enabled for a table, a change table and one or two query

functions are generated. The change table serves as a repository for the source table changes

extracted from the transaction log by the capture process. The query functions are used to

extract data from the change table. The names of these functions are derived from the

@capture_instance

parameter in the following ways:

All changes function:

Net changes function:

also creates the capture and cleanup jobs for the database if the

source table is the first table in the database to be enabled for change data capture and no

transactional publications exist for the database. It sets the

column in the

catalog view to

Agent doesn't have to be running when CDC is enabled for a table. However, the

capture process doesn't process the transaction log and write entries to the change table

unless SQL Server Agent is running.

Requires membership in the

fixed database role.

The following example enables change data capture for the

Only the required parameters are specified.

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

## Examples

### Example 1

`fn_cdc_get_net_changes`

### Example 2

```sql
cdc.fn_cdc_get_all_changes_<capture_instance>
```

### Example 3

```sql
cdc.fn_cdc_get_net_changes_<capture_instance>
```

### Example 4

`lsn_value`

### Example 5

```sql
Msg 313, Level 16, State 3, Line 1 An insufficient number of arguments were supplied for the procedure or function
```

### Example 6

`cdc.fn_cdc_get_net_changes_HR_Department`

### Example 7

`HumanResources.Department`

### Example 8

`GETDATE`

### Example 9

`GETDATE`

### Example 10

`cdc.fn_cdc_get_net_changes_HR_Department`
