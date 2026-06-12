---
name: "sys.sp_cdc_cleanup_change_table"
title: "sys.sp_cdc_cleanup_change_table"
category: "general"
description: "performs the following operations: @low_water_mark @capture_instance is left unchanged. However, if the current low watermark is greater than the low watermark value specified using the @low_water_mark parameter for the is thrown. The error message for Error 22957 is 2. Change table entries with values less than the low watermark are then deleted. The delete threshold is used to limit the number o"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sys.sp_cdc_cleanup_change_table [ @capture_instance = ]
      'capture_instance'
      , [ @low_water_mark = ] low_water_mark
      , [ @threshold = ]
      'delete threshold'
      , [ @f
      C
      leanup
      F
      ailed = ]
      'cleanup failed'
      OUTPUT
      [ ; ]
---

## Description

performs the following operations: @low_water_mark @capture_instance is left unchanged. However, if the current low watermark is greater than the low watermark value specified using the @low_water_mark parameter for the is thrown. The error message for Error 22957 is 2. Change table entries with values less than the low watermark are then deleted. The delete threshold is used to limit the number of rows deleted in a single transaction. A failure to successfully delete entries is reported, but doesn't affect any change to the capture instance low watermark that might have been made based on the stored procedure times out after updating the for the capture instance but without deleting the change table data, increasing the data retention value using the stored procedure sys.sp_cdc_change_job next execution of the stored procedure

## Syntax

```sql
sys.sp_cdc_cleanup_change_table [ @capture_instance = ]
'capture_instance'
, [ @low_water_mark = ] low_water_mark
, [ @threshold = ]
'delete threshold'
, [ @f
C leanup
F ailed = ]
'cleanup failed'
OUTPUT
[ ; ]
```

## Permissions

data for the specified retention period. The value in cdc.change*tables should be treated as the new low watermark. The stored procedure doesn't set the value to match the newly specified data retention period. The procedure always performs cleanup based on the low watermark. Specifying a value for the @low_water_mark parameter that is equal to or higher than the value in cdc.change_tables , avoids generating Error 22957. 4. If you use to manage the cleanup table process and a deadlock occurs between the CDC scan and CDC cleanup when is invoked, Error 22852 is logged with severity 10 (informational message). The message for Error 22852 is as follows: Output Use in the following circumstances: The cleanup Agent job reports delete failures. An administrator can run this stored procedure explicitly to retry a failed operation. To retry cleanup for a given capture instance, execute , and specify for the @low_water_mark parameter. The simple retention-based policy used by the cleanup Agent job isn't adequate. Because this stored procedure performs cleanup for a single capture instance, it can be used to build a custom cleanup strategy that tailors the rules for cleanup to the individual capture instance. Requires membership in the fixed database role. cdc.fn_cdc_get_all_changes*<capture_instance> (Transact-SQL) sys.fn_cdc_get_min_lsn (Transact-SQL)
## Remarks

performs the following operations:

@low_water_mark

parameter is

value for the

@capture_instance

is left unchanged. However, if the current low watermark is greater

than the low watermark value specified using the

@low_water_mark

parameter for the

procedure, the

Error 22957

is thrown. The error message for Error 22957 is

2. Change table entries with

values less than the low watermark are then

deleted. The delete threshold is used to limit the number of rows deleted in a single

transaction. A failure to successfully delete entries is reported, but doesn't affect any

change to the capture instance low watermark that might have been made based on the

stored procedure times out after updating the

for the capture instance but without deleting the change table data, increasing

the data retention value using the stored procedure

sys.sp_cdc_change_job

next execution of the stored procedure

doesn't retain

The new low watermark might not be the low watermark that is specified in the

stored procedure call. If other entries in the

table share the

same commit time, the smallest

represented in the group of entries is

selected as the adjusted low watermark. If the

@low_water_mark

parameter is

or the current low watermark is greater than the new low watermark, the

value for the capture instance is left unchanged.
