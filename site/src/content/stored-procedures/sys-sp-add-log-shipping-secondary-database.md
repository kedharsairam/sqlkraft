---
name: 'sys.sp_add_log_shipping_secondary_database'
title: 'sp_add_log_shipping_secondary_database'
category: 'general'
description: 'Sets up a secondary database for log shipping. Transact-SQL syntax conventions The name of the secondary database. The name of the primary instance of the SQL Server Database Engine in the log shipping'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_log_shipping_secondary_database
  [ @secondary_database = ]
  'secondary_database'
  , [ @primary_server = ]
  'primary_server'
  , [ @primary_database = ]
  'primary_database'
  [ , [ @restore_delay = ]
  'restore_delay'
  ]
  [ , [ @restore_all = ]
  'restore_all'
  ]
  [ , [ @restore_mode = ]
  'restore_mode'
  ]
  [ , [ @disconnect_users = ]
  'disconnect_users'
  ]
  [ , [ @block_size = ]
  'block_size'
  ]
  [ , [ @buffer_count = ]
  'buffer_count'
  ]
  [ , [ @max_transfer_size = ]
  'max_transfer_size'
  ]
  [ , [ @restore_threshold = ]
  'restore_threshold'
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
  [ ; ]
---

## Description

Sets up a secondary database for log shipping. Transact-SQL syntax conventions The name of the secondary database. The name of the primary instance of the SQL Server Database Engine in the log shipping

## Syntax

```sql
sp_add_log_shipping_secondary_database
[ @secondary_database = ]
'secondary_database'
, [ @primary_server = ]
'primary_server'
, [ @primary_database = ]
'primary_database'
[ , [ @restore_delay = ]
'restore_delay'
]
[ , [ @restore_all = ]
'restore_all'
]
[ , [ @restore_mode = ]
'restore_mode'
]
[ , [ @disconnect_users = ]
'disconnect_users'
]
[ , [ @block_size = ]
'block_size'
]
[ , [ @buffer_count = ]
'buffer_count'
]
[ , [ @max_transfer_size = ]
'max_transfer_size'
]
[ , [ @restore_threshold = ]
'restore_threshold'
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
[ ; ]
```
