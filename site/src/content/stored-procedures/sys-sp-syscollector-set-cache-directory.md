---
name: 'sys.sp_syscollector_set_cache_directory'
title: 'sp_syscollector_set_cache_directory'
category: 'general'
description: 'Specifies the directory where collected data is stored before it''s uploaded to the management Transact-SQL syntax conventions The directory in the file system where collected data is stored temporarily. , with a default of an empty string. If no value is specified, the default temporary You must disable the data collector before changing the cache directory configuration. This stored procedure fai'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_syscollector_set_cache_directory'
---

## Description

Specifies the directory where collected data is stored before it's uploaded to the management Transact-SQL syntax conventions The directory in the file system where collected data is stored temporarily. , with a default of an empty string. If no value is specified, the default temporary You must disable the data collector before changing the cache directory configuration. This stored procedure fails if the data collector is enabled. For more information, see

## Syntax

```sql
sp_syscollector_set_cache_directory
```

## Permissions

06/23/2025 Applies to: SQL Server Specifies the directory where collected data is stored before it's uploaded to the management data warehouse. Transact-SQL syntax conventions syntaxsql The directory in the file system where collected data is stored temporarily. @cache_directory is , with a default of an empty string. If no value is specified, the default temporary SQL Server directory is used. (success) or (failure). You must disable the data collector before changing the cache directory configuration. This stored procedure fails if the data collector is enabled. For more information, see Enable or disable data collection , and Manage data collection . The specified directory doesn't need to exist at the time the is executed; however, data can't be successfully cached and uploaded until the directory is created. We recommend creating the directory before executing this stored procedure.

## Examples

### Example 1

```sql
D:\tempdata
```

### Example 2

```sql
USE
msdb;
GO
EXECUTE
dbo.sp_syscollector_disable_collector;
GO
EXECUTE
dbo.sp_syscollector_set_cache_directory @cache_directory = N
'D:\tempdata'
;
GO
EXECUTE
dbo.sp_syscollector_enable_collector;
GO
```
