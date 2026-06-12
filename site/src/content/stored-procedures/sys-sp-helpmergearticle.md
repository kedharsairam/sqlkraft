---
name: "sys.sp_helpmergearticle"
title: "sp_helpmergearticle"
category: "general"
description: "Returns information about an article. This stored procedure is executed at the Publisher on the publication database or at a republishing Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergearticle
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

Returns information about an article. This stored procedure is executed at the Publisher on the publication database or at a republishing Subscriber on the subscription database.

## Syntax

```sql
sp_helpmergearticle
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
