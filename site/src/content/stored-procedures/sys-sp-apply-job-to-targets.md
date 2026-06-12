---
name: "sys.sp_apply_job_to_targets"
title: "sp_apply_job_to_targets"
category: "general"
description: "Applies a job to one or more target servers or to the target servers belonging to one or more The job identification number of the job to apply to the specified target servers or target server must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_apply_job_to_targets
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @target_server_groups = ]
  N
  'target_server_groups'
  ]
  [ , [ @target_servers = ]
  N
  'target_servers'
  ]
  [ , [ @operation = ]
  'operation'
  ]
  [ ; ]
---

## Description

Applies a job to one or more target servers or to the target servers belonging to one or more The job identification number of the job to apply to the specified target servers or target server must be specified, but both can't be specified.

## Syntax

```sql
sp_apply_job_to_targets
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @target_server_groups = ]
N
'target_server_groups'
]
[ , [ @target_servers = ]
N
'target_servers'
]
[ , [ @operation = ]
'operation'
]
[ ; ]
```
