---
name: 'sys.sp_setnetname'
title: 'sp_setnetname'
category: 'general'
description: 'to their actual network computer names for remote instances of SQL Server. This procedure can be used to enable execution of remote stored procedure calls to computers that have network names containing SQL Server identifiers that Transact-SQL syntax conventions The name of the remote server as referenced in user-coded remote stored procedure call , with no default. Exactly one row in The network '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_setnetname
  [ @server = ]
  N
  'server'
  , [ @netname = ]
  N
  'netname'
  [ ; ]
---

## Description

to their actual network computer names for remote instances of SQL Server. This procedure can be used to enable execution of remote stored procedure calls to computers that have network names containing SQL Server identifiers that Transact-SQL syntax conventions The name of the remote server as referenced in user-coded remote stored procedure call , with no default. Exactly one row in The network name of the computer to which remote stored procedure calls are made.

## Syntax

```sql
sp_setnetname
[ @server = ]
N
'server'
, [ @netname = ]
N
'netname'
[ ; ]
```

## Examples

### Example 1

```sql
sp_setnetname
```

### Example 2

```sql
sqlserv2
```

### Example 3

```sql
EXECUTE
sp_addlinkedserver
'sqlserv2'
;
GO
EXECUTE
sp_addserver
'rpcserv2'
;
GO
EXECUTE
sp_setnetname
'rpcserv2'
,
'sqlserv2'
;
```

### Example 4

```sql
sp_setnetname
```

### Example 5

```sql
USE
master
;
GO
EXECUTE
sp_addserver
'Win_1'
;
EXECUTE
sp_setnetname
'Win_1'
,
'Win-1'
;
EXECUTE
Win_1.master.dbo.sp_who;
```
