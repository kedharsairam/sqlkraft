---
name: "sys.sp_cdc_stop_job"
title: "sys.sp_cdc_stop_job"
category: "general"
description: "Stops a change data capture cleanup or capture job for the current database. Transact-SQL syntax conventions can be used by an administrator to explicitly stop either the capture job"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_stop_job
  [ [ @job_type = ]
  N
  'job_type'
  ]
  [ ; ]
---

## Description

Stops a change data capture cleanup or capture job for the current database. Transact-SQL syntax conventions can be used by an administrator to explicitly stop either the capture job

## Syntax

```sql
sys.sp_cdc_stop_job
[ [ @job_type = ]
N
'job_type'
]
[ ; ]
```

## Permissions

06/23/2025 Applies to: SQL Server Stops a change data capture cleanup or capture job for the current database. Transact-SQL syntax conventions syntaxsql Type of job to add. @job_type is with a default of . Valid inputs are and . (success) or (failure). None. can be used by an administrator to explicitly stop either the capture job or the cleanup job.

## Examples

### Example 1

`AdventureWorks2022`

### Example 2

```sql
USE
AdventureWorks2022;
GO
EXECUTE sys.sp_cdc_stop_job @job_type = N
'capture'
;
GO
```
