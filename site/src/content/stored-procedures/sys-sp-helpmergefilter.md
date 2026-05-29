---
name: "sys.sp_helpmergefilter"
title: "sp_helpmergefilter"
category: "general"
description: "Returns information about merge filters. This stored procedure is executed at the Publisher on Transact-SQL syntax conventions , which returns the names of all The name of the filter about which to return information. , which returns information about all the filters defined on the article or"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergefilter
  [ @publication = ]
  N
  'publication'
  [ , [ @article = ]
  N
  'article'
  ]
  [ , [ @filtername = ]
  N
  'filtername'
  ]
  [ , [ @filter_type_bm = ] filter_type_bm ]
  [ ; ]
---

## Description

Returns information about merge filters. This stored procedure is executed at the Publisher on Transact-SQL syntax conventions , which returns the names of all The name of the filter about which to return information. , which returns information about all the filters defined on the article or

## Syntax

```sql
sp_helpmergefilter
[ @publication = ]
N
'publication'
[ , [ @article = ]
N
'article'
]
[ , [ @filtername = ]
N
'filtername'
]
[ , [ @filter_type_bm = ] filter_type_bm ]
[ ; ]
```
