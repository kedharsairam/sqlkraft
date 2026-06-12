---
name: "sys.sp_add_category"
title: "sp_add_category"
category: "general"
description: "Adds the specified category of jobs, alerts, or operators to the server. For alternative method, The class of the category to be added."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_category
  [ [ @class = ]
  'class'
  ]
  [ , [ @type = ]
  'type'
  ]
  [ , [ @name = ]
  'name'
  ]
  [ ; ]
---

## Description

Adds the specified category of jobs, alerts, or operators to the server. For alternative method, The class of the category to be added.

## Syntax

```sql
sp_add_category
[ [ @class = ]
'class'
]
[ , [ @type = ]
'type'
]
[ , [ @name = ]
'name'
]
[ ; ]
```

## Examples

### Example 1

`AdminJobs`

### Example 2

```sql
USE msdb;
GO
EXECUTE dbo.sp_add_category
@
class
= N
'JOB'
,
@
type
= N
'LOCAL'
,
@
name
= N
'AdminJobs'
;
GO
```
