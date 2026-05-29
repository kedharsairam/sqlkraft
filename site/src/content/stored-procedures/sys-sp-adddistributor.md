---
name: 'sys.sp_adddistributor'
title: 'sp_adddistributor'
category: 'general'
description: 'table (if there isn''t one), marks the server entry as a Distributor, and stores property information. This stored procedure is executed at the database to register and mark the server as a distributor. In the case of a remote distributor, it''s also executed at the Publisher from the Transact-SQL syntax conventions , with no default. This parameter is only used if setting up a remote Distributor. I'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_adddistributor
  [ @distributor = ]
  N
  'distributor'
  [ , [ @heartbeat_interval = ] heartbeat_interval ]
  [ , [ @password = ]
  N
  'password'
  ]
  [ , [ @from_scripting = ] from_scripting ]
  [ , [ @encrypt_distributor_connection = ]
  N
  'encrypt_distributor_connection'
  ]
  [ , [ @trust_distributor_certificate = ]
  N
  'trust_distributor_certificate'
  ]
  [ , [ @host_name_in_distributor_certificate = ]
  N
  'host_name_in_distributor_certificate'
  ]
  [ ; ]
---

## Description

table (if there isn't one), marks the server entry as a Distributor, and stores property information. This stored procedure is executed at the database to register and mark the server as a distributor. In the case of a remote distributor, it's also executed at the Publisher from the Transact-SQL syntax conventions , with no default. This parameter is only used if setting up a remote Distributor. It adds entries for the Distributor properties in the

## Syntax

```sql
sp_adddistributor
[ @distributor = ]
N
'distributor'
[ , [ @heartbeat_interval = ] heartbeat_interval ]
[ , [ @password = ]
N
'password'
]
[ , [ @from_scripting = ] from_scripting ]
[ , [ @encrypt_distributor_connection = ]
N
'encrypt_distributor_connection'
]
[ , [ @trust_distributor_certificate = ]
N
'trust_distributor_certificate'
]
[ , [ @host_name_in_distributor_certificate = ]
N
'host_name_in_distributor_certificate'
]
[ ; ]
```

## Permissions

Only members of the fixed server role can execute . Configure Publishing and Distribution sp_changedistributor_property (Transact-SQL) sp_dropdistributor (Transact-SQL) sp_helpdistributor (Transact-SQL) System stored procedures (Transact-SQL) Configure Distribution Last updated on 11/18/2025 Related content View and Modify Distributor and Publisher Properties sp_adddistributor (Transact-SQL) sp_dropdistributor (Transact-SQL) sp_helpdistributor (Transact-SQL) Replication stored procedures (Transact-SQL) Last updated on 11/18/2025 Related content
