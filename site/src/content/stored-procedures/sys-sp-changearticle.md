---
name: "sys.sp_changearticle"
title: "sp_changearticle"
category: "general"
description: "Changes the properties of an article in a transactional or snapshot publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication that contains the article. The name of the article whose property is to be changed. An article property to change."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changearticle
  [ [ @publication = ]
  N
  'publication'
  ]
  [ , [ @article = ]
  N
  'article'
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

Changes the properties of an article in a transactional or snapshot publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication that contains the article. The name of the article whose property is to be changed. An article property to change.

## Syntax

```sql
sp_changearticle
[ [ @publication = ]
N
'publication'
]
[ , [ @article = ]
N
'article'
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

Only members of the fixed server role or fixed database role can execute . View and Modify Article Properties Change Publication and Article Properties sp_addarticle (Transact-SQL) sp_articlecolumn (Transact-SQL) sp_droparticle (Transact-SQL) sp_helparticle (Transact-SQL) sp_helparticlecolumns (Transact-SQL) Related content sp_changearticle (Transact-SQL) sp_droparticle (Transact-SQL) sp_helparticle (Transact-SQL) sp_helparticlecolumns (Transact-SQL) Replication stored procedures (Transact-SQL) Publish Data and Database Objects
