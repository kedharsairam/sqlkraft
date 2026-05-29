---
name: "sys.sp_backup_on_demand"
title: "managed_backup.sp_backup_on_demand"
category: "general"
description: "SQL Server 2016 (13.x) and later versions Requests SQL Server managed backup to Microsoft Azure to perform a backup of the specified Use this stored procedure to perform ad hoc backups for a database configured with SQL Server managed backup to Microsoft Azure. This prevents any break in the backup chain and SQL Server managed backup to Microsoft Azure processes are aware and the backup is stored "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  EXECUTE
  managed_backup.sp_backup_on_demand
  [ @database_name = ]
  'database name'
  , [ @type = ] {
  'Database'
  |
  'Log'
  }
  [ ; ]
---

## Description

SQL Server 2016 (13.x) and later versions Requests SQL Server managed backup to Microsoft Azure to perform a backup of the specified Use this stored procedure to perform ad hoc backups for a database configured with SQL Server managed backup to Microsoft Azure. This prevents any break in the backup chain and SQL Server managed backup to Microsoft Azure processes are aware and the backup is stored in the same Azure Blob storage container.

## Syntax

```sql
EXECUTE
managed_backup.sp_backup_on_demand
[ @database_name = ]
'database name'
, [ @type = ] {
'Database'
|
'Log'
}
[ ; ]
```
