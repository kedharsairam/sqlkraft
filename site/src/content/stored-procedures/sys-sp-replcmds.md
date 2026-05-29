---
name: 'sys.sp_replcmds'
title: 'sp_replcmds'
category: 'general'
description: 'Returns the commands for transactions marked for replication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The number of transactions to return information about. which specifies the next transaction waiting for distribution. procedure should be run only to troubleshoot problems with replication. Arguments for extended stored proce'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replcmds [ @maxtrans = ] maxtrans
  [ ; ]
---

## Description

Returns the commands for transactions marked for replication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The number of transactions to return information about. which specifies the next transaction waiting for distribution. procedure should be run only to troubleshoot problems with replication. Arguments for extended stored procedures must be entered in the specific order as

## Syntax

```sql
sp_replcmds [ @maxtrans = ] maxtrans
[ ; ]
```

## Permissions

A warning message number 18759 is added to both the SQL Server error log and the Microsoft Windows application log, if is unable to replicate a text command because the text pointer wasn't retrieved in the same transaction. Only members of the fixed server role or the fixed database role can execute . Error Messages sp_repldone (Transact-SQL) sp_replflush (Transact-SQL) sp_repltrans (Transact-SQL) System stored procedures (Transact-SQL) Related content Only one client connection can have log reader access to a given database. If a client has log reader access to a database, executing causes the client to release its access. Other clients can then scan the transaction log using or . Only members of the fixed server role or the fixed database role can execute . sp_replcmds (Transact-SQL) sp_repldone (Transact-SQL) sp_repltrans (Transact-SQL) System stored procedures (Transact-SQL) Related content

## Examples

### Example 1

```sql
sp_repltrans
```

### Example 2

```sql
sp_replcmds
```

### Example 3

```sql
sp_repldone
```

### Example 4

```sql
NULL
```

### Example 5

```sql
NULL
```

### Example 6

```sql
1
```

### Example 7

```sql
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
```
