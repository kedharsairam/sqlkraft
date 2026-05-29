---
name: 'sys.sp_copysubscription'
title: 'sp_copysubscription'
category: 'general'
description: 'Copies a subscription database that''s pull subscriptions, but no push subscriptions. Only single file databases can be copied. This stored procedure is executed at the Subscriber on the Transact-SQL syntax conventions The string that specifies the complete path, including file name, to which a copy of the data file This feature will be removed in a future version of SQL Server. Avoid using this fe'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_copysubscription
  [ @filename = ]
  N
  'filename'
  [ , [ @temp_dir = ]
  N
  'temp_dir'
  ]
  [ , [ @overwrite_existing_file = ] overwrite_existing_file ]
  [ ; ]
---

## Description

Copies a subscription database that's pull subscriptions, but no push subscriptions. Only single file databases can be copied. This stored procedure is executed at the Subscriber on the Transact-SQL syntax conventions The string that specifies the complete path, including file name, to which a copy of the data file This feature will be removed in a future version of SQL Server. Avoid using this feature in

## Syntax

```sql
sp_copysubscription
[ @filename = ]
N
'filename'
[ , [ @temp_dir = ]
N
'temp_dir'
]
[ , [ @overwrite_existing_file = ] overwrite_existing_file ]
[ ; ]
```
