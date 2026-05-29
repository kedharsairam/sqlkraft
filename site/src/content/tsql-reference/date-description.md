---
name: 'date description'
title: 'date description'
category: 'data-types'
description: 'Azure SQL Managed Instance'
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

Defines a date in SQL Server. The

data type was introduced in SQL Server 2008 (10.0.x).


## Syntax
Usage

Default string literal format

(used for down-level

client)

For more information, see the

Backward compatibility for down-level clients

section.

Range

through

(

through

for

Informatica)

January 1, 1 CE (Common Era) through December 31, 9999 CE (October 15,

1582 CE through December 31, 9999 CE for Informatica)

Element ranges

is four digits from

to

that represent a year. Informatica

limits

to the range

to

.

is two digits from

to

that represent a month in the specified year.

is two digits from

to

, depending on the month, which represents

a day of the specified month.

Character length

10 positions

Precision, scale

Storage size

3 bytes, fixed

Storage structure

one 3-byte integer stores

Accuracy

One day

ﾉ

Expand table

#### Property

#### Value

#### time

#### datetime2

#### datetimeoffset

### date

### date

```sql
DATE
```

```sql
DECLARE @MyDate DATE
CREATE TABLE Table1 (Column1 DATE)
```

```sql
yyyy-MM-dd
```

```sql
0001-01-01
```

```sql
9999-12-31
```

```sql
1582-10-15
```

```sql
9999-12-31
```

```sql
yyyy
```

```sql
0001
```

```sql
9999
```

```sql
yyyy
```

```sql
1582
```

```sql
9999
```

```sql
MM
```

```sql
01
```

```sql
12
```

```sql
dd
```

```sql
01
```

```sql
31
```

```sql
10, 0
```
