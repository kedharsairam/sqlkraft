---
name: "sys.sp_changemergepublication"
title: "sp_changemergepublication"
category: "general"
description: "Changes the properties of a merge publication. This stored procedure is executed at the Publisher on the publication database. The property to change for the given publication. values listed in the table that follows. The new value for the specified property. , and can be one of the values listed in the table that follows."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changemergepublication
  [ @publication = ]
  N
  'publication'
  [ , [ @property = ]
  N
  'property'
  ]
  [ , [ @value = ]
  N
  'value'
  ]
  [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
  [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
  [ ; ]
---

## Description

Changes the properties of a merge publication. This stored procedure is executed at the Publisher on the publication database. The property to change for the given publication. values listed in the table that follows. The new value for the specified property. , and can be one of the values listed in the table that follows. This table describes the properties of the publication that can be changed, and describes

## Syntax

```sql
sp_changemergepublication
[ @publication = ]
N
'publication'
[ , [ @property = ]
N
'property'
]
[ , [ @value = ]
N
'value'
]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. View and Modify Publication Properties Change Publication and Article Properties sp_addmergepublication (Transact-SQL) sp_dropmergepublication (Transact-SQL) sp_helpmergepublication (Transact-SQL) Replication stored procedures (Transact-SQL)
## Examples

### Example 1

`sp_changemergepublication`

### Example 2

```sql
1
```

### Example 3

```sql
alt_snapshot_folder compress_snapshot dynamic_filters ftp_address ftp_login ftp_password ftp_port ftp_subdirectory post_snapshot_script publication_compatibility_level
```

### Example 4

```sql
80SP3
```

### Example 5

```sql
pre_snapshot_script snapshot_in_defaultfolder sync_mode use_partition_groups
```

### Example 6

```sql
1
```

### Example 7

```sql
dynamic_filters validate_subscriber_info
```

### Example 8

`publish_to_active_directory`

### Example 9

```sql
DECLARE
@publication
AS sysname;
SET
@publication = N
'AdvWorksSalesOrdersMerge'
;
-- Disable DDL replication for the publication.
USE
[AdventureWorks2022]
EXEC sp_changemergepublication
@publication = @publication,
@property = N
'replicate_ddl'
,
@
value
= 0,
@force_invalidate_snapshot = 0,
```
