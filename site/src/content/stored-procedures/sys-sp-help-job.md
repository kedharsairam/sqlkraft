---
name: "sys.sp_help_job"
title: "sp_help_job"
category: "general"
description: "Returns information about jobs that are used by SQL Server Agent to perform automated Transact-SQL syntax conventions The job identification number. To view a specific job, either to return information about all jobs."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_job
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @job_aspect = ]
  'job_aspect'
  ]
  [ , [ @job_type = ]
  'job_type'
  ]
  [ , [ @owner_login_name = ]
  N
  'owner_login_name'
  ]
  [ , [ @subsystem = ]
  N
  'subsystem'
  ]
  [ , [ @category_name = ]
  N
  'category_name'
  ]
  [ , [ @enabled = ] enabled ]
  [ , [ @execution_status = ] execution_status ]
  [ , [ @date_comparator = ]
  'date_comparator'
  ]
  [ , [ @date_created = ] date_created ]
  [ , [ @date_last_modified = ] date_last_modified ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ ; ]
---

## Description

Returns information about jobs that are used by SQL Server Agent to perform automated Transact-SQL syntax conventions The job identification number. To view a specific job, either to return information about all jobs.

## Syntax

```sql
sp_help_job
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @job_aspect = ]
'job_aspect'
]
[ , [ @job_type = ]
'job_type'
]
[ , [ @owner_login_name = ]
N
'owner_login_name'
]
[ , [ @subsystem = ]
N
'subsystem'
]
[ , [ @category_name = ]
N
'category_name'
]
[ , [ @enabled = ] enabled ]
[ , [ @execution_status = ] execution_status ]
[ , [ @date_comparator = ]
'date_comparator'
]
[ , [ @date_created = ] date_created ]
[ , [ @date_last_modified = ] date_last_modified ]
[ , [ @description = ]
N
'description'
]
[ ; ]
```
