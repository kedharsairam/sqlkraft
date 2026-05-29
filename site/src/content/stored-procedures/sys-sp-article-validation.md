---
name: "sys.sp_article_validation"
title: "sp_article_validation"
category: "general"
description: "Initiates a data validation request for the specified article. This stored procedure is executed at the Publisher on the publication database and at the Subscriber on the subscription database. Transact-SQL syntax conventions The name of the publication in which the article exists. The name of the article to validate. Specifies if only the rowcount for the table is returned. , perform a rowcount a"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_article_validation
  [ @publication = ]
  N
  'publication'
  , [ @article = ]
  N
  'article'
  [ , [ @rowcount_only = ] rowcount_only ]
  [ , [ @full_or_fast = ] full_or_fast ]
  [ , [ @shutdown_agent = ] shutdown_agent ]
  [ , [ @subscription_level = ] subscription_level ]
  [ , [ @reserved = ] reserved ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Initiates a data validation request for the specified article. This stored procedure is executed at the Publisher on the publication database and at the Subscriber on the subscription database. Transact-SQL syntax conventions The name of the publication in which the article exists. The name of the article to validate. Specifies if only the rowcount for the table is returned. , perform a rowcount and a SQL Server 7.0 compatible checksum.

## Syntax

```sql
sp_article_validation
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @rowcount_only = ] rowcount_only ]
[ , [ @full_or_fast = ] full_or_fast ]
[ , [ @shutdown_agent = ] shutdown_agent ]
[ , [ @subscription_level = ] subscription_level ]
[ , [ @reserved = ] reserved ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
