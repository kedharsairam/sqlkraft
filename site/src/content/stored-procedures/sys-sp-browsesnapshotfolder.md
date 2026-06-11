---
name: "sys.sp_browsesnapshotfolder"
title: "sp_browsesnapshotfolder"
category: "general"
description: "Returns the complete path for the latest snapshot generated for a publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication that contains the article."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_browsesnapshotfolder
  [ @publication = ]
  N
  'publication'
  [ , [ @subscriber = ]
  N
  'subscriber'
  ]
  [ , [ @subscriber_db = ]
  N
  'subscriber_db'
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Returns the complete path for the latest snapshot generated for a publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication that contains the article. The name of the subscription database. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_browsesnapshotfolder
[ @publication = ]
N
'publication'
[ , [ @subscriber = ]
N
'subscriber'
]
[ , [ @subscriber_db = ]
N
'subscriber_db'
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
