---
name: "sys.sp_replcmds"
title: "sp_replcmds"
category: "general"
description: "Returns the commands for transactions marked for replication. This stored procedure is executed at the Publisher on the publication database. The number of transactions to return information about. which specifies the next transaction waiting for distribution. procedure should be run only to troubleshoot problems with replication."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replcmds [ @maxtrans = ] maxtrans
              [ ; ]
---

## Description

Returns the commands for transactions marked for replication. This stored procedure is executed at the Publisher on the publication database. The number of transactions to return information about. which specifies the next transaction waiting for distribution. procedure should be run only to troubleshoot problems with replication.

## Syntax

```sql
sp_replcmds [ @maxtrans = ] maxtrans
[ ; ]
```

## Permissions

A warning message number 18759 is added to both the SQL Server error log and the Microsoft Windows application log, if is unable to replicate a text command because the text pointer wasn't retrieved in the same transaction. Only members of the fixed server role or the fixed database role can execute. Error Messages sp_repldone (Transact-SQL) sp_replflush (Transact-SQL) sp_repltrans (Transact-SQL) System stored procedures (Transact-SQL)
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
