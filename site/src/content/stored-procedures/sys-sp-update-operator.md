---
name: "sys.sp_update_operator"
title: "sp_update_operator"
category: "general"
description: "Updates information about an operator (notification recipient) for use with alerts and jobs."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_update_operator
      [ @name = ]
      N
      'name'
      [ , [ @new_name = ]
      N
      'new_name'
      ]
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

Updates information about an operator (notification recipient) for use with alerts and jobs.

## Syntax

```sql
sp_update_operator
[ @name = ]
N
'name'
[ , [ @new_name = ]
N
'new_name'
]
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
