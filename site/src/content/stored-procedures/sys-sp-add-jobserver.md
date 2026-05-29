---
name: 'sys.sp_add_jobserver'
title: 'sp_add_jobserver'
category: 'general'
description: 'Targets the specified job at the specified server. Transact-SQL syntax conventions The identification number of the job. must be specified, but both can''t be specified. must be specified, but both can''t be specified. The name of the server at which to target the job. for a local server, or the name of an existing'
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

Targets the specified job at the specified server. Transact-SQL syntax conventions The identification number of the job. must be specified, but both can't be specified. must be specified, but both can't be specified. The name of the server at which to target the job. for a local server, or the name of an existing

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
