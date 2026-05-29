---
name: 'sys.sp_helppublication'
title: 'sys.sp_helppublication'
category: 'general'
description: 'Azure SQL Managed Instance'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## Description
Subscribers. This option is valid only if

is set to

.

Specifies whether the Distribution

Agent detects

Configure last writer

conflict detection & resolution

conflicts for a publication that is

enabled for peer-to-peer replication. A

value of

means that last writer

conflicts are detected.

: SQL Server 2019 (15.x) CU

13 and later versions.

(success) or

(failure).

is used in snapshot and transactional replication.


## returns information on all publications owned by the user executing this
procedure.

SQL

Only members of the

fixed server role at the Publisher, members of the

fixed database role on the publication database, or users in the publication access list (PAL) can

execute

.

For a non-SQL Server Publisher, only members of the

fixed server role at the

Distributor, members of the

fixed database role on the distribution database, or

users in the PAL can execute

.

View and Modify Publication Properties

sp_addpublication (Transact-SQL)

sp_changepublication (Transact-SQL)

sp_droppublication (Transact-SQL)

Replication stored procedures (Transact-SQL)

Last updated on 01/19/2026

Related content

```sql
allow_partition_switch
```

```sql
1
```

```sql
enabled_for_p2p_lastwriter_conflictdetection
```

```sql
1
```

```sql
0
```

```sql
1
```

```sql
sp_helppublication
```

```sql
sp_helppublication
```

```sql
sp_helppublication
```

```sql
DECLARE
@myTranPub
AS
sysname
SET
@myTranPub = N
'AdvWorksProductTran'
USE
[AdventureWorks2022]
EXEC sp_helppublication @publication = @myTranPub
GO
```

```sql
sp_helppublication
```
