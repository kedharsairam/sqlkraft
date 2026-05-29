---
name: "sys.sp_change_log_shipping_secondary_primary"
title: "sp_change_log_shipping_secondary_primary"
category: "general"
description: "Changes secondary database settings. Transact-SQL syntax conventions The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_change_log_shipping_secondary_primary
  [ @primary_server = ]
  'primary_server'
  ,
  [ @primary_database = ]
  'primary_database'
  ,
  [ , [ @backup_source_directory = ]
  N
  'backup_source_directory'
  ]
  [ , [ @backup_destination_directory = ]
  N
  'backup_destination_directory'
  ]
  [ , [ @file_retention_period = ] file_retention_period ]
  [ , [ @monitor_server_security_mode = ] monitor_server_security_mode ]
  [ , [ @monitor_server_login = ]
  'monitor_server_login'
  ]
  [ , [ @monitor_server_password = ]
  'monitor_server_password'
  ]
  [ , [ @monitor_connection_options = ]
  '<key_value_pairs>;[...]'
  ]
  [ ; ]
---

## Description

Changes secondary database settings. Transact-SQL syntax conventions The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server.

## Syntax

```sql
sp_change_log_shipping_secondary_primary
[ @primary_server = ]
'primary_server'
,
[ @primary_database = ]
'primary_database'
,
[ , [ @backup_source_directory = ]
N
'backup_source_directory'
]
[ , [ @backup_destination_directory = ]
N
'backup_destination_directory'
]
[ , [ @file_retention_period = ] file_retention_period ]
[ , [ @monitor_server_security_mode = ] monitor_server_security_mode ]
[ , [ @monitor_server_login = ]
'monitor_server_login'
]
[ , [ @monitor_server_password = ]
'monitor_server_password'
]
[ , [ @monitor_connection_options = ]
'<key_value_pairs>;[...]'
]
[ ; ]
```
