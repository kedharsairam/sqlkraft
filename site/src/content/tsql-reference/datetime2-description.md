---
name: "datetime2 description"
title: "Datetime2 description"
category: "data-types"
description: ""
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Defines a date that is combined with a time of day that is based on 24-hour clock.

can be considered as an extension of the existing

type that has a larger date range, a

larger default fractional precision, and optional user-specified precision.

## Syntax

[ (

fractional seconds precision

) ]

Usage

Default string literal

format

(used for down-level

client)

For more information, see

Backward compatibility for down-level clients

later in

this article.

Date range

through

January 1, 1 CE through December 31, 9999 CE

Time range

through

Time zone offset range

None

Element ranges

is a four-digit number, ranging from

through

, which

represents a year.

is a two-digit number, ranging from

to

, which represents a month in

the specified year.

is a two-digit number, ranging from

to

depending on the month,

which represents a day of the specified month.

is a two-digit number, ranging from

to

, which represents the hour.

is a two-digit number, ranging from

to

, which represents the minute.

Expand table

is a two-digit number, ranging from

to

, which represents the second.

is a zero- to seven-digit number from

to

, which represents the

fractional seconds. In Informatica, the fractional seconds are truncated when

n

is less than.

Character length

19 positions minimum (

) to 27 maximum (

)

Precision, scale

0 to 7 digits, with an accuracy of 100 nanoseconds (100 ns). The default

precision is 7 digits.

In Microsoft Fabric Data Warehouse, this precision can be an integer from 0 to

6, with no default. Precision must be specified in Microsoft Fabric Data

Warehouse.

Storage size

6 bytes for precision less than 3.

7 bytes for precision 3 or 4.

All other precision requires 8 bytes.

Accuracy

100 nanoseconds

Default value

Calendar

Gregorian

User-defined fractional

second precision

Yes

Time zone offset aware

and preservation

No

Daylight saving aware

No

Provided values are for uncompressed rowstore. Use of

data compression

or

columnstore

might alter storage size for each precision. Additionally, storage size on disk and in memory

might differ. For example,

values always require 8 bytes in memory when batch

mode is used.

When a

value is cast to a

value, an extra byte is added to the

value to store precision.

For data type metadata, see

sys.systypes

or

TYPEPROPERTY. Precision and scale are variable for

some date and time data types. To obtain the precision and scale for a column, see

COLUMNPROPERTY

,

COL_LENGTH

, or

sys.columns.

1

2

1

2

#### ISO 8601

#### ODBC

#### data type

#### Default string

#### literal format

#### passed to down-

#### level client

#### Down-level

#### ODBC

#### Down-level

#### OLEDB

#### Down-level

#### JDBC

#### Down-

#### level

```sql
DECLARE @MyDatetime2 datetime2(7);
CREATE TABLE Table1 (Column1 datetime2(7));
```

```sql
yyyy-MM-dd HH:mm:ss[.nnnnnnn]
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
n*
```

```sql
0
```

```sql
9999999
```

```sql
3
```

```sql
yyyy-MM-dd HH:mm:ss
```

```sql
yyyy-MM-dd
HH:mm:ss.0000000
```

```sql
1900-01-01 00:00:00
```
