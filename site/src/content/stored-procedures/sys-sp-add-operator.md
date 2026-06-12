---
name: "sys.sp_add_operator"
title: "sp_add_operator"
category: "general"
description: "Creates an operator (notification recipient) for use with alerts and jobs."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  dbo.sp_add_operator
      [ @name = ]
      N
      'name'
      [ , [ @enabled = ] enabled ]
      [ , [ @email_address = ]
      N
      'email_address'
      ]
      [ , [ @pager_address = ]
      N
      'pager_address'
      ]
      [ , [ @weekday_pager_start_time = ] weekday_pager_start_time ]
      [ , [ @weekday_pager_end_time = ] weekday_pager_end_time ]
      [ , [ @saturday_pager_start_time = ] saturday_pager_start_time ]
      [ , [ @saturday_pager_end_time = ] saturday_pager_end_time ]
      [ , [ @sunday_pager_start_time = ] sunday_pager_start_time ]
      [ , [ @sunday_pager_end_time = ] sunday_pager_end_time ]
      [ , [ @pager_days = ] pager_days ]
      [ , [ @netsend_address = ]
      N
      'netsend_address'
      ]
      [ , [ @category_name = ]
      N
      'category_name'
      ]
      [ ; ]
---

## Description

Creates an operator (notification recipient) for use with alerts and jobs.

## Syntax

```sql
dbo.sp_add_operator
[ @name = ]
N
'name'
[ , [ @enabled = ] enabled ]
[ , [ @email_address = ]
N
'email_address'
]
[ , [ @pager_address = ]
N
'pager_address'
]
[ , [ @weekday_pager_start_time = ] weekday_pager_start_time ]
[ , [ @weekday_pager_end_time = ] weekday_pager_end_time ]
[ , [ @saturday_pager_start_time = ] saturday_pager_start_time ]
[ , [ @saturday_pager_end_time = ] saturday_pager_end_time ]
[ , [ @sunday_pager_start_time = ] sunday_pager_start_time ]
[ , [ @sunday_pager_end_time = ] sunday_pager_end_time ]
[ , [ @pager_days = ] pager_days ]
[ , [ @netsend_address = ]
N
'netsend_address'
]
[ , [ @category_name = ]
N
'category_name'
]
[ ; ]
```
