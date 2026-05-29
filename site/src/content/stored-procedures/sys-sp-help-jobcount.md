---
name: 'sys.sp_help_jobcount'
title: 'sp_help_jobcount'
category: 'general'
description: 'Provides the number of jobs that a schedule is attached to. Transact-SQL syntax conventions The identifier of the schedule to list. The name of the schedule to list. Returns the following result set:'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_jobcount
  [ [ @schedule_name = ]
  N
  'schedule_name'
  ]
  [ , [ @schedule_id = ] schedule_id ]
  [ ; ]
---

## Description

Provides the number of jobs that a schedule is attached to. Transact-SQL syntax conventions The identifier of the schedule to list. The name of the schedule to list. Returns the following result set:

## Syntax

```sql
sp_help_jobcount
[ [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @schedule_id = ] schedule_id ]
[ ; ]
```
