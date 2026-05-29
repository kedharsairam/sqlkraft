---
title: "Collations"
topic: "io-fundamentals"
description: ". For more information, see"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Deprecated feature

Replacement

Feature name

...

. For more information, see

ALTER DATABASE

(Transact-SQL) compatibility level

.

Database

compatibility level

110 and 120.

Plan to upgrade the database and application for a future release. However, we continue

to support applications certified on any supported database compatibility level as long as

possible, to make the upgrades easier. For more information about compatibility levels,

see

ALTER DATABASE (Transact-SQL) compatibility level

.

Database

compatibility level

110

Database

compatibility level

120

Deprecated feature

Replacement

Feature name

Korean_Wansung_Unicode

Lithuanian_Classic

SQL_AltDiction_CP1253_CS_AS

None. These collations exist in SQL Server 2005 (9.x), but aren't visible

through fn_helpcollations.

Korean_Wansung_Unicode

Lithuanian_Classic

SQL_AltDiction_CP1253_CS_AS

Hindi

Macedonian

These collations exist in SQL Server 2005 (9.x) and higher, but aren't

visible through fn_helpcollations. Use Macedonian_FYROM_90 and

Indic_General_90 instead.

Hindi

Macedonian

Azeri_Latin_90

Azeri_Cyrilllic_90

Azeri_Latin_100

Azeri_Cyrilllic_100

Azeri_Latin_90

Azeri_Cyrilllic_90

Deprecated feature

Replacement

Feature name

sp_droptype

timestamp

## syntax for

rowversion

data type

rowversion

data type syntax

Ability to insert null values into

timestamp

columns.

Use a

instead.

into

columns

'text in row' table option

Use

varchar(max)

,

nvarchar(max)

, and

varbinary(max)

data types.

For more information, see

sp_tableoption

.

Text in row table option

Data types:

text

ntext

image

Use

varchar(max)

,

nvarchar(max)

, and

varbinary(max)

data types.

Data types:

text

,

ntext

, or

image

ﾉ

Expand table

ﾉ

Expand table

```sql
sp_dbcmptlevel
ALTER DATABASE
```

```sql
SET COMPATIBILITY_LEVEL
```

```sql
sp_dbcmptlevel
```

```sql
sp_addtype
sp_droptype
CREATE TYPE
DROP TYPE
sp_addtype
```

```sql
TIMESTAMP
```

```sql
DEFAULT
```

```sql
INSERT NULL
```

```sql
TIMESTAMP
```
