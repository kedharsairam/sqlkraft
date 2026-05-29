---
name: "sys.sp_addextendedproperty"
title: "sp_addextendedproperty"
category: "general"
description: "SQL database in Microsoft Fabric Adds a new extended property to a database object. Transact-SQL syntax conventions The name of the property to be added. , with no default, and can't be Names can include blank or non-alphanumeric character strings, and binary values. The value to be associated with the property. can't be more than 7,500 bytes."
tags: ["stored-procedure"]
pubDate: 2026-05-29
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

SQL database in Microsoft Fabric Adds a new extended property to a database object. Transact-SQL syntax conventions The name of the property to be added. , with no default, and can't be Names can include blank or non-alphanumeric character strings, and binary values. The value to be associated with the property. can't be more than 7,500 bytes.

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
