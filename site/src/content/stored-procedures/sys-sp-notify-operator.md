---
name: "sys.sp_notify_operator"
title: "sp_notify_operator"
category: "general"
description: "Sends an e-mail message to an operator using Database Mail. Transact-SQL syntax conventions The name of the Database Mail profile to use to send the message. isn't specified, the default Database Mail profile is The identifier for the operator to send the message to."
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

Sends an e-mail message to an operator using Database Mail. Transact-SQL syntax conventions The name of the Database Mail profile to use to send the message. isn't specified, the default Database Mail profile is The identifier for the operator to send the message to. The name of the operator to send the message to.

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
