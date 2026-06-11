---
name: "sys.sp_fkeys"
title: "sp_fkeys"
category: "general"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns logical foreign key information for the current environment. This procedure shows foreign key relationships including disabled foreign keys. Transact-SQL syntax conventions The name of the table, with the primary key, used to return catalog information. Wildcard pattern matching isn't supported."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_fkeys
  [ [ @pktable_name = ]
  N
  'pktable_name'
  ]
  [ , [ @pktable_owner = ]
  N
  'pktable_owner'
  ]
  [ , [ @pktable_qualifier = ]
  N
  'pktable_qualifier'
  ]
  [ , [ @fktable_name = ]
  N
  'fktable_name'
  ]
  [ , [ @fktable_owner = ]
  N
  'fktable_owner'
  ]
  [ , [ @fktable_qualifier = ]
  N
  'fktable_qualifier'
  ]
  [ ; ]
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns logical foreign key information for the current environment. This procedure shows foreign key relationships including disabled foreign keys. Transact-SQL syntax conventions The name of the table, with the primary key, used to return catalog information. . Wildcard pattern matching isn't supported. parameter, or both, must be supplied.

## Syntax

```sql
sp_fkeys
[ [ @pktable_name = ]
N
'pktable_name'
]
[ , [ @pktable_owner = ]
N
'pktable_owner'
]
[ , [ @pktable_qualifier = ]
N
'pktable_qualifier'
]
[ , [ @fktable_name = ]
N
'fktable_name'
]
[ , [ @fktable_owner = ]
N
'fktable_owner'
]
[ , [ @fktable_qualifier = ]
N
'fktable_qualifier'
]
[ ; ]
```
