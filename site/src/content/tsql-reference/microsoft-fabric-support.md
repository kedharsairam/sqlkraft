---
name: "Microsoft Fabric support"
title: "Microsoft Fabric support"
category: "statements"
description: "The ANSI and ISO 8601 compliance sections of the"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

The ANSI and ISO 8601 compliance sections of the

date

and

time

articles apply to

.

Some down-level clients don't support the

,

,

, and

data

types. The following table shows the type mapping between an up-level instance of SQL Server

and down-level clients.

SQL Server

SQLCLIENT

HH:mm:ss[.nnnnnnn]

or

or

yyyy-MM-dd

or

or

yyyy-MM-dd

HH:mm:ss[.nnnnnnn]

or

or

yyyy-MM-dd

HH:mm:ss[.nnnnnnn]

[+|-]hh:mm

or

or

In Microsoft Fabric, currently you can't create columns with the

data type, but

you can use

for converting data with the

AT TIME ZONE

function, for example:

SQL

In Microsoft Fabric SQL database: precision of 7 digits can be used, but mirrored data into

Fabric OneLake would have the time zone and seventh time decimal trimmed. This column

type can't be used as a primary key in tables in Fabric SQL database.

ﾉ

Expand table

### datetimeoffset

### datetimeoffset

### datetime2

```sql
SQL_WVARCHAR
```

```sql
SQL_VARCHAR
DBTYPE_WSTRor
DBTYPE_STR
Java.sql.String
String
```

```sql
SqString
```

```sql
SQL_WVARCHAR
```

```sql
SQL_VARCHAR
DBTYPE_WSTRor
DBTYPE_STR
Java.sql.String
String
```

```sql
SqString
```

```sql
SQL_WVARCHAR
```

```sql
SQL_VARCHAR
DBTYPE_WSTRor
DBTYPE_STR
Java.sql.String
String
```

```sql
SqString
```

```sql
SQL_WVARCHAR
```

```sql
SQL_VARCHAR
DBTYPE_WSTRor
DBTYPE_STR
Java.sql.String
String
```

```sql
SqString
```

```sql
SELECT
CAST
(
CAST
(
'2024-07-03 00:00:00'
AS
DATETIMEOFFSET)
AT
TIME
ZONE
'Pacific
Standard Time'
AS
DATETIME2)
AS
PST;
```
