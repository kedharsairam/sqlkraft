---
name: "sys.sp_changedistpublisher"
title: "sp_changedistpublisher"
category: "general"
description: "Changes the properties of the distribution Publisher. This stored procedure is executed at the Transact-SQL syntax conventions A property to change for the given Publisher. properties in the table listed under The value for the given property."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changedistpublisher
  [ @publisher = ]
  N
  'publisher'
  [ , [ @property = ]
  N
  'property'
  ]
  [ , [ @value = ]
  N
  'value'
  ]
  [ ; ]
---

## Description

Changes the properties of the distribution Publisher. This stored procedure is executed at the Transact-SQL syntax conventions A property to change for the given Publisher. properties in the table listed under The value for the given property. , and can be one of the values in the

## Syntax

```sql
sp_changedistpublisher
[ @publisher = ]
N
'publisher'
[ , [ @property = ]
N
'property'
]
[ , [ @value = ]
N
'value'
]
[ ; ]
```
