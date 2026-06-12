---
name: "sys.sp_addextendedproperty"
title: "sp_addextendedproperty"
category: "general"
description: "Adds a new extended property to a database object."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_addextendedproperty
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

Adds a new extended property to a database object.

## Syntax

```sql
sp_addextendedproperty
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
