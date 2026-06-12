---
name: "sys.sp_help_category"
title: "sp_help_category"
category: "general"
description: "Provides information about the specified classes of jobs, alerts, or operators. Specifies the class about which information is requested. Provides information about a job category. Provides information about an alert category. Provides information about an operator category. The type of category for which information is requested."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_category
  [ [ @class = ]
  'class'
  ]
  [ , [ @type = ]
  'type'
  ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ , [ @suffix = ] suffix ]
  [ ; ]
---

## Description

Provides information about the specified classes of jobs, alerts, or operators. Specifies the class about which information is requested. Provides information about a job category. Provides information about an alert category. Provides information about an operator category. The type of category for which information is requested.

## Syntax

```sql
sp_help_category
[ [ @class = ]
'class'
]
[ , [ @type = ]
'type'
]
[ , [ @name = ]
N
'name'
]
[ , [ @suffix = ] suffix ]
[ ; ]
```
