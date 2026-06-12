---
name: "sys.sp_restoremergeidentityrange"
title: "sp_restoremergeidentityrange"
category: "general"
description: "This stored procedure is used to update identity range assignments. It ensures that automatic identity range management functions properly after a Publisher is restored from a backup. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_restoremergeidentityrange
              [ [ @publication = ]
              N
              'publication'
              ]
              [ , [ @article = ]
              N
              'article'
              ]
              [ ; ]
---

## Description

This stored procedure is used to update identity range assignments. It ensures that automatic identity range management functions properly after a Publisher is restored from a backup. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_restoremergeidentityrange
[ [ @publication = ]
N
'publication'
]
[ , [ @article = ]
N
'article'
]
[ ; ]
```

## Permissions

is used with merge replication. gets maximum identity range allocation information from the Distributor, and updates values in the column of MSmerge_identity_range_allocations for the articles that use automatic identity range management. Only members of the fixed server role or fixed database role can execute. sp_addmergearticle (Transact-SQL) sp_changemergearticle (Transact-SQL) Replicate Identity Columns
## Remarks

This stored procedure is used to update identity range assignments. It ensures that automatic

identity range management functions properly after a Publisher is restored from a backup. This

stored procedure is executed at the Publisher on the publication database.

The name of the publication.

@publication

, with a default of. When specified,

only identity ranges for that publication are restored.

The name of the article.

, with a default of. When specified, only

identity ranges for that article are restored.

(success) or
