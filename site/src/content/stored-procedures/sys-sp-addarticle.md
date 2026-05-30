---
name: "sys.sp_addarticle"
title: "sp_addarticle"
category: "general"
description: "Creates an article and adds it to a publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addarticle
  [ @publication = ]
  N
  'publication'
  , [ @article = ]
  N
  'article'
  [ , [ @source_table = ]
  N
  'source_table'
  ]
  [ , [ @destination_table = ]
  N
  'destination_table'
  ]
  [ , [ @vertical_partition = ]
  N
  'vertical_partition'
  ]
  [ , [ @type = ]
  N
  'type'
  ]
  [ , [ @filter = ]
  N
  'filter'
  ]
  [ , [ @sync_object = ]
  N
  'sync_object'
  ]
  [ , [ @ins_cmd = ]
  N
  'ins_cmd'
  ]
  [ , [ @del_cmd = ]
  N
  'del_cmd'
  ]
  [ , [ @upd_cmd = ]
  N
  'upd_cmd'
  ]
  [ , [ @creation_script = ]
  N
  'creation_script'
  ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @pre_creation_cmd = ]
  N
  'pre_creation_cmd'
  ]
  [ , [ @filter_clause = ]
  N
  'filter_clause'
  ]
  [ , [ @schema_option = ] schema_option ]
  [ , [ @destination_owner = ]
  N
  'destination_owner'
  ]
  [ , [ @status = ] status ]
  [ , [ @source_owner = ]
  N
  'source_owner'
  ]
  [ , [ @sync_object_owner = ]
  N
  'sync_object_owner'
  ]
  [ , [ @filter_owner = ]
  N
  'filter_owner'
  ]
  [ , [ @source_object = ]
  N
  'source_object'
  ]
  [ , [ @artid = ] artid
  OUTPUT
  ]
  [ , [ @auto_identity_range = ]
  N
  'auto_identity_range'
  ]
  [ , [ @pub_identity_range = ] pub_identity_range ]
  [ , [ @identity_range = ] identity_range ]
  [ , [ @threshold = ] threshold ]
  [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
  [ , [ @use_default_datatypes = ] use_default_datatypes ]
  [ , [ @identityrangemanagementoption = ]
  N
  'identityrangemanagementoption'
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @fire_triggers_on_snapshot = ]
  N
  'fire_triggers_on_snapshot'
  ]
  [ ; ]
---

## Description

Creates an article and adds it to a publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions

## Syntax

```sql
sp_addarticle
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @source_table = ]
N
'source_table'
]
[ , [ @destination_table = ]
N
'destination_table'
]
[ , [ @vertical_partition = ]
N
'vertical_partition'
]
[ , [ @type = ]
N
'type'
]
[ , [ @filter = ]
N
'filter'
]
[ , [ @sync_object = ]
N
'sync_object'
]
[ , [ @ins_cmd = ]
N
'ins_cmd'
]
[ , [ @del_cmd = ]
N
'del_cmd'
]
[ , [ @upd_cmd = ]
N
'upd_cmd'
]
[ , [ @creation_script = ]
N
'creation_script'
]
[ , [ @description = ]
N
'description'
]
[ , [ @pre_creation_cmd = ]
N
'pre_creation_cmd'
]
[ , [ @filter_clause = ]
N
'filter_clause'
]
[ , [ @schema_option = ] schema_option ]
[ , [ @destination_owner = ]
N
'destination_owner'
]
[ , [ @status = ] status ]
[ , [ @source_owner = ]
N
'source_owner'
]
[ , [ @sync_object_owner = ]
N
'sync_object_owner'
]
[ , [ @filter_owner = ]
N
'filter_owner'
]
[ , [ @source_object = ]
N
'source_object'
]
[ , [ @artid = ] artid
OUTPUT
]
[ , [ @auto_identity_range = ]
N
'auto_identity_range'
]
[ , [ @pub_identity_range = ] pub_identity_range ]
[ , [ @identity_range = ] identity_range ]
[ , [ @threshold = ] threshold ]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @use_default_datatypes = ] use_default_datatypes ]
[ , [ @identityrangemanagementoption = ]
N
'identityrangemanagementoption'
]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @fire_triggers_on_snapshot = ]
N
'fire_triggers_on_snapshot'
]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Define an Article sp_articlecolumn (Transact-SQL) sp_articlefilter (Transact-SQL) sp_articleview (Transact-SQL) Related content Description then add the table as an article again using sp_addarticle. Replication will then add the column to the table. 21567 16 No The call format VCALL cannot be used for the specified article. VCALL format can be used only for articles in publications that allow updating subscriptions. If you do not require updating subscriptions, specify a different call format. If you do require updating subscriptions, you must drop the publication and re-create it to specify that updating subscriptions are allowed. 21569 16 No The article %s in the publication %s does not have a valid conflict table entry in the system table sysarticleupdates. This entry is required for publications that allow queued updating subscriptions. Check for errors in the last run of the Snapshot Agent. 21570 16 No Cannot create the logical record relationship. Table '%s' does not have a foreign key referencing table '%s'. A logical record relationship requires a foreign key relationship between the parent and child tables. 21571 16 No Cannot create the logical record relationship in publication '%s'. The use_partition_groups option for the publication must be set to "true" in order to use logical records. Use sp_changemergepublication to set the option to "true". 21572 16 No Cannot add a logical record relationship because the foreign key constraint '%s' on table '%s' is disabled. To create the logical record relationship, first enable the foreign key constraint. 21573 16 No Cannot add a logical record relationship because the foreign key constraint '%s' on table '%s' is defined with the NOT FOR REPLICATION option. To add the logical record relationship, first drop the foreign key constraint, and then re-create it without the NOT FOR REPLICATION option. 21574 16 No Cannot add a logical record relationship because the article '%s' is published in publication '%s', which has a compatibility level lower than 90RTM. Use sp_changemergepublication to set the publication_compatibility_level to 90RTM. 21575 16 No The value specified for the property filter_type is not valid. Valid values are 1 (join filter only), 2 (logical record relation only), and 3 (join filter and logical record relation). 21576 16 No Cannot add a logical record relationship between tables '%s' and '%s' because the foreign key column '%s' in table '%s' allows NULL values. Alter the column to disallow NULL values. 21578 16 No In order to use partition_options of 2 (non overlapping partitions with multiple subscriptions per partition) or 3 (non overlapping partitions one subscription per partition) the publication '%s' must be enabled to use
