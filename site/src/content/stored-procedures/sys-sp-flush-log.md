---
name: 'sys.sp_flush_log'
title: 'sys.sp_flush_log'
category: 'general'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

06/23/2025

Applies to:

SQL Server 2016 (13.x) and later versions

Flushes to disk the transaction log of the current database, thereby hardening all previously

committed delayed durable transactions.

If you choose to use delayed transaction durability because of the performance benefits, but

you also want to have a guaranteed limit on the amount of data that is lost on server crash or

failover, then execute

on a regular schedule. For example, if you want to

make sure you don't lose more than

n

seconds worth of data, you would execute

every

n

seconds.

Executing

guarantees that all previously committed delayed durable

transactions are made durable. For more information, see

Control Transaction Durability

.

Transact-SQL syntax conventions


## syntaxsql
None.

A return code of

indicates success. Any other value indicates failure.

None.

SQL

SQL Server transaction log architecture and management guide

Related content

```sql
sys.sp_flush_log
```

```sql
sp_flush_log
```

```sql
sys.sp_flush_log
```

```sql
1
```

```sql
sp_flush_log
[ ; ]
```

```sql
EXECUTE
sys.sp_flush_log;
```
