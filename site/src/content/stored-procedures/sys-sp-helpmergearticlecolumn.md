---
name: "sys.sp_helpmergearticlecolumn"
title: "sp_helpmergearticlecolumn"
category: "general"
description: "Returns the list of columns in the specified table or view article for a merge publication. Because stored procedures don't have columns, this stored procedure returns an error if a stored procedure is specified as the article. This stored procedure is executed at the Publisher Transact-SQL syntax conventions The name of a table or view that is the article to retrieve information on."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergearticlecolumn
  [ @publication = ]
  N
  'publication'
  , [ @article = ]
  N
  'article'
  [ ; ]
---

## Description

Returns the list of columns in the specified table or view article for a merge publication. Because stored procedures don't have columns, this stored procedure returns an error if a stored procedure is specified as the article. This stored procedure is executed at the Publisher Transact-SQL syntax conventions The name of a table or view that is the article to retrieve information on.

## Syntax

```sql
sp_helpmergearticlecolumn
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ ; ]
```
