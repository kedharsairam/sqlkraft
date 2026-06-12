---
name: "sys.sp_backup_config_advanced"
title: "managed_backup.sp_backup_config_advanced"
category: "general"
description: "managed_backup.sp_backup_config_advanced (Transact-SQL) managed_backup.sp_backup_config_schedule (Transact-SQL)"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  USE
              msdb;
              GO
              EXECUTE
              managed_backup.sp_backup_config_advanced
              @encryption_algorithm =
              'AES_128'
              ,
              @encryptor_type =
              'CERTIFICATE'
              ,
              @encryptor_name =
              'MyTestDBBackupEncryptCert'
              ;
              GO
---

## Description

managed_backup.sp_backup_config_advanced (Transact-SQL) managed_backup.sp_backup_config_schedule (Transact-SQL)

## Syntax

```sql
USE msdb;
GO
EXECUTE managed_backup.sp_backup_config_advanced
@encryption_algorithm =
'AES_128'
,
@encryptor_type =
'CERTIFICATE'
,
@encryptor_name =
'MyTestDBBackupEncryptCert'
;
GO
```
