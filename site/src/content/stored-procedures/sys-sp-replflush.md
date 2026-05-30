---
name: "sys.sp_replflush"
title: "sp_replflush"
category: "general"
description: "Azure SQL Managed Instance Flushes the article cache. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions is used in transactional replication. Article definitions are stored in the cache for efficiency. is used by other replication stored procedures whenever an article definition is modified or dropped. You shouldn't have to execute this procedure"
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## Description

Azure SQL Managed Instance Flushes the article cache. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions is used in transactional replication. Article definitions are stored in the cache for efficiency. is used by other replication stored procedures whenever an article definition is modified or dropped. You shouldn't have to execute this procedure manually. You should only use for troubleshooting replication as directed by an experienced replication support

## Permissions

Only one client connection can have log reader access to a given database. If a client has log reader access to a database, executing causes the client to release its access. Other clients can then scan the transaction log using or . Only members of the fixed server role or the fixed database role can execute . sp_replcmds (Transact-SQL) sp_repldone (Transact-SQL) sp_repltrans (Transact-SQL) System stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Azure SQL Managed Instance

Flushes the article cache. This stored procedure is executed at the Publisher on the publication

Transact-SQL syntax conventions

(success) or

is used in transactional replication.

Article definitions are stored in the cache for efficiency.

is used by other

replication stored procedures whenever an article definition is modified or dropped.

You shouldn't have to execute this procedure manually. You should only use

for troubleshooting replication as directed by an experienced replication support

professional.

## Code Blocks

```sql
0
```

```sql
1
```

`sp_replflush`

```sql
sp_replflush
[ ; ]
```

`sp_replcmds`
