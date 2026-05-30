---
name: "sys.sp_update_job"
title: "sp_update_job"
category: "general"
description: "Updates the attributes of an existing job created in the SQL Server Agent service. Transact-SQL syntax conventions The identification number of the job to be updated. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_update_job
  [ [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @new_name = ]
  N
  'new_name'
  ]
  [ , [ @enabled = ] enabled ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @start_step_id = ] start_step_id ]
  [ , [ @category_name = ]
  N
  'category_name'
  ]
  [ , [ @owner_login_name = ]
  N
  'owner_login_name'
  ]
  [ , [ @notify_level_eventlog = ] notify_level_eventlog ]
  [ , [ @notify_level_email = ] notify_level_email ]
  [ , [ @notify_level_netsend = ] notify_level_netsend ]
  [ , [ @notify_level_page = ] notify_level_page ]
  [ , [ @notify_email_operator_name = ]
  N
  'notify_email_operator_name'
  ]
  [ , [ @notify_netsend_operator_name = ]
  N
  'notify_netsend_operator_name'
  ]
  [ , [ @notify_page_operator_name = ]
  N
  'notify_page_operator_name'
  ]
  [ , [ @delete_level = ] delete_level ]
  [ , [ @automatic_post = ] automatic_post ]
  [ ; ]
---

## Description

Updates the attributes of an existing job created in the SQL Server Agent service. Transact-SQL syntax conventions The identification number of the job to be updated. must be specified, but both can't be specified.

## Syntax

```sql
sp_update_job
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @new_name = ]
N
'new_name'
]
[ , [ @enabled = ] enabled ]
[ , [ @description = ]
N
'description'
]
[ , [ @start_step_id = ] start_step_id ]
[ , [ @category_name = ]
N
'category_name'
]
[ , [ @owner_login_name = ]
N
'owner_login_name'
]
[ , [ @notify_level_eventlog = ] notify_level_eventlog ]
[ , [ @notify_level_email = ] notify_level_email ]
[ , [ @notify_level_netsend = ] notify_level_netsend ]
[ , [ @notify_level_page = ] notify_level_page ]
[ , [ @notify_email_operator_name = ]
N
'notify_email_operator_name'
]
[ , [ @notify_netsend_operator_name = ]
N
'notify_netsend_operator_name'
]
[ , [ @notify_page_operator_name = ]
N
'notify_page_operator_name'
]
[ , [ @delete_level = ] delete_level ]
[ , [ @automatic_post = ] automatic_post ]
[ ; ]
```

## Examples

### Example 1

```sql
NightlyBackups
```

### Example 2

```sql
USE
msdb;
GO
EXECUTE
dbo.sp_update_job
@job_name = N
'NightlyBackups'
,
@new_name = N
'NightlyBackups -- Disabled'
,
@description = N
'Nightly backups disabled during server migration.'
,
@enabled = 0;
GO
```
