---
name: "sys.sp_change_log_shipping_primary_database"
title: "sp_change_log_shipping_primary_database"
category: "general"
description: "Changes the primary database settings."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_change_log_shipping_primary_database
              [ @database = ]
              'database'
              [ , [ @backup_directory = ]
              N
              'backup_directory'
              ]
              [ , [ @backup_share = ]
              N
              'backup_share'
              ]
              [ , [ @backup_retention_period = ]
              'backup_retention_period'
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
              [ , [ @backup_threshold = ]
              'backup_threshold'
              ]
              [ , [ @threshold_alert = ]
              'threshold_alert'
              ]
              [ , [ @threshold_alert_enabled = ]
              'threshold_alert_enabled'
              ]
              [ , [ @history_retention_period = ]
              'history_retention_period'
              ]
              [ , [ @backup_compression = ] backup_compression_option ]
              [ , [ @monitor_connection_options = ]
              '<key_value_pairs>;[...]'
              ]
              [ ; ]
---

## Description

Changes the primary database settings.

## Syntax

```sql
sp_change_log_shipping_primary_database
[ @database = ]
'database'
[ , [ @backup_directory = ]
N
'backup_directory'
]
[ , [ @backup_share = ]
N
'backup_share'
]
[ , [ @backup_retention_period = ]
'backup_retention_period'
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
[ , [ @backup_threshold = ]
'backup_threshold'
]
[ , [ @threshold_alert = ]
'threshold_alert'
]
[ , [ @threshold_alert_enabled = ]
'threshold_alert_enabled'
]
[ , [ @history_retention_period = ]
'history_retention_period'
]
[ , [ @backup_compression = ] backup_compression_option ]
[ , [ @monitor_connection_options = ]
'<key_value_pairs>;[.]'
]
[ ; ]
```
