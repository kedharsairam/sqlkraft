---
name: "sys.sp_add_job"
title: "sp_add_job"
category: "general"
description: "Creates a new job executed by the SQL Server Agent service."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_job
  [ @job_name = ]
  N
  'job_name'
  [ , [ @enabled = ] enabled ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @start_step_id = ] step_id ]
  [ , [ @category_name = ]
  'category'
  ]
  [ , [ @category_id = ] category_id ]
  [ , [ @owner_login_name = ]
  'login'
  ]
  [ , [ @notify_level_eventlog = ] eventlog_level ]
  [ , [ @notify_level_email = ] email_level ]
  [ , [ @notify_level_netsend = ] netsend_level ]
  [ , [ @notify_level_page = ] page_level ]
  [ , [ @notify_email_operator_name = ]
  'email_name'
  ]
  [ , [ @notify_netsend_operator_name = ]
  'netsend_name'
  ]
  [ , [ @notify_page_operator_name = ]
  'page_name'
  ]
  [ , [ @delete_level = ] delete_level ]
  [ , [ @job_id = ] job_id
  OUTPUT
  ]
  [ ; ]
---

## Description

Creates a new job executed by the SQL Server Agent service. Transact-SQL syntax conventions , most, but not all SQL Server Agent features are

## Syntax

```sql
sp_add_job
[ @job_name = ]
N
'job_name'
[ , [ @enabled = ] enabled ]
[ , [ @description = ]
N
'description'
]
[ , [ @start_step_id = ] step_id ]
[ , [ @category_name = ]
'category'
]
[ , [ @category_id = ] category_id ]
[ , [ @owner_login_name = ]
'login'
]
[ , [ @notify_level_eventlog = ] eventlog_level ]
[ , [ @notify_level_email = ] email_level ]
[ , [ @notify_level_netsend = ] netsend_level ]
[ , [ @notify_level_page = ] page_level ]
[ , [ @notify_email_operator_name = ]
'email_name'
]
[ , [ @notify_netsend_operator_name = ]
'netsend_name'
]
[ , [ @notify_page_operator_name = ]
'page_name'
]
[ , [ @delete_level = ] delete_level ]
[ , [ @job_id = ] job_id
OUTPUT
]
[ ; ]
```
