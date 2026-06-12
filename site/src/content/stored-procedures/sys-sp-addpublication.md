---
name: "sys.sp_addpublication"
title: "sp_addpublication"
category: "general"
description: "Creates a snapshot or transactional publication. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addpublication
  [ @publication = ]
  N
  'publication'
  [ , [ @taskid = ] taskid ]
  [ , [ @restricted = ]
  N
  'restricted'
  ]
  [ , [ @sync_method = ]
  N
  'sync_method'
  ]
  [ , [ @repl_freq = ]
  N
  'repl_freq'
  ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @status = ]
  N
  'status'
  ]
  [ , [ @independent_agent = ]
  N
  'independent_agent'
  ]
  [ , [ @immediate_sync = ]
  N
  'immediate_sync'
  ]
  [ , [ @enabled_for_internet = ]
  N
  'enabled_for_internet'
  ]
  [ , [ @allow_push = ]
  N
  'allow_push'
  ]
  [ , [ @allow_pull = ]
  N
  'allow_pull'
  ]
  [ , [ @allow_anonymous = ]
  N
  'allow_anonymous'
  ]
  [ , [ @allow_sync_tran = ]
  N
  'allow_sync_tran'
  ]
  [ , [ @autogen_sync_procs = ]
  N
  'autogen_sync_procs'
  ]
  [ , [ @retention = ] retention ]
  [ , [ @allow_queued_tran = ]
  N
  'allow_queued_tran'
  ]
  [ , [ @snapshot_in_defaultfolder = ]
  N
  'snapshot_in_defaultfolder'
  ]
  [ , [ @alt_snapshot_folder = ]
  N
  'alt_snapshot_folder'
  ]
  [ , [ @pre_snapshot_script = ]
  N
  'pre_snapshot_script'
  ]
  [ , [ @post_snapshot_script = ]
  N
  'post_snapshot_script'
  ]
  [ , [ @compress_snapshot = ]
  N
  'compress_snapshot'
  ]
  [ , [ @ftp_address = ]
  N
  'ftp_address'
  ]
  [ , [ @ftp_port = ] ftp_port ]
  [ , [ @ftp_subdirectory = ]
  N
  'ftp_subdirectory'
  ]
  [ , [ @ftp_login = ]
  N
  'ftp_login'
  ]
  [ , [ @ftp_password = ]
  N
  'ftp_password'
  ]
  [ , [ @allow_dts = ]
  N
  'allow_dts'
  ]
  [ , [ @allow_subscription_copy = ]
  N
  'allow_subscription_copy'
  ]
  [ , [ @conflict_policy = ]
  N
  'conflict_policy'
  ]
  [ , [ @centralized_conflicts = ]
  N
  'centralized_conflicts'
  ]
  [ , [ @conflict_retention = ] conflict_retention ]
  [ , [ @queue_type = ]
  N
  'queue_type'
  ]
  [ , [ @add_to_active_directory = ]
  N
  'add_to_active_directory'
  ]
  [ , [ @logreader_job_name = ]
  N
  'logreader_job_name'
  ]
---

## Description

Creates a snapshot or transactional publication. This stored procedure is executed at the Publisher on the publication database. ## Syntax

```sql
sp_addpublication
[ @publication = ]
N
'publication'
[ , [ @taskid = ] taskid ]
[ , [ @restricted = ]
N
'restricted'
]
[ , [ @sync_method = ]
N
'sync_method'
]
[ , [ @repl_freq = ]
N
'repl_freq'
]
[ , [ @description = ]
N
'description'
]
[ , [ @status = ]
N
'status'
]
[ , [ @independent_agent = ]
N
'independent_agent'
]
[ , [ @immediate_sync = ]
N
'immediate_sync'
]
[ , [ @enabled_for_internet = ]
N
'enabled_for_internet'
]
[ , [ @allow_push = ]
N
'allow_push'
]
[ , [ @allow_pull = ]
N
'allow_pull'
]
[ , [ @allow_anonymous = ]
N
'allow_anonymous'
]
[ , [ @allow_sync_tran = ]
N
'allow_sync_tran'
]
[ , [ @autogen_sync_procs = ]
N
'autogen_sync_procs'
]
[ , [ @retention = ] retention ]
[ , [ @allow_queued_tran = ]
N
'allow_queued_tran'
]
[ , [ @snapshot_in_defaultfolder = ]
N
'snapshot_in_defaultfolder'
]
[ , [ @alt_snapshot_folder = ]
N
'alt_snapshot_folder'
]
[ , [ @pre_snapshot_script = ]
N
'pre_snapshot_script'
]
[ , [ @post_snapshot_script = ]
N
'post_snapshot_script'
]
[ , [ @compress_snapshot = ]
N
'compress_snapshot'
]
[ , [ @ftp_address = ]
N
'ftp_address'
]
[ , [ @ftp_port = ] ftp_port ]
[ , [ @ftp_subdirectory = ]
N
'ftp_subdirectory'
]
[ , [ @ftp_login = ]
N
'ftp_login'
]
[ , [ @ftp_password = ]
N
'ftp_password'
]
[ , [ @allow_dts = ]
N
'allow_dts'
]
[ , [ @allow_subscription_copy = ]
N
'allow_subscription_copy'
]
[ , [ @conflict_policy = ]
N
'conflict_policy'
]
[ , [ @centralized_conflicts = ]
N
'centralized_conflicts'
]
[ , [ @conflict_retention = ] conflict_retention ]
[ , [ @queue_type = ]
N
'queue_type'
]
[ , [ @add_to_active_directory = ]
N
'add_to_active_directory'
]
[ , [ @logreader_job_name = ]
N
'logreader_job_name'
]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. Windows authentication logins must have a user account in the database representing their Windows user account. A user account representing a Windows group isn't sufficient. sp_addlogreader_agent (Transact-SQL) sp_addpublication_snapshot (Transact-SQL) sp_changepublication (Transact-SQL) sp_droppublication (Transact-SQL) sp_helppublication (Transact-SQL) sp_replicationdboption (Transact-SQL) Publish Data and Database Objects
