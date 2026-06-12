---
title: "Extended stored procedures programming"
topic: "query-processing"
description: "Level0type = 'type' and Level0type ="
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

Deprecated feature

Replacement

Feature name

DBCC DBREINDEX

option of.

DBCC DBREINDEX

DBCC INDEXDEFRAG

option of

DBCC INDEXDEFRAG

DBCC SHOWCONTIG

DBCC SHOWCONTIG

DBCC PINTABLE

DBCC UNPINTABLE

Has no effect.

DBCC [UN]PINTABLE

Deprecated feature

Replacement

Feature name

Level0type = 'type' and Level0type =

'USER' to add extended properties to

level-1 or level-2 type objects.

Use Level0type = 'USER' only to add an extended property directly to a

user or role.

Use Level0type = '

' to add an extended property to level-1 types

such as

or VIEW, or level-2 types such as COLUMN or TRIGGER.

For more information, see

sp_addextendedproperty.

EXTPROP_LEVEL0

EXTPROP_LEVEL0USER

Deprecated feature

Replacement

Feature name

Use

Use

argument of

xp_loginconfig

Deprecated feature

Replacement

Feature name

srv_alloc

srv_convert

srv_describe

srv_getbindtoken

srv_got_attention

Use CLR Integration instead.

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

ﾉ

Expand table

Deprecated feature

Replacement

Feature name

srv_message_handler

srv_paramdata

srv_paraminfo

srv_paramlen

srv_parammaxlen

srv_paramname

srv_paramnumber

srv_paramset

srv_paramsetoutput

srv_paramstatus

srv_paramtype

srv_pfield

srv_pfieldex

srv_rpcdb

srv_rpcname

srv_rpcnumber

srv_rpcoptions

srv_rpcowner

srv_rpcparams

srv_senddone

srv_sendmsg

srv_sendrow

srv_setcoldata

srv_setcollen

srv_setutype

srv_willconvert

srv_wsendmsg

Use CLR Integration instead.

`REBUILD`

```sql
ALTER INDEX
```

`REORGANIZE`

```sql
ALTER INDEX
```

`sys.dm_db_index_physical_stats`

`SCHEMA`

`TABLE`

`TYPE`

```sql
xp_grantlogin xp_revokelogin xp_loginConfig
```

```sql
CREATE LOGIN
```

```sql
DROP LOGIN IsIntegratedSecurityOnly
```

```sql
SERVERPROPERTY xp_grantlogin xp_revokelogin
```

`XP_API`

```sql
sp_addextendedproc sp_dropextendedproc sp_helpextendedproc
```

```sql
sp_addextendedproc sp_dropextendedproc sp_helpextendedproc
```
