---
name: "smalldatetime description"
title: "Smalldatetime description"
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

SQL database in Microsoft

Fabric

Defines a date that is combined with a time of day. The time is based on a 24-hour day, with seconds always zero (

) and without fractional seconds.

(used for down-level client)

Not applicable

through

January 1, 1900, through June 6, 2079 through

rounds to is four digits, ranging from 1900 to 2079, which represents a year.

is two digits, ranging from 01 to 12, which represents a month in the specified year.

７

Note

Use the

,

,

, and data types for new work. These types

align with the SQL standard, as they're more portable.

, and

provide more seconds precision.

provides time zone support for globally deployed applications.

Property

Value

Character length

Storage size

Accuracy

Default value

Calendar

User-defined

fractional second precision

Time zone offset aware and

preservation

Daylight saving

aware

smalldatetime

```sql
:00
```

```sql
DECLARE @MySmallDateTime SMALLDATETIME;
CREATE TABLE Table1 (Column1 SMALLDATETIME);
```

```sql
1900-01-01
```

```sql
2079-06-06
```

```sql
00:00:00
```

```sql
23:59:59
2024-05-09 23:59:59
```

```sql
2024-05-10 00:00:00
```

`yyyy`

`MM`
