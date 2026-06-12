---
name: "sys.sp_updateextendedproperty"
title: "sp_updateextendedproperty"
category: "general"
description: "Updates the value of an existing extended property."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_updateextendedproperty
  [ @name = ]
  N
  'name'
  [ , [ @value = ] value ]
  [ , [ @level0type = ]
  'level0type'
  ]
  [ , [ @level0name = ]
  N
  'level0name'
  ]
  [ , [ @level1type = ]
  'level1type'
  ]
  [ , [ @level1name = ]
  N
  'level1name'
  ]
  [ , [ @level2type = ]
  'level2type'
  ]
  [ , [ @level2name = ]
  N
  'level2name'
  ]
  [ ; ]
---

## Description

Updates the value of an existing extended property.

## Syntax

```sql
sp_updateextendedproperty
[ @name = ]
N
'name'
[ , [ @value = ] value ]
[ , [ @level0type = ]
'level0type'
]
[ , [ @level0name = ]
N
'level0name'
]
[ , [ @level1type = ]
'level1type'
]
[ , [ @level1name = ]
N
'level1name'
]
[ , [ @level2type = ]
'level2type'
]
[ , [ @level2name = ]
N
'level2name'
]
[ ; ]
```
