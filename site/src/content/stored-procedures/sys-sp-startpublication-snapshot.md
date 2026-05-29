---
name: 'sys.sp_startpublication_snapshot'
title: 'sp_startpublication_snapshot'
category: 'general'
description: 'Used to start the Snapshot Agent job that generates the initial snapshot for a publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication. , with no default. The name of a non-SQL Server Publisher. , with a default of shouldn''t specify this parameter for a SQL Server Publisher. is used with all types of r'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_startpublication_snapshot'
---

## Description

Used to start the Snapshot Agent job that generates the initial snapshot for a publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication. , with no default. The name of a non-SQL Server Publisher. , with a default of shouldn't specify this parameter for a SQL Server Publisher. is used with all types of replication.

## Syntax

```sql
sp_startpublication_snapshot
```

## Permissions

For a non-SQL Server Publisher, this stored procedure is executed at the Distributor on the distribution database. Only members of the fixed server role or fixed database role can execute . Create and Apply the Initial Snapshot sp_addpublication_snapshot (Transact-SQL) sp_changepublication_snapshot (Transact-SQL) Related content

## Remarks

Applies to:

Used to start the Snapshot Agent job that generates the initial snapshot for a publication. This

stored procedure is executed at the Publisher on the publication database.

Transact-SQL syntax conventions

The name of the publication.

@publication

, with no default.

The name of a non-SQL Server Publisher.

, with a default of

shouldn't specify this parameter for a SQL Server Publisher.

(success) or

is used with all types of replication.
