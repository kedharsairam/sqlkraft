---
name: "sys.sp_remove_job_from_targets"
title: "sp_remove_job_from_targets"
category: "general"
description: "Removes the specified job from the given target servers or target server groups. The job identification number of the job from which to remove the specified target servers or must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_remove_job_from_targets
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
              [ ; ]
---

## Description

Removes the specified job from the given target servers or target server groups. The job identification number of the job from which to remove the specified target servers or must be specified, but both can't be specified.

## Syntax

```sql
sp_remove_job_from_targets
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
[ ; ]
```
