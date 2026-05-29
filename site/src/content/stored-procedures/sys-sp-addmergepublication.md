---
name: 'sys.sp_addmergepublication'
title: 'sp_addmergepublication'
category: 'general'
description: 'Creates a new merge publication. This stored procedure is executed at the Publisher on the database that is being published. Transact-SQL syntax conventions'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergepublication
  [ @publication = ]
  N
  'publication'
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @retention = ] retention ]
  [ , [ @sync_mode = ]
  N
  'sync_mode'
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
  [ , [ @enabled_for_internet = ]
  N
  'enabled_for_internet'
  ]
  [ , [ @centralized_conflicts = ]
  N
  'centralized_conflicts'
  ]
  [ , [ @dynamic_filters = ]
  N
  'dynamic_filters'
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
  [ , [ @conflict_retention = ] conflict_retention ]
  [ , [ @keep_partition_changes = ]
  N
  'keep_partition_changes'
  ]
  [ , [ @allow_subscription_copy = ]
  N
  'allow_subscription_copy'
  ]
  [ , [ @allow_synctoalternate = ]
  N
  'allow_synctoalternate'
  ]
  [ , [ @validate_subscriber_info = ]
  N
  'validate_subscriber_info'
  ]
  [ , [ @add_to_active_directory = ]
  N
  'add_to_active_directory'
  ]
  [ , [ @max_concurrent_merge = ] max_concurrent_merge ]
  [ , [ @max_concurrent_dynamic_snapshots = ] max_concurrent_dynamic_snapshots ]
  [ , [ @use_partition_groups = ]
  N
  'use_partition_groups'
  ]
  [ , [ @publication_compatibility_level = ]
  N
  'publication_compatibility_level'
  ]
  [ , [ @replicate_ddl = ] replicate_ddl ]
  [ , [ @allow_subscriber_initiated_snapshot = ]
  N
  'allow_subscriber_initiated_snapshot'
  ]
  [ , [ @allow_web_synchronization = ]
  N
  'allow_web_synchronization'
  ]
---

## Description

Creates a new merge publication. This stored procedure is executed at the Publisher on the database that is being published. Transact-SQL syntax conventions

## Syntax

```sql
sp_addmergepublication
[ @publication = ]
N
'publication'
[ , [ @description = ]
N
'description'
]
[ , [ @retention = ] retention ]
[ , [ @sync_mode = ]
N
'sync_mode'
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
[ , [ @enabled_for_internet = ]
N
'enabled_for_internet'
]
[ , [ @centralized_conflicts = ]
N
'centralized_conflicts'
]
[ , [ @dynamic_filters = ]
N
'dynamic_filters'
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
[ , [ @conflict_retention = ] conflict_retention ]
[ , [ @keep_partition_changes = ]
N
'keep_partition_changes'
]
[ , [ @allow_subscription_copy = ]
N
'allow_subscription_copy'
]
[ , [ @allow_synctoalternate = ]
N
'allow_synctoalternate'
]
[ , [ @validate_subscriber_info = ]
N
'validate_subscriber_info'
]
[ , [ @add_to_active_directory = ]
N
'add_to_active_directory'
]
[ , [ @max_concurrent_merge = ] max_concurrent_merge ]
[ , [ @max_concurrent_dynamic_snapshots = ] max_concurrent_dynamic_snapshots ]
[ , [ @use_partition_groups = ]
N
'use_partition_groups'
]
[ , [ @publication_compatibility_level = ]
N
'publication_compatibility_level'
]
[ , [ @replicate_ddl = ] replicate_ddl ]
[ , [ @allow_subscriber_initiated_snapshot = ]
N
'allow_subscriber_initiated_snapshot'
]
[ , [ @allow_web_synchronization = ]
N
'allow_web_synchronization'
]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Create a publication Publish Data and Database Objects sp_changemergepublication (Transact-SQL) sp_dropmergepublication (Transact-SQL) sp_helpmergepublication (Transact-SQL) Replication stored procedures (Transact-SQL) Related content
