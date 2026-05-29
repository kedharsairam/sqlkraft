---
name: 'sys.sp_copysnapshot'
title: 'sp_copysnapshot'
category: 'general'
description: 'Copies the snapshot folder of the specified publication to the folder listed in the . This stored procedure is executed at the Publisher on the publication database. This stored procedure is useful for copying a snapshot to removable media. Transact-SQL syntax conventions The name of the publication whose snapshot contents are to be copied. The name of the folder where the contents of the publicat'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_copysnapshot
  [ @publication = ]
  N
  'publication'
  , [ @destination_folder = ]
  N
  'destination_folder'
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

Copies the snapshot folder of the specified publication to the folder listed in the . This stored procedure is executed at the Publisher on the publication database. This stored procedure is useful for copying a snapshot to removable media. Transact-SQL syntax conventions The name of the publication whose snapshot contents are to be copied. The name of the folder where the contents of the publication snapshot are to be copied.

## Syntax

```sql
sp_copysnapshot
[ @publication = ]
N
'publication'
, [ @destination_folder = ]
N
'destination_folder'
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
