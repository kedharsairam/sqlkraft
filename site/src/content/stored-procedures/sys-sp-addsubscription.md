---
name: "sys.sp_addsubscription"
title: "sp_addsubscription"
category: "general"
description: "Adds a subscription to a publication and sets the Subscriber status. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_addsubscription
      [ @publication = ]
      N
      'publication'
      [ , [ @article = ]
      N
      'article'
      ]
      [ , [ @subscriber = ]
      N
      'subscriber'
      ]
      [ , [ @destination_db = ]
      N
      'destination_db'
      ]
      [ , [ @sync_type = ]
      N
      'sync_type'
      ]
      [ , [ @status = ]
      N
      'status'
      ]
      [ , [ @subscription_type = ]
      N
      'subscription_type'
      ]
      [ , [ @update_mode = ]
      N
      'update_mode'
      ]
      [ , [ @loopback_detection = ]
      N
      'loopback_detection'
      ]
      [ , [ @frequency_type = ] frequency_type ]
      [ , [ @frequency_interval = ] frequency_interval ]
      [ , [ @frequency_relative_interval = ] frequency_relative_interval ]
      [ , [ @frequency_recurrence_factor = ] frequency_recurrence_factor ]
      [ , [ @frequency_subday = ] frequency_subday ]
      [ , [ @frequency_subday_interval = ] frequency_subday_interval ]
      [ , [ @active_start_time_of_day = ] active_start_time_of_day ]
      [ , [ @active_end_time_of_day = ] active_end_time_of_day ]
      [ , [ @active_start_date = ] active_start_date ]
      [ , [ @active_end_date = ] active_end_date ]
      [ , [ @optional_command_line = ]
      N
      'optional_command_line'
      ]
      [ , [ @reserved = ]
      N
      'reserved'
      ]
      [ , [ @enabled_for_syncmgr = ]
      N
      'enabled_for_syncmgr'
      ]
      [ , [ @offloadagent = ] offloadagent ]
      [ , [ @offloadserver = ]
      N
      'offloadserver'
      ]
      [ , [ @dts_package_name = ]
      N
      'dts_package_name'
      ]
      [ , [ @dts_package_password = ]
      N
      'dts_package_password'
      ]
      [ , [ @dts_package_location = ]
      N
      'dts_package_location'
      ]
      [ , [ @distribution_job_name = ]
      N
      'distribution_job_name'
      ]
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ , [ @backupdevicetype = ]
      N
      'backupdevicetype'
      ]
      [ , [ @backupdevicename = ]
      N
      'backupdevicename'
      ]
      [ , [ @mediapassword = ]
      N
      'mediapassword'
      ]
      [ , [ @password = ]
      N
      'password'
      ]
      [ , [ @fileidhint = ] fileidhint ]
      [ , [ @unload = ] unload ]
---

## Description

Adds a subscription to a publication and sets the Subscriber status. This stored procedure is executed at the Publisher on the publication database. ## Syntax

```sql
sp_addsubscription
[ @publication = ]
N
'publication'
[ , [ @article = ]
N
'article'
]
[ , [ @subscriber = ]
N
'subscriber'
]
[ , [ @destination_db = ]
N
'destination_db'
]
[ , [ @sync_type = ]
N
'sync_type'
]
[ , [ @status = ]
N
'status'
]
[ , [ @subscription_type = ]
N
'subscription_type'
]
[ , [ @update_mode = ]
N
'update_mode'
]
[ , [ @loopback_detection = ]
N
'loopback_detection'
]
[ , [ @frequency_type = ] frequency_type ]
[ , [ @frequency_interval = ] frequency_interval ]
[ , [ @frequency_relative_interval = ] frequency_relative_interval ]
[ , [ @frequency_recurrence_factor = ] frequency_recurrence_factor ]
[ , [ @frequency_subday = ] frequency_subday ]
[ , [ @frequency_subday_interval = ] frequency_subday_interval ]
[ , [ @active_start_time_of_day = ] active_start_time_of_day ]
[ , [ @active_end_time_of_day = ] active_end_time_of_day ]
[ , [ @active_start_date = ] active_start_date ]
[ , [ @active_end_date = ] active_end_date ]
[ , [ @optional_command_line = ]
N
'optional_command_line'
]
[ , [ @reserved = ]
N
'reserved'
]
[ , [ @enabled_for_syncmgr = ]
N
'enabled_for_syncmgr'
]
[ , [ @offloadagent = ] offloadagent ]
[ , [ @offloadserver = ]
N
'offloadserver'
]
[ , [ @dts_package_name = ]
N
'dts_package_name'
]
[ , [ @dts_package_password = ]
N
'dts_package_password'
]
[ , [ @dts_package_location = ]
N
'dts_package_location'
]
[ , [ @distribution_job_name = ]
N
'distribution_job_name'
]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @backupdevicetype = ]
N
'backupdevicetype'
]
[ , [ @backupdevicename = ]
N
'backupdevicename'
]
[ , [ @mediapassword = ]
N
'mediapassword'
]
[ , [ @password = ]
N
'password'
]
[ , [ @fileidhint = ] fileidhint ]
[ , [ @unload = ] unload ]
```

## Permissions

The implemented security mode. @security_mode is , with a default of. specifies SQL Server authentication. specifies Windows authentication. This parameter is deprecated and is provided for backward-compatibility only. Setting @encrypted_password to any value but results in an error. Specifies a non-SQL Server Publisher. @publisher is , with a default of. @publisher shouldn't be used when publishing from a SQL Server Publisher. (success) or (failure). is used in snapshot replication, transactional replication, and merge replication. isn't required when the Subscriber only has anonymous subscriptions to merge publications. writes to the MSsubscriber_info table in the database. ７ Note This parameter is deprecated and is maintained for backward compatibility of scripts. The property is now specified on a per-subscription basis when executing. When a value is specified, it's used as a default when creating subscriptions at this Subscriber and a warning message is returned.

## Examples

### Example 1

`Automatic`

### Example 2

`sp_addsubscription`

### Example 3

`sp_addsubscription`

### Example 4

```sql
-- This script uses sqlcmd scripting variables. They are in the form
-- $(MyVariable). For information about how to use scripting variables
-- on the command line and in SQL Server Management Studio, see the
-- "Executing Replication Scripts" section in the topic
-- "Programming Replication Using System Stored Procedures".
DECLARE
@publication
AS sysname;
DECLARE
@subscriber
AS sysname;
DECLARE
@subscriptionDB
AS sysname;
SET
@publication = N
'AdvWorksProductTran'
;
SET
@subscriber = $(SubServer);
SET
@subscriptionDB = N
'AdventureWorks2022Replica'
;
--Add a push subscription to a transactional publication.
USE
[AdventureWorks2022]
EXEC sp_addsubscription
@publication = @publication,
@subscriber = @subscriber,
@destination_db = @subscriptionDB,
@subscription_type = N
'push'
;
--Add an agent job to synchronize the push subscription.
EXEC sp_addpushsubscription_agent
@publication = @publication,
@subscriber = @subscriber,
@subscriber_db = @subscriptionDB,
@job_login = $(Login),
@job_password = $(Password);
GO
```
