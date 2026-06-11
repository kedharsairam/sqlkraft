---
name: "sys.sp_dropdynamicsnapshot_job"
title: "sp_dropdynamicsnapshot_job"
category: "general"
description: "Removes a filtered data snapshot job for a publication with parameterized row filters. This stored procedure is executed at the Publisher on the publication database. When the job is deleted, all of the related data is deleted from the Transact-SQL syntax conventions The name of the publication from which the filtered data snapshot job is being removed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropdynamicsnapshot_job
  [ @publication = ]
  N
  'publication'
  [ , [ @dynamic_snapshot_jobname = ]
  N
  'dynamic_snapshot_jobname'
  ]
  [ , [ @dynamic_snapshot_jobid = ]
  'dynamic_snapshot_jobid'
  ]
  [ , [ @ignore_distributor = ] ignore_distributor ]
  [ ; ]
---

## Description

Removes a filtered data snapshot job for a publication with parameterized row filters. This stored procedure is executed at the Publisher on the publication database. When the job is deleted, all of the related data is deleted from the Transact-SQL syntax conventions The name of the publication from which the filtered data snapshot job is being removed. The name of the filtered data snapshot job being removed.

## Syntax

```sql
sp_dropdynamicsnapshot_job
[ @publication = ]
N
'publication'
[ , [ @dynamic_snapshot_jobname = ]
N
'dynamic_snapshot_jobname'
]
[ , [ @dynamic_snapshot_jobid = ]
'dynamic_snapshot_jobid'
]
[ , [ @ignore_distributor = ] ignore_distributor ]
[ ; ]
```
