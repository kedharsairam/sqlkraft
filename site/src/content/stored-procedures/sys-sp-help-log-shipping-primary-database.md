---
name: "sys.sp_help_log_shipping_primary_database"
title: "sp_help_log_shipping_primary_database"
category: "general"
description: "Retrieves primary database settings."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_log_shipping_primary_database
  [ [ @database = ]
  N
  'database'
  ]
  [ , [ @primary_id = ]
  'primary_id'
  ]
  [ ; ]
---

## Description

Retrieves primary database settings.

## Syntax

```sql
sp_help_log_shipping_primary_database
[ [ @database = ]
N
'database'
]
[ , [ @primary_id = ]
'primary_id'
]
[ ; ]
```
