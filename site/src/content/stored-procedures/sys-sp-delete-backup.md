---
name: "sys.sp_delete_backup"
title: "sp_delete_backup"
category: "general"
description: "2016 (13.x) and later versions Deletes all snapshots and the backup file that comprise a snapshot backup set from the specified database. This system stored procedure is the only recommended method for managing snapshot backup sets. For more information, see The URL of the backup to be deleted, which deletes all snapshots comprising the specified backup s"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sys.sp_delete_backup
      [ @backup_url = ]
      N
      'backup_metadata_file_url'
      , [ [ @db_name = ]
      N
      'database_name'
      |
      NULL
      ]
---

## Description

2016 (13.x) and later versions Deletes all snapshots and the backup file that comprise a snapshot backup set from the specified database. This system stored procedure is the only recommended method for managing snapshot backup sets. For more information, see The URL of the backup to be deleted, which deletes all snapshots comprising the specified backup set including the backup file itself.

## Syntax

```sql
sys.sp_delete_backup
[ @backup_url = ]
N
'backup_metadata_file_url'
, [ [ @db_name = ]
N
'database_name'
|
NULL
]
```

## Permissions

06/23/2025 x) and later versions Deletes all snapshots and the backup file that comprise a snapshot backup set from the specified database. This system stored procedure is the only recommended method for managing snapshot backup sets. For more information, see File-Snapshot Backups for Database Files in Azure. syntaxsql The URL of the backup to be deleted, which deletes all snapshots comprising the specified backup set including the backup file itself. The name of the database containing the snapshot to be deleted. When a database name is provided, the system verifies that the backup URL provided is a backup URL for the specified database and uses sp_delete_backup_file_snapshot to delete each snapshot. If no database name is provided, this database check isn't performed. Requires ALTER ANY DATABASE permission or ALTER permission on the specified database. Requires ALTER ANY DATABASE permission. sys.fn_db_backup_file_snapshots (Transact-SQL) sp_delete_backup (Transact-SQL)
