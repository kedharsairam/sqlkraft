---
name: 'sys.sp_updateextendedproperty'
title: 'sp_updateextendedproperty'
category: 'general'
description: 'SQL database in Microsoft Fabric Updates the value of an existing extended property. Transact-SQL syntax conventions The name of the property to be updated. The value associated with the property. can''t be more than 7,500 bytes. The user or user-defined type.'
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

SQL database in Microsoft Fabric Updates the value of an existing extended property. Transact-SQL syntax conventions The name of the property to be updated. The value associated with the property. can't be more than 7,500 bytes. The user or user-defined type.

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
