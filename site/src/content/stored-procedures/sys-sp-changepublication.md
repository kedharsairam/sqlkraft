---
name: "sys.sp_changepublication"
title: "sp_changepublication"
category: "general"
description: "Changes the properties of a publication. This stored procedure is executed at the Publisher on The publication property to change. This table describes the properties of the publication that can be changed and restrictions on the values for those properties."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changepublication
  [ [ @publication = ]
  N
  'publication'
  ]
  [ , [ @property = ]
  N
  'property'
  ]
  [ , [ @value = ]
  N
  'value'
  ]
  [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
  [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Changes the properties of a publication. This stored procedure is executed at the Publisher on The publication property to change. This table describes the properties of the publication that can be changed and restrictions on the values for those properties.

## Syntax

```sql
sp_changepublication
[ [ @publication = ]
N
'publication'
]
[ , [ @property = ]
N
'property'
]
[ , [ @value = ]
N
'value'
]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

SQL Only members of the fixed server role or fixed database role can execute. View and Modify Publication Properties Change Publication and Article Properties sp_addpublication (Transact-SQL) sp_droppublication (Transact-SQL) sp_helppublication (Transact-SQL) Replication stored procedures (Transact-SQL)
