---
name: "sys.sp_repltrans"
title: "sp_repltrans"
category: "general"
description: "Returns a result set of all the transactions in the publication database transaction log that are marked for replication but aren't marked as distributed. This stored procedure is executed at the Publisher on a publication database. Transact-SQL syntax conventions returns information about the publication database from which it's executed, allowing you to view transactions currently not distribute"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  EXECUTE
  sp_repldone
  @xactid =
  NULL
  ,
  @xact_seqno =
  NULL
  ,
  @numtrans = 0,
  @
  time
  = 0,
  @
  reset
  = 1;
---

## Description

Returns a result set of all the transactions in the publication database transaction log that are marked for replication but aren't marked as distributed. This stored procedure is executed at the Publisher on a publication database. Transact-SQL syntax conventions returns information about the publication database from which it's executed, allowing you to view transactions currently not distributed (those transactions remaining in the

## Syntax

```sql
EXECUTE sp_repldone
@xactid =
NULL
,
@xact_seqno =
NULL
,
@numtrans = 0,
@
time
= 0,
@
reset
= 1;
```

## Permissions

06/23/2025 Applies to: SQL Server Azure SQL Managed Instance Returns a result set of all the transactions in the publication database transaction log that are marked for replication but aren't marked as distributed. This stored procedure is executed at the Publisher on a publication database. Transact-SQL syntax conventions syntaxsql None. returns information about the publication database from which it's executed, allowing you to view transactions currently not distributed (those transactions remaining in the transaction log that aren't yet sent to the Distributor). The result set displays the log sequence numbers of the first and last records for each transaction. is similar to sp_replcmds , but doesn't return the commands for the transactions. is used in transactional replication. isn't supported for non-SQL Server Publishers. Only members of the fixed server role or the fixed database role can execute . sp_repldone (Transact-SQL) sp_replflush (Transact-SQL) System stored procedures (Transact-SQL) Related content

## Examples

### Example 1

`sp_repltrans`

### Example 2

`sp_replcmds`

### Example 3

`sp_repldone`

### Example 4

`NULL`

### Example 5

`NULL`

### Example 6

```sql
1
```

### Example 7

```sql
EXECUTE sp_repldone
@xactid =
NULL
,
@xact_seqno =
NULL
,
@numtrans = 0,
@
time
= 0,
@
reset
= 1;
```
