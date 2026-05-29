---
name: 'sys.sp_adddistpublisher'
title: 'sp_adddistpublisher'
category: 'general'
description: 'Configures a Publisher to use a specified distribution database. This stored procedure is executed at the Distributor on any database. The stored procedures must have been run prior to using this stored procedure. Transact-SQL syntax conventions Server name can be specified as for a named instance. Specify the port number for your connection when SQL Server is deployed on Linux or Windows with a c'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_adddistpublisher
  [ @publisher = ]
  N
  'publisher'
  , [ @distribution_db = ]
  N
  'distribution_db'
  [ , [ @security_mode = ] security_mode ]
  [ , [ @login = ]
  N
  'login'
  ]
  [ , [ @password = ]
  N
  'password'
  ]
  [ , [ @working_directory = ]
  N
  'working_directory'
  ]
  [ , [ @trusted = ]
  N
  'trusted'
  ]
  [ , [ @encrypted_password = ] encrypted_password ]
  [ , [ @thirdparty_flag = ] thirdparty_flag ]
  [ , [ @publisher_type = ]
  N
  'publisher_type'
  ]
  [ , [ @storage_connection_string = ]
  N
  'storage_connection_string'
  ]
  [ ; ]
---

## Description

Configures a Publisher to use a specified distribution database. This stored procedure is executed at the Distributor on any database. The stored procedures must have been run prior to using this stored procedure. Transact-SQL syntax conventions Server name can be specified as for a named instance. Specify the port number for your connection when SQL Server is deployed on Linux or Windows with a custom

## Syntax

```sql
sp_adddistpublisher
[ @publisher = ]
N
'publisher'
, [ @distribution_db = ]
N
'distribution_db'
[ , [ @security_mode = ] security_mode ]
[ , [ @login = ]
N
'login'
]
[ , [ @password = ]
N
'password'
]
[ , [ @working_directory = ]
N
'working_directory'
]
[ , [ @trusted = ]
N
'trusted'
]
[ , [ @encrypted_password = ] encrypted_password ]
[ , [ @thirdparty_flag = ] thirdparty_flag ]
[ , [ @publisher_type = ]
N
'publisher_type'
]
[ , [ @storage_connection_string = ]
N
'storage_connection_string'
]
[ ; ]
```

## Permissions

Only members of the fixed server role can execute . Configure Publishing and Distribution sp_changedistpublisher (Transact-SQL) Related content Only members of the fixed server role can execute . Configure Publishing and Distribution sp_changedistributiondb (Transact-SQL) sp_dropdistributiondb (Transact-SQL) sp_helpdistributiondb (Transact-SQL) System stored procedures (Transact-SQL) Configure Distribution Related content
