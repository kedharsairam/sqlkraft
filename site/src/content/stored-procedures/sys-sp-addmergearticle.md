---
name: "sys.sp_addmergearticle"
title: "sp_addmergearticle"
category: "general"
description: "Adds an article to an existing merge publication. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergearticle
              [ @publication = ]
              N
              'publication'
              , [ @article = ]
              N
              'article'
              , [ @source_object = ]
              N
              'source_object'
              [ , [ @type = ]
              N
              'type'
              ]
              [ , [ @description = ]
              N
              'description'
              ]
              [ , [ @column_tracking = ]
              N
              'column_tracking'
              ]
              [ , [ @status = ]
              N
              'status'
              ]
              [ , [ @pre_creation_cmd = ]
              N
              'pre_creation_cmd'
              ]
              [ , [ @creation_script = ]
              N
              'creation_script'
              ]
              [ , [ @schema_option = ] schema_option ]
              [ , [ @subset_filterclause = ]
              N
              'subset_filterclause'
              ]
              [ , [ @article_resolver = ]
              N
              'article_resolver'
              ]
              [ , [ @resolver_info = ]
              N
              'resolver_info'
              ]
              [ , [ @source_owner = ]
              N
              'source_owner'
              ]
              [ , [ @destination_owner = ]
              N
              'destination_owner'
              ]
              [ , [ @vertical_partition = ]
              N
              'vertical_partition'
              ]
              [ , [ @auto_identity_range = ]
              N
              'auto_identity_range'
              ]
              [ , [ @pub_identity_range = ] pub_identity_range ]
              [ , [ @identity_range = ] identity_range ]
              [ , [ @threshold = ] threshold ]
              [ , [ @verify_resolver_signature = ] verify_resolver_signature ]
              [ , [ @destination_object = ]
              N
              'destination_object'
              ]
              [ , [ @allow_interactive_resolver = ]
              N
              'allow_interactive_resolver'
              ]
              [ , [ @fast_multicol_updateproc = ]
              N
              'fast_multicol_updateproc'
              ]
              [ , [ @check_permissions = ] check_permissions ]
              [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
              [ , [ @published_in_tran_pub = ]
              N
              'published_in_tran_pub'
              ]
              [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
              [ , [ @logical_record_level_conflict_detection = ]
              N
              'logical_record_level_conflict_detection'
              ]
              [ , [ @logical_record_level_conflict_resolution = ]
              N
              'logical_record_level_conflict_resolution'
              ]
              [ , [ @partition_options = ] partition_options ]
              [ , [ @processing_order = ] processing_order ]
              [ , [ @subscriber_upload_options = ] subscriber_upload_options ]
---

## Description

Adds an article to an existing merge publication. This stored procedure is executed at the Publisher on the publication database. ## Syntax

```sql
sp_addmergearticle
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
, [ @source_object = ]
N
'source_object'
[ , [ @type = ]
N
'type'
]
[ , [ @description = ]
N
'description'
]
[ , [ @column_tracking = ]
N
'column_tracking'
]
[ , [ @status = ]
N
'status'
]
[ , [ @pre_creation_cmd = ]
N
'pre_creation_cmd'
]
[ , [ @creation_script = ]
N
'creation_script'
]
[ , [ @schema_option = ] schema_option ]
[ , [ @subset_filterclause = ]
N
'subset_filterclause'
]
[ , [ @article_resolver = ]
N
'article_resolver'
]
[ , [ @resolver_info = ]
N
'resolver_info'
]
[ , [ @source_owner = ]
N
'source_owner'
]
[ , [ @destination_owner = ]
N
'destination_owner'
]
[ , [ @vertical_partition = ]
N
'vertical_partition'
]
[ , [ @auto_identity_range = ]
N
'auto_identity_range'
]
[ , [ @pub_identity_range = ] pub_identity_range ]
[ , [ @identity_range = ] identity_range ]
[ , [ @threshold = ] threshold ]
[ , [ @verify_resolver_signature = ] verify_resolver_signature ]
[ , [ @destination_object = ]
N
'destination_object'
]
[ , [ @allow_interactive_resolver = ]
N
'allow_interactive_resolver'
]
[ , [ @fast_multicol_updateproc = ]
N
'fast_multicol_updateproc'
]
[ , [ @check_permissions = ] check_permissions ]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @published_in_tran_pub = ]
N
'published_in_tran_pub'
]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ , [ @logical_record_level_conflict_detection = ]
N
'logical_record_level_conflict_detection'
]
[ , [ @logical_record_level_conflict_resolution = ]
N
'logical_record_level_conflict_resolution'
]
[ , [ @partition_options = ] partition_options ]
[ , [ @processing_order = ] processing_order ]
[ , [ @subscriber_upload_options = ] subscriber_upload_options ]
```
