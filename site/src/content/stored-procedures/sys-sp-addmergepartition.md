---
name: 'sys.sp_addmergepartition'
title: 'sp_addmergepartition'
category: 'general'
description: 'Creates a dynamically filtered partition for a subscription, filtered by the values of at the Subscriber. This stored procedure is executed at the Publisher on the database that is being published, and is used to manually generate partitions. Transact-SQL syntax conventions The merge publication on which the partition is being created. The value used when creating the partition for a subscription,'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergepartition
  [ @publication = ]
  N
  'publication'
  [ , [ @suser_sname = ]
  N
  'suser_sname'
  ]
  [ , [ @host_name = ]
  N
  'host_name'
  ]
  [ ; ]
---

## Description

Creates a dynamically filtered partition for a subscription, filtered by the values of at the Subscriber. This stored procedure is executed at the Publisher on the database that is being published, and is used to manually generate partitions. Transact-SQL syntax conventions The merge publication on which the partition is being created. The value used when creating the partition for a subscription, filtered by the value of the

## Syntax

```sql
sp_addmergepartition
[ @publication = ]
N
'publication'
[ , [ @suser_sname = ]
N
'suser_sname'
]
[ , [ @host_name = ]
N
'host_name'
]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Create a Snapshot for a Merge Publication with Parameterized Filters Parameterized Filters - Parameterized Row Filters Related content Only members of the fixed server role or the fixed database role can execute . Create a Snapshot for a Merge Publication with Parameterized Filters Parameterized Filters - Parameterized Row Filters sp_dropdynamicsnapshot_job (Transact-SQL) sp_helpdynamicsnapshot_job (Transact-SQL) Related content sp_addmergepartition (Transact-SQL) sp_dropmergepartition (Transact-SQL)
