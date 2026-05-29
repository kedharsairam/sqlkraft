---
name: "sys.sp_attachsubscription"
title: "sp_attachsubscription"
category: "general"
description: "Attaches an existing subscription database to any Subscriber. This stored procedure is executed Transact-SQL syntax conventions This feature is deprecated and will be removed in a future release. This feature shouldn't be used in new development work. For merge publications that are partitioned using parameterized filters, we recommend using the new features of partitioned snapshots, which simplif"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_attachsubscription
  [ @dbname = ]
  N
  'dbname'
  , [ @filename = ]
  N
  'filename'
  [ , [ @subscriber_security_mode = ] subscriber_security_mode ]
  [ , [ @subscriber_login = ]
  N
  'subscriber_login'
  ]
  [ , [ @subscriber_password = ]
  N
  'subscriber_password'
  ]
  [ , [ @distributor_security_mode = ] distributor_security_mode ]
  [ , [ @distributor_login = ]
  N
  'distributor_login'
  ]
  [ , [ @distributor_password = ]
  N
  'distributor_password'
  ]
  [ , [ @publisher_security_mode = ] publisher_security_mode ]
  [ , [ @publisher_login = ]
  N
  'publisher_login'
  ]
  [ , [ @publisher_password = ]
  N
  'publisher_password'
  ]
  [ , [ @job_login = ]
  N
  'job_login'
  ]
  [ , [ @job_password = ]
  N
  'job_password'
  ]
  [ , [ @db_master_key_password = ]
  N
  'db_master_key_password'
  ]
  [ ; ]
---

## Description

Attaches an existing subscription database to any Subscriber. This stored procedure is executed Transact-SQL syntax conventions This feature is deprecated and will be removed in a future release. This feature shouldn't be used in new development work. For merge publications that are partitioned using parameterized filters, we recommend using the new features of partitioned snapshots, which simplify the initialization of a large number of subscriptions. For more information,

## Syntax

```sql
sp_attachsubscription
[ @dbname = ]
N
'dbname'
, [ @filename = ]
N
'filename'
[ , [ @subscriber_security_mode = ] subscriber_security_mode ]
[ , [ @subscriber_login = ]
N
'subscriber_login'
]
[ , [ @subscriber_password = ]
N
'subscriber_password'
]
[ , [ @distributor_security_mode = ] distributor_security_mode ]
[ , [ @distributor_login = ]
N
'distributor_login'
]
[ , [ @distributor_password = ]
N
'distributor_password'
]
[ , [ @publisher_security_mode = ] publisher_security_mode ]
[ , [ @publisher_login = ]
N
'publisher_login'
]
[ , [ @publisher_password = ]
N
'publisher_password'
]
[ , [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ , [ @db_master_key_password = ]
N
'db_master_key_password'
]
[ ; ]
```

## Arguments

Applies to:

Azure SQL Database

Attaches an existing subscription database to any Subscriber. This stored procedure is executed

at the new Subscriber on the

Transact-SQL syntax conventions

This feature is deprecated and will be removed in a future release. This feature shouldn't

be used in new development work. For merge publications that are partitioned using

parameterized filters, we recommend using the new features of partitioned snapshots,

which simplify the initialization of a large number of subscriptions. For more information,

publications that aren't partitioned, you can initialize a subscription with a backup. For

more information, see
