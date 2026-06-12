---
name: "sys.sp_cdc_start_job"
title: "sys.sp_cdc_start_job"
category: "general"
description: "Starts a change data capture cleanup or capture job for the current database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_start_job
              [ [ @job_type = ]
              N
              'job_type'
              ]
              [ ; ]
---

## Description

Starts a change data capture cleanup or capture job for the current database.

## Syntax

```sql
sys.sp_cdc_start_job
[ [ @job_type = ]
N
'job_type'
]
[ ; ]
```

## Permissions

06/23/2025 syntaxsql Type of job to add. @job_type is with a default of. Valid inputs are and. (success) or (failure). None. can be used by an administrator to explicitly start either the capture job or the cleanup job.
