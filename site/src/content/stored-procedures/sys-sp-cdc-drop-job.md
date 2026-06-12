---
name: "sys.sp_cdc_drop_job"
title: "sys.sp_cdc_drop_job"
category: "general"
description: ""
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_drop_job [ [ @job_type = ]
  N
  'job_type'
  ]
  [ ; ]
---

## Description

Removes a change data capture cleanup or capture job for the current database from ## Syntax

```sql
sys.sp_cdc_drop_job [ [ @job_type = ]
N
'job_type'
]
[ ; ]
```

## Permissions

06/23/2025 syntaxsql Type of job to remove. job_type is and can't be. Valid inputs are and. (success) or (failure). None. is called internally by sys.sp_cdc_disable_db. Requires membership in the fixed database role.

## Examples

### Example 1

`AdventureWorks2022`

### Example 2

```sql
USE
AdventureWorks2022;
GO
EXECUTE sys.sp_cdc_drop_job @job_type = N
'cleanup'
;
```
