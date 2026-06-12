---
name: "sys.sp_add_log_shipping_primary_database"
title: "sp_add_log_shipping_primary_database"
category: "general"
description: "Sets up the primary database for a log shipping configuration, including the backup job, local monitor record, and remote monitor record."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sys.sp_add_log_shipping_primary_database
      [ @database = ]
      N
      'database'
      , [ @backup_directory = ]
      N
      'backup_directory'
      , [ @backup_share = ]
      N
      'backup_share'
      [ , [ @backup_job_name = ]
      N
      'backup_job_name'
      ]
      [ , [ @backup_retention_period = ] backup_retention_period ]
      [ , [ @monitor_server = ]
      N
      'monitor_server'
      ]
      [ , [ @monitor_server_security_mode = ] monitor_server_security_mode ]
      [ , [ @monitor_server_login = ]
      N
      'monitor_server_login'
      ]
      [ , [ @monitor_server_password = ]
      N
      'monitor_server_password'
      ]
      [ , [ @backup_threshold = ] backup_threshold ]
      [ , [ @threshold_alert = ] threshold_alert ]
      [ , [ @threshold_alert_enabled = ] threshold_alert_enabled ]
      [ , [ @history_retention_period = ] history_retention_period ]
      [ , [ @backup_job_id = ]
      'backup_job_id'
      OUTPUT
      ]
      [ , [ @primary_id = ]
      'primary_id'
      OUTPUT
      ]
      [ , [ @overwrite = ] overwrite ]
      [ , [ @ignoreremotemonitor = ] ignoreremotemonitor ]
      [ , [ @backup_compression = ] backup_compression ]
      [ , [ @primary_server_with_port_override = ]
      N
      'primary_server_with_port_override'
      ]
      [ , [ @primary_connection_options = ]
      N
      'primary_connection_options'
      ]
      [ , [ @monitor_connection_options = ]
      N
      'monitor_connection_options'
      ]
      [ ; ]
---

## Description

Sets up the primary database for a log shipping configuration, including the backup job, local monitor record, and remote monitor record. ## Syntax

```sql
sys.sp_add_log_shipping_primary_database
[ @database = ]
N
'database'
, [ @backup_directory = ]
N
'backup_directory'
, [ @backup_share = ]
N
'backup_share'
[ , [ @backup_job_name = ]
N
'backup_job_name'
]
[ , [ @backup_retention_period = ] backup_retention_period ]
[ , [ @monitor_server = ]
N
'monitor_server'
]
[ , [ @monitor_server_security_mode = ] monitor_server_security_mode ]
[ , [ @monitor_server_login = ]
N
'monitor_server_login'
]
[ , [ @monitor_server_password = ]
N
'monitor_server_password'
]
[ , [ @backup_threshold = ] backup_threshold ]
[ , [ @threshold_alert = ] threshold_alert ]
[ , [ @threshold_alert_enabled = ] threshold_alert_enabled ]
[ , [ @history_retention_period = ] history_retention_period ]
[ , [ @backup_job_id = ]
'backup_job_id'
OUTPUT
]
[ , [ @primary_id = ]
'primary_id'
OUTPUT
]
[ , [ @overwrite = ] overwrite ]
[ , [ @ignoreremotemonitor = ] ignoreremotemonitor ]
[ , [ @backup_compression = ] backup_compression ]
[ , [ @primary_server_with_port_override = ]
N
'primary_server_with_port_override'
]
[ , [ @primary_connection_options = ]
N
'primary_connection_options'
]
[ , [ @monitor_connection_options = ]
N
'monitor_connection_options'
]
[ ; ]
```
