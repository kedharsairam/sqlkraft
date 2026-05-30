---
name: "sys.sp_showpendingchanges"
title: "sp_showpendingchanges"
category: "general"
description: "Returns a result set showing the changes that are waiting to be replicated. This stored procedure is executed at the Publisher on the publication database and at the Subscriber on Transact-SQL syntax conventions The name of the server where the replicated changes are applied. This procedure provides an approximation of the number of changes and the rows that are involved in those changes. For exam"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_showpendingchanges
  [ [ @destination_server = ]
  N
  'destination_server'
  ]
  [ , [ @publication = ]
  N
  'publication'
  ]
  [ , [ @article = ]
  N
  'article'
  ]
  [ , [ @show_rows = ] show_rows ]
  [ ; ]
---

## Description

Returns a result set showing the changes that are waiting to be replicated. This stored procedure is executed at the Publisher on the publication database and at the Subscriber on Transact-SQL syntax conventions The name of the server where the replicated changes are applied. This procedure provides an approximation of the number of changes and the rows that are involved in those changes. For example, the procedure retrieves information from

## Syntax

```sql
sp_showpendingchanges
[ [ @destination_server = ]
N
'destination_server'
]
[ , [ @publication = ]
N
'publication'
]
[ , [ @article = ]
N
'article'
]
[ , [ @show_rows = ] show_rows ]
[ ; ]
```
