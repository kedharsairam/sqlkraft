---
name: "sys.sp_configure_automatic_tuning"
title: "sp_configure_automatic_tuning"
category: "general"
description: "2022 (16.x) and later versions SQL database in Microsoft Fabric Changes the configuration for the feature. The configuration options apply to a given These options include the ability to allow a to be allowed or skipped for APC consideration, or to configure APC to apply an additional extended, time-based plan regression check to that specific query. The configuration options are Transa"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_configure_automatic_tuning
  [ @option = ] {
  'FORCE_LAST_GOOD_PLAN'
  |
  'FORCE_LAST_GOOD_PLAN_EXTENDED_CHECK'
  }
  , [ @type = ]
  'type'
  [ , [ @type_value = ]
  N
  'type_value'
  ]
  , [ @option_value = ] {
  'ON'
  |
  'OFF'
  }
---

## Description

2022 (16.x) and later versions SQL database in Microsoft Fabric Changes the configuration for the feature. The configuration options apply to a given These options include the ability to allow a to be allowed or skipped for APC consideration, or to configure APC to apply an additional extended, time-based plan regression check to that specific query. The configuration options are ## Syntax

```sql
sp_configure_automatic_tuning
[ @option = ] {
'FORCE_LAST_GOOD_PLAN'
|
'FORCE_LAST_GOOD_PLAN_EXTENDED_CHECK'
}
, [ @type = ]
'type'
[ , [ @type_value = ]
N
'type_value'
]
, [ @option_value = ] {
'ON'
|
'OFF'
}
```
