---
name: "sys.sp_help_jobserver"
title: "sp_help_jobserver"
category: "general"
description: "Returns information about the server for a given job. The job identification number for which to return information. must be specified, but both can't be specified. The job name for which to return information. must be specified, but both can't be specified. Whether the last-run execution information is part of the result set. doesn't include last-run information. i"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_jobserver
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @show_last_run_details = ] show_last_run_details ]
  [ ; ]
---

## Description

Returns information about the server for a given job. The job identification number for which to return information. must be specified, but both can't be specified. The job name for which to return information. must be specified, but both can't be specified. Whether the last-run execution information is part of the result set. doesn't include last-run information. includes last-run information.

## Syntax

```sql
sp_help_jobserver
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @show_last_run_details = ] show_last_run_details ]
[ ; ]
```
