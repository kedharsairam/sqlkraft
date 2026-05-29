---
name: 'sys.sp_backup_config_basic'
title: 'managed_backup.sp_backup_config_basic'
category: 'general'
description: 'SQL Server 2016 (13.x) and later versions Configures the SQL Server managed backup to Microsoft Azure basic settings for a specific database or for an instance of SQL Server. Transact-SQL syntax conventions Enable or disable SQL Server managed backup to Microsoft Azure for the specified database. Required parameter when configuring SQL Server managed backup to Microsoft Azure for the first instanc'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  EXECUTE
  managed_backup.sp_backup_config_basic
  [ @enable_backup = ] { 0 | 1 }
  , [ @database_name = ]
  'database_name'
  , [ @container_url = ]
  'Azure_Storage_blob_container'
  , [ @retention_days = ] retention_period_in_days
  , [ @credential_name = ]
  'sql_credential_name'
  [ ; ]
---

## Description

SQL Server 2016 (13.x) and later versions Configures the SQL Server managed backup to Microsoft Azure basic settings for a specific database or for an instance of SQL Server. Transact-SQL syntax conventions Enable or disable SQL Server managed backup to Microsoft Azure for the specified database. Required parameter when configuring SQL Server managed backup to Microsoft Azure for the first instance of SQL Server. If you're changing an existing SQL Server managed backup to

## Syntax

```sql
EXECUTE
managed_backup.sp_backup_config_basic
[ @enable_backup = ] { 0 | 1 }
, [ @database_name = ]
'database_name'
, [ @container_url = ]
'Azure_Storage_blob_container'
, [ @retention_days = ] retention_period_in_days
, [ @credential_name = ]
'sql_credential_name'
[ ; ]
```
