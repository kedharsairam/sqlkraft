---
name: "sys.sp_help_alert"
title: "sp_help_alert"
category: "general"
description: "Reports information about the alerts defined for the server. information about all alerts is returned. The sorting order to use for producing the results. The identification number of the alert to report information about."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_alert
  [ [ @alert_name = ]
  N
  'alert_name'
  ]
  [ , [ @order_by = ]
  N
  'order_by'
  ]
  [ , [ @alert_id = ] alert_id ]
  [ , [ @category_name = ]
  N
  'category_name'
  ]
  [ , [ @legacy_format = ] legacy_format ]
  [ ; ]
---

## Description

Reports information about the alerts defined for the server. information about all alerts is returned. The sorting order to use for producing the results. The identification number of the alert to report information about.

## Syntax

```sql
sp_help_alert
[ [ @alert_name = ]
N
'alert_name'
]
[ , [ @order_by = ]
N
'order_by'
]
[ , [ @alert_id = ] alert_id ]
[ , [ @category_name = ]
N
'category_name'
]
[ , [ @legacy_format = ] legacy_format ]
[ ; ]
```
