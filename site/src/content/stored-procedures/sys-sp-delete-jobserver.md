---
name: "sys.sp_delete_jobserver"
title: "sp_delete_jobserver"
category: "general"
description: "Removes the specified target server. Transact-SQL syntax conventions The identification number of the job from which the specified target server will be removed. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_jobserver
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  , [ @server_name = ]
  N
  'server_name'
  [ ; ]
---

## Description

Removes the specified target server. Transact-SQL syntax conventions The identification number of the job from which the specified target server will be removed. must be specified, but both can't be specified. The name of the job from which the specified target server will be removed. must be specified, but both can't be specified. The name of the target server to remove from the specified job. or the name of a remote target server.

## Syntax

```sql
sp_delete_jobserver
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
, [ @server_name = ]
N
'server_name'
[ ; ]
```
