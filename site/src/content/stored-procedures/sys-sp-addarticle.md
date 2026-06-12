---
name: "sys.sp_addarticle"
title: "sp_addarticle"
category: "general"
description: "Creates an article and adds it to a publication. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
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

Creates an article and adds it to a publication. This stored procedure is executed at the Publisher on the publication database. ## Syntax

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

Only members of the fixed server role or fixed database role can execute. Define an Article sp_articlecolumn (Transact-SQL) sp_articlefilter (Transact-SQL) sp_articleview (Transact-SQL)
