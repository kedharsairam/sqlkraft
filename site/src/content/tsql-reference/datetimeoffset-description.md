---
name: "datetimeoffset description"
title: "Datetimeoffset description"
category: "data-types"
description: "Azure SQL Managed Instance"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Defines a date that is combined with a time of a day based on a 24-hour clock like

datetime2

,

and adds time zone awareness based on Coordinated Universal Time (UTC).

yyyy-MM-dd HH:mm:ss[.nnnnnnn] [{+|-}hh:mm]

For more information, see the

Backward compatibility for down-level

clients

section that follows.

through

January 1, 1 CE through December 31, 9999 CE

through

through

is four digits, ranging from

through

, that represent a

year.

is two digits, ranging from

to

, that represent a month in

the specified year.

is two digits, ranging from

to

depending on the month,

that represent a day of the specified month.

is two digits, ranging from

to

, that represent the hour.

is two digits, ranging from

to

, that represent the minute.

is two digits, ranging from

to

, that represent the second.

n

is zero to seven digits, ranging from

to

, that represent

the fractional seconds.

is two digits that range from

to

.

is two digits that range from

to

.

Expand table

#### Precision, scale

#### User-defined fractional second

#### precision

#### Time zone offset aware and

#### preservation

#### Specified scale

#### Result (precision, scale)

#### Column length (bytes)

#### Fractional seconds precision

#### datetimeoffset(0)

#### datetimeoffset(1)

#### datetimeoffset(2)

#### datetimeoffset(3)

#### datetimeoffset(4)

#### datetimeoffset(5)

#### datetimeoffset(6)

#### datetimeoffset(7)

```sql
DECLARE @MyDatetimeoffset DATETIMEOFFSET(7);
CREATE TABLE Table1 (Column1 DATETIMEOFFSET(7));
```

```sql
0001-01-01
```

```sql
9999-12-31
```

```sql
00:00:00
```

```sql
23:59:59.9999999
```

```sql
-14:00
```

```sql
+14:00
```

`yyyy`

```sql
0001
```

```sql
9999
```

`MM`

```sql
01
```

```sql
12
```

`dd`

```sql
01
```

```sql
31
```

`HH`

```sql
00
```

```sql
23
```

`mm`

```sql
00
```

```sql
59
```

`ss`

```sql
00
```

```sql
59
```

```sql
0
```

```sql
9999999
```

`hh`

```sql
-14
```

```sql
+14
```

`mm`

```sql
00
```

```sql
59
```
