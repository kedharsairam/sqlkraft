---
name: 'sys.sp_refreshsubscriptions'
title: 'sp_refreshsubscriptions'
category: 'general'
description: 'Add subscriptions to new articles for all the existing Subscribers to an immediate-updating publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions Specifies the publication for which to refresh subscriptions. Identified for informational purposes only. Not supported. Future compatibility is not'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_refreshsubscriptions
  [ @publication = ]
  N
  'publication'
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Add subscriptions to new articles for all the existing Subscribers to an immediate-updating publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions Specifies the publication for which to refresh subscriptions. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_refreshsubscriptions
[ @publication = ]
N
'publication'
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

is used in snapshot, transactional, and merge replication. is called by for an immediate-updating publication. Only members of the fixed server role or the fixed database role can execute . sp_addarticle (Transact-SQL) System stored procedures (Transact-SQL) Related content
