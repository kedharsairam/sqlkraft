---
title: "Remote servers"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Feature name

value appears in trace events as the ObjectName and in performance counters and

as the instance name. The

Feature ID

value appears in trace events as the ObjectId.

Deprecated feature

Replacement

Feature name

Feature

ID

{

|

}

[MEDIA]

continues to be

deprecated.

{

|

}

and

{

|

}

are discontinued.

None.

or

or

104

103

Deprecated feature

Replacement

Feature name

Feature

ID

Upgrade from version

100 (SQL Server 2008

(10.0.x) and SQL Server

2008 R2 (10.50.x)).

When a SQL Server version goes out of

support

, the associated database

compatibility levels are marked deprecated. However, we continue to support

applications certified on any supported database compatibility level as long as

possible, to make the upgrades easier. For more information about

compatibility levels, see

ALTER DATABASE (Transact-SQL) compatibility level.

Database

compatibility

level 100

108

Deprecated feature

Replacement

Feature name

Feature ID

Ability to return result sets from triggers

None

Returning results from trigger

12

Deprecated feature

Replacement

Feature name

Feature

ID

Encryption using RC4 or RC4_128 is deprecated and is

scheduled to be removed in the next version. Decrypting

RC4 and RC4_128 aren't deprecated.

Use another encryption algorithm such as

AES.

Deprecated

encryption

algorithm

253

Using the MD2, MD4, MD5, SHA, and SHA1 is

deprecated.

Use SHA2_256 or SHA2_512 instead. Older

algorithms continue working, but they raise

a deprecation event.

Deprecated hash

algorithm

None

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

`sys.dm_os_performance_counters`

`RESTORE`

`DATABASE`

`LOG`

`WITH`

`PASSWORD`

`BACKUP`

`DATABASE`

`LOG`

```sql
WITH PASSWORD
```

`BACKUP`

`DATABASE`

`LOG`

```sql
WITH MEDIAPASSWORD
```

```sql
BACKUP DATABASE
```

```sql
BACKUP LOG
WITH PASSWORD
BACKUP DATABASE
```

```sql
BACKUP LOG
WITH MEDIAPASSWORD
```
