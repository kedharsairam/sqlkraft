---
name: "sys.sp_changedistributiondb"
title: "sp_changedistributiondb"
category: "general"
description: "Changes the properties of the distribution database. This stored procedure is executed at the The name of the distribution database. The property to change for the given database. History table retention period. Maximum distribution retention period. Minimum distribution retention period."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changedistributiondb
  [ @database = ]
  N
  'database'
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

Changes the properties of the distribution database. This stored procedure is executed at the The name of the distribution database. The property to change for the given database. History table retention period. Maximum distribution retention period. Minimum distribution retention period.

## Syntax

```sql
sp_changedistributiondb
[ @database = ]
N
'database'
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
