---
name: "sys.sp_add_log_shipping_secondary_primary"
title: "sp_add_log_shipping_secondary_primary"
category: "general"
description: "Sets up the primary information, adds local and remote monitor links, and creates copy and restore jobs on the secondary server for the specified primary database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_add_log_shipping_secondary_primary
      [ @primary_server = ]
      'primary_server'
      , [ @primary_database = ]
      'primary_database'
      , [ @backup_source_directory = ]
      N
      'backup_source_directory'
      , [ @backup_destination_directory = ]
      N
      'backup_destination_directory'
      , [ @copy_job_name = ]
      'copy_job_name'
      , [ @restore_job_name = ]
      'restore_job_name'
      [ , [ @file_retention_period = ]
      'file_retention_period'
      ]
      [ , [ @monitor_server = ]
      'monitor_server'
      ]
      [ , [ @monitor_server_security_mode = ]
      'monitor_server_security_mode'
      ]
      [ , [ @monitor_server_login = ]
      'monitor_server_login'
      ]
      [ , [ @monitor_server_password = ]
      'monitor_server_password'
      ]
      [ , [ @copy_job_id = ]
      'copy_job_id'
      OUTPUT
      ]
      [ , [ @restore_job_id = ]
      'restore_job_id'
      OUTPUT
      ]
      [ , [ @secondary_id = ]
      'secondary_id'
      OUTPUT
      ]
      [ , [ @secondary_connection_options = ]
      '<key_value_pairs>;[...]'
      ]
      [ , [ @monitor_connection_options = ]
      '<key_value_pairs>;[...]'
      ]
      [ ; ]
---

## Description

Sets up the primary information, adds local and remote monitor links, and creates copy and restore jobs on the secondary server for the specified primary database.

## Syntax

```sql
sp_add_log_shipping_secondary_primary
[ @primary_server = ]
'primary_server'
, [ @primary_database = ]
'primary_database'
, [ @backup_source_directory = ]
N
'backup_source_directory'
, [ @backup_destination_directory = ]
N
'backup_destination_directory'
, [ @copy_job_name = ]
'copy_job_name'
, [ @restore_job_name = ]
'restore_job_name'
[ , [ @file_retention_period = ]
'file_retention_period'
]
[ , [ @monitor_server = ]
'monitor_server'
]
[ , [ @monitor_server_security_mode = ]
'monitor_server_security_mode'
]
[ , [ @monitor_server_login = ]
'monitor_server_login'
]
[ , [ @monitor_server_password = ]
'monitor_server_password'
]
[ , [ @copy_job_id = ]
'copy_job_id'
OUTPUT
]
[ , [ @restore_job_id = ]
'restore_job_id'
OUTPUT
]
[ , [ @secondary_id = ]
'secondary_id'
OUTPUT
]
[ , [ @secondary_connection_options = ]
'<key_value_pairs>;[.]'
]
[ , [ @monitor_connection_options = ]
'<key_value_pairs>;[.]'
]
[ ; ]
```

## Examples

### Example 1

`sp_add_log_shipping_secondary_primary`

### Example 2

`master`

### Example 3

`log_shipping_secondary`

### Example 4

`log_shipping_secondary`

### Example 5

`log_shipping_secondary`

### Example 6

`sp_add_log_shipping_secondary_primary`

### Example 7

`AdventureWorks2022`

### Example 8

```sql
EXECUTE master.dbo.sp_add_log_shipping_secondary_primary
@primary_server = N
'TRIBECA'
,
@primary_database = N
'AdventureWorks2022'
,
@backup_source_directory = N
'\\tribeca\LogShipping'
,
@backup_destination_directory = N
''
,
@copy_job_name = N
''
,
@restore_job_name = N
''
,
@file_retention_period = 1440,
@monitor_server = N
'ROCKAWAY'
,
@monitor_server_security_mode = 1,
@copy_job_id = @LS_Secondary__CopyJobId
OUTPUT
,
@restore_job_id = @LS_Secondary__RestoreJobId
OUTPUT
,
@secondary_id = @LS_Secondary__SecondaryId
OUTPUT
;
GO
```
