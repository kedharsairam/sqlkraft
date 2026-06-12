---
name: "sys.sp_helparticlecolumns"
title: "sp_helparticlecolumns"
category: "general"
description: "Returns all columns in the underlying table. This stored procedure is executed at the Publisher on the publication database. For Oracle Publishers, this stored procedure is executed at the The name of the publication that contains the article."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helparticlecolumns
              [ @publication = ]
              N
              'publication'
              , [ @article = ]
              N
              'article'
              [ , [ @publisher = ]
              N
              'publisher'
              ]
              [ ; ]
---

## Description

Returns all columns in the underlying table. This stored procedure is executed at the Publisher on the publication database. For Oracle Publishers, this stored procedure is executed at the The name of the publication that contains the article.

## Syntax

```sql
sp_helparticlecolumns
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
