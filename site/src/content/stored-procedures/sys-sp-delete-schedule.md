---
name: "sys.sp_delete_schedule"
title: "sp_delete_schedule"
category: "general"
description: "The schedule identification number of the schedule to delete. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_delete_schedule
      [ [ @schedule_id = ] schedule_id ]
      [ , [ @schedule_name = ]
      N
      'schedule_name'
      ]
      [ , [ @force_delete = ] force_delete ]
      [ , [ @automatic_post = ] automatic_post ]
      [ ; ]
---

## Description

## Syntax

```sql
sp_delete_schedule
[ [ @schedule_id = ] schedule_id ]
[ , [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @force_delete = ] force_delete ]
[ , [ @automatic_post = ] automatic_post ]
[ ; ]
```
