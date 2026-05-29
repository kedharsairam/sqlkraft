---
name: 'sys.sp_adddistributiondb'
title: 'sp_adddistributiondb'
category: 'general'
description: 'Creates a new distribution database and installs the Distributor schema. The distribution database stores procedures, schema, and metadata used in replication. This stored procedure is executed at the Distributor on the database in order to create the distribution database, and install the necessary tables and stored procedures required to enable the Transact-SQL syntax conventions The name of the'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_adddistributiondb
  [ @database = ]
  N
  'database'
  [ , [ @data_folder = ]
  N
  'data_folder'
  ]
  [ , [ @data_file = ]
  N
  'data_file'
  ]
  [ , [ @data_file_size = ] data_file_size ]
  [ , [ @log_folder = ]
  N
  'log_folder'
  ]
  [ , [ @log_file = ]
  N
  'log_file'
  ]
  [ , [ @log_file_size = ] log_file_size ]
  [ , [ @min_distretention = ] min_distretention ]
  [ , [ @max_distretention = ] max_distretention ]
  [ , [ @history_retention = ] history_retention ]
  [ , [ @security_mode = ] security_mode ]
  [ , [ @login = ]
  N
  'login'
  ]
  [ , [ @password = ]
  N
  'password'
  ]
  [ , [ @createmode = ] createmode ]
  [ , [ @from_scripting = ] from_scripting ]
  [ , [ @deletebatchsize_xact = ] deletebatchsize_xact ]
  [ , [ @deletebatchsize_cmd = ] deletebatchsize_cmd ]
  [ ; ]
---

## Description

Creates a new distribution database and installs the Distributor schema. The distribution database stores procedures, schema, and metadata used in replication. This stored procedure is executed at the Distributor on the database in order to create the distribution database, and install the necessary tables and stored procedures required to enable the Transact-SQL syntax conventions The name of the distribution database to be created.

## Syntax

```sql
sp_adddistributiondb
[ @database = ]
N
'database'
[ , [ @data_folder = ]
N
'data_folder'
]
[ , [ @data_file = ]
N
'data_file'
]
[ , [ @data_file_size = ] data_file_size ]
[ , [ @log_folder = ]
N
'log_folder'
]
[ , [ @log_file = ]
N
'log_file'
]
[ , [ @log_file_size = ] log_file_size ]
[ , [ @min_distretention = ] min_distretention ]
[ , [ @max_distretention = ] max_distretention ]
[ , [ @history_retention = ] history_retention ]
[ , [ @security_mode = ] security_mode ]
[ , [ @login = ]
N
'login'
]
[ , [ @password = ]
N
'password'
]
[ , [ @createmode = ] createmode ]
[ , [ @from_scripting = ] from_scripting ]
[ , [ @deletebatchsize_xact = ] deletebatchsize_xact ]
[ , [ @deletebatchsize_cmd = ] deletebatchsize_cmd ]
[ ; ]
```

## Permissions

Only members of the fixed server role can execute . Configure Publishing and Distribution sp_changedistributiondb (Transact-SQL) sp_dropdistributiondb (Transact-SQL) sp_helpdistributiondb (Transact-SQL) System stored procedures (Transact-SQL) Configure Distribution Related content
