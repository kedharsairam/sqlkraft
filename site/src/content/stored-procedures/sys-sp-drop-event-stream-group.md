---
name: 'sys.sp_drop_event_stream_group'
title: 'sys.sp_drop_event_stream_group'
category: 'general'
description: 'Drops a stream event group for the Server 2025 (17.x) and Azure SQL Database. Transact-SQL syntax conventions Specifies the name of the event stream group you want to drop. , with no default, and can''t be server role membership can execute this procedure. Change event streaming is currently in Azure SQL Database (preview feature database scoped configuration not required). During preview, this fea'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_drop_event_stream_group [ @stream_group_name = ]
  N
  'stream_group_name'
  [ ; ]
---

## Description

Drops a stream event group for the Server 2025 (17.x) and Azure SQL Database. Transact-SQL syntax conventions Specifies the name of the event stream group you want to drop. , with no default, and can't be server role membership can execute this procedure. Change event streaming is currently in Azure SQL Database (preview feature database scoped configuration not required). During preview, this feature is subject to change. For current supportability, see

## Syntax

```sql
sys.sp_drop_event_stream_group [ @stream_group_name = ]
N
'stream_group_name'
[ ; ]
```

## Permissions

SQL Server 2025 (17.x) Azure SQL Database Drops a stream event group for the change event streaming (CES) feature introduced in SQL Server 2025 (17.x) and Azure SQL Database. Transact-SQL syntax conventions syntaxsql Specifies the name of the event stream group you want to drop. @stream_group_name is , with no default, and can't be . A user with database permissions, database role membership, or server role membership can execute this procedure. ７ Change event streaming is currently in for: SQL Server 2025 ( ). Azure SQL Database (preview feature database scoped configuration not required). During preview, this feature is subject to change. For current supportability, see .
