---
name: "sys.sp_help_jobactivity"
title: "sp_help_jobactivity"
category: "general"
description: "Lists information about the runtime state of SQL Server Agent jobs. The job identification number. must be specified, but both can't be specified. must be specified, but both can't be specified. The session ID to report information about."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_jobactivity
              [ [ @job_id = ]
              'job_id'
              ]
              [ , [ @job_name = ]
              N
              'job_name'
              ]
              [ , [ @session_id = ] session_id ]
              [ ; ]
---

## Description

Lists information about the runtime state of SQL Server Agent jobs. The job identification number. must be specified, but both can't be specified. must be specified, but both can't be specified. The session ID to report information about.

## Syntax

```sql
sp_help_jobactivity
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @session_id = ] session_id ]
[ ; ]
```
