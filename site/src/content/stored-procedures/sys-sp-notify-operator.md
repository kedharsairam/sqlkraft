---
name: "sys.sp_notify_operator"
title: "sp_notify_operator"
category: "general"
description: "Sends an e-mail message to an operator using Database Mail."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_notify_operator
  [ [ @profile_name = ]
  N
  'profile_name'
  ]
  [ , [ @id = ] id ]
  [ , [ @name = ]
  N
  'name'
  ]
  [ , [ @subject = ]
  N
  'subject'
  ]
  [ , [ @body = ]
  N
  'body'
  ]
  [ , [ @file_attachments = ]
  N
  'file_attachments'
  ]
  [ , [ @mail_database = ]
  N
  'mail_database'
  ]
  [ ; ]
---

## Description

Sends an e-mail message to an operator using Database Mail.

## Syntax

```sql
sp_notify_operator
[ [ @profile_name = ]
N
'profile_name'
]
[ , [ @id = ] id ]
[ , [ @name = ]
N
'name'
]
[ , [ @subject = ]
N
'subject'
]
[ , [ @body = ]
N
'body'
]
[ , [ @file_attachments = ]
N
'file_attachments'
]
[ , [ @mail_database = ]
N
'mail_database'
]
[ ; ]
```
