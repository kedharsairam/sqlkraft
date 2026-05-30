---
name: "sys.sp_replrestart"
title: "sp_replrestart"
category: "general"
description: "Used by transactional replication during backup and restore so that the replicated data at the Distributor is synchronized with data at the Publisher. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions is used when the highest log sequence number (LSN) value at the Distributor doesn't match the highest LSN value at the Publisher. fixed d"
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## Description

Used by transactional replication during backup and restore so that the replicated data at the Distributor is synchronized with data at the Publisher. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions is used when the highest log sequence number (LSN) value at the Distributor doesn't match the highest LSN value at the Publisher. fixed database role can execute

## Permissions

06/23/2025 Applies to: SQL Server Azure SQL Managed Instance Used by transactional replication during backup and restore so that the replicated data at the Distributor is synchronized with data at the Publisher. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions syntaxsql None. (success) or (failure). is used when the highest log sequence number (LSN) value at the Distributor doesn't match the highest LSN value at the Publisher. Only members of the fixed server role or fixed database role can execute . ） Important is an internal replication stored procedure and should only be used when restoring a database published in a transactional replication topology as directed in .

## Code Blocks

```sql
0
```

```sql
1
```

`sp_replrestart`

```sql
sp_replrestart
[ ; ]
```
