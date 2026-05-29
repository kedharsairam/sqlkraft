---
name: 'sys.sp_dropmergepartition'
title: 'sp_dropmergepartition'
category: 'general'
description: 'Analytics Platform System (PDW) Removes a partition for a parameterized row filter from a publication. This stored procedure is executed at the Publisher on the publication database. This stored procedure also removes the corresponding snapshot job and snapshot files for the partition. Transact-SQL syntax conventions function at the Subscriber used to define the partition. function at the Subscrib'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropmergepartition
  [ @publication = ]
  N
  'publication'
  , [ @suser_sname = ]
  N
  'suser_sname'
  , [ @host_name = ]
  N
  'host_name'
  [ ; ]
---

## Description

Analytics Platform System (PDW) Removes a partition for a parameterized row filter from a publication. This stored procedure is executed at the Publisher on the publication database. This stored procedure also removes the corresponding snapshot job and snapshot files for the partition. Transact-SQL syntax conventions function at the Subscriber used to define the partition. function at the Subscriber used to define the partition.

## Syntax

```sql
sp_dropmergepartition
[ @publication = ]
N
'publication'
, [ @suser_sname = ]
N
'suser_sname'
, [ @host_name = ]
N
'host_name'
[ ; ]
```

## Permissions

is used in merge replication. Only members of the fixed server role or fixed database role can execute . Manage Partitions for a Merge Publication with Parameterized Filters Last updated on 11/18/2025 Related content sp_addmergepartition (Transact-SQL) sp_dropmergepartition (Transact-SQL)
