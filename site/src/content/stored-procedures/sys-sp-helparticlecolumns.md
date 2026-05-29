---
name: 'sys.sp_helparticlecolumns'
title: 'sp_helparticlecolumns'
category: 'general'
description: 'Returns all columns in the underlying table. This stored procedure is executed at the Publisher on the publication database. For Oracle Publishers, this stored procedure is executed at the Transact-SQL syntax conventions The name of the publication that contains the article. The name of the article that has its columns returned. Specifies a non-SQL Server Publisher. shouldn''t be specified when the'
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

Returns all columns in the underlying table. This stored procedure is executed at the Publisher on the publication database. For Oracle Publishers, this stored procedure is executed at the Transact-SQL syntax conventions The name of the publication that contains the article. The name of the article that has its columns returned. Specifies a non-SQL Server Publisher. shouldn't be specified when the requested article is published by a SQL Server

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
