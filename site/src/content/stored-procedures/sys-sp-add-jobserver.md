---
name: "sys.sp_add_jobserver"
title: "sp_add_jobserver"
category: "general"
description: "Targets the specified job at the specified server. The identification number of the job. must be specified, but both can't be specified. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_jobserver
              [ @job_id = ] job_id
              | [ @job_name = ]
              'job_name'
              [ , [ @server_name = ]
              'server'
              ]
              [ ; ]
---

## Description

Targets the specified job at the specified server. The identification number of the job. must be specified, but both can't be specified. must be specified, but both can't be specified.

## Syntax

```sql
sp_add_jobserver
[ @job_id = ] job_id
| [ @job_name = ]
'job_name'
[ , [ @server_name = ]
'server'
]
[ ; ]
```
