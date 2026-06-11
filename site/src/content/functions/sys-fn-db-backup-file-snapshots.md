---
name: "sys.fn_db_backup_file_snapshots"
title: "sys.fn_db_backup_file_snapshots"
category: "backup-restore"
description: "SQL Server 2016 (13.x) and later versions Returns Azure snapshots associated with the database files. If the specified database isn't found, or if the database files aren't stored in the Microsoft Azure Blob Storage, no rows are returned. Use this system function with the procedure to identify and delete orphaned backup snapshots."
tags: ["backup-restore", "function"]
pubDate: 2026-05-29
syntax: "sys.sp_delete_backup_file_snapshot"
---

## Description

SQL Server 2016 (13.x) and later versions Returns Azure snapshots associated with the database files. If the specified database isn't found, or if the database files aren't stored in the Microsoft Azure Blob Storage, no rows are returned. Use this system function with the procedure to identify and delete orphaned backup snapshots. File-Snapshot Backups for Database Files in Azure Transact-SQL syntax conventions

## Syntax

`sys.sp_delete_backup_file_snapshot`

## Permissions

Requires ALTER ANY DATABASE permission. sys.fn_db_backup_file_snapshots (Transact-SQL) sp_delete_backup (Transact-SQL) Related content sys.fn_db_backup_file_snapshots (Transact-SQL) sp_delete_backup_file_snapshot (Transact-SQL) Related content
