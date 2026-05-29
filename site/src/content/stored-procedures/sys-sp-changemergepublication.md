---
name: 'sys.sp_changemergepublication'
title: 'sp_changemergepublication'
category: 'general'
description: 'Changes the properties of a merge publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The property to change for the given publication. values listed in the table that follows. The new value for the specified property. , and can be one of the values listed in the table that follows. This table describes the properties of the '
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

Changes the properties of a merge publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The property to change for the given publication. values listed in the table that follows. The new value for the specified property. , and can be one of the values listed in the table that follows. This table describes the properties of the publication that can be changed, and describes

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

Only members of the fixed server role or fixed database role can execute . View and Modify Publication Properties Change Publication and Article Properties sp_addmergepublication (Transact-SQL) sp_dropmergepublication (Transact-SQL) sp_helpmergepublication (Transact-SQL) Replication stored procedures (Transact-SQL) Related content View and Modify Publication Properties sp_addmergepublication (Transact-SQL) sp_changemergepublication (Transact-SQL) sp_dropmergepublication (Transact-SQL) Replication stored procedures (Transact-SQL) Related content If you're running continuous mode merges, you must either: Stop the Merge Agent, and then perform another merge without the parameter specified. Deactivate the publication with to ensure that any continuous-mode merges that are polling for the publication status fail. SQL When you have completed step 3 of running , resume continuous mode merges based on how you stopped them. Either: Add the parameter back for the Merge Agent. Reactivate the publication with . SQL Only members of the fixed server role or fixed database role can execute . To use this stored procedure, the Publisher must be running SQL Server 2000 (8.x). The Subscribers must be running either SQL Server 2000 (8.x) or SQL Server 7.0, Service Pack 2. MSmerge_genhistory (Transact-SQL) MSmerge_contents (Transact-SQL) MSmerge_tombstone (Transact-SQL) Related content Description partition groups functionality. Use sp_changemergepublication to set 'use_partition_groups' to 'true'. 21579 16 No Article "%s" in publication "%s" does not qualify for the partition option that you specified. You cannot specify a value of 2 or 3 (nonoverlapping partitions) for the @partition_options parameter because the article is involved in multiple join filters. Either select a value of 0 or 1 for the @partition_options parameter, or drop all but one of the join filters by using sp_dropmergefilter. 21580 16 No Article "%s" in publication "%s" does not qualify for the partition option that you specified. You cannot specify a value of 2 or 3 (nonoverlapping partitions) for the @partition_options parameter because the article is involved in both a row filter and a join filter. Either select a value of 0 or 1 for the @partition_options parameter; drop the join filter by using sp_dropmergefilter; or change the row filter by using sp_changemergepublication. 21581 16 No Article "%s" in publication "%s" does not qualify for the partition option that you specified. You cannot specify a value of 2 or 3 (nonoverlapping partitions) for the @partition_options parameter because the article has a join filter with a join_unique_key value of 0. Either select a value of 0 or 1 for the @partition_options parameter, or use sp_changemergefilter to specify a value of 1 for join_unique_key. 21582 16 No Article "%s" in publication "%s" does not qualify for the partition option that you specified. You cannot specify a value of 2 or 3 (nonoverlapping partitions) for the @partition_options parameter because the article has a direct or indirect join filter relationship with parent article "%s". The parent article does not use the same value for partition_options. Use sp_changemergepublication to change the value for one of the articles. 21583 16 No Cannot update the column in article '%s'. The article has a value of 2 or 3 (nonoverlapping partitions) for the partition_options property, and the column is involved in a row filter and/or a join filter. In this situation, the column cannot be updated at a Subscriber or republisher; it must be updated at the top-level Publisher. 21584 16 No Cannot insert the row for article '%s'. The row does not belong to the Subscriber's partition, and the article has a value of 2 or 3 (nonoverlapping partitions) for the partition_options property. Nonoverlapping partitions do not allow out-of-partition inserts. 21585 16 No Cannot specify custom article ordering in publication '%s' because the publication has a compatibility level lower than 90RTM. Use sp_changemergepublication to set the publication_compatibility_level to 90RTM.

## Examples

### Example 1

```sql
sp_changemergepublication
```

### Example 2

```sql
1
```

### Example 3

```sql
alt_snapshot_folder
compress_snapshot
dynamic_filters
ftp_address
ftp_login
ftp_password
ftp_port
ftp_subdirectory
post_snapshot_script
publication_compatibility_level
```

### Example 4

```sql
80SP3
```

### Example 5

```sql
pre_snapshot_script
snapshot_in_defaultfolder
sync_mode
use_partition_groups
```

### Example 6

```sql
1
```

### Example 7

```sql
dynamic_filters
validate_subscriber_info
```

### Example 8

```sql
publish_to_active_directory
```

### Example 9

```sql
DECLARE
@publication
AS
sysname;
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
