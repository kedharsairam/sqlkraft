---
name: "Character string constants"
title: "Character string constants"
category: "data-types"
description: ""
tags: ["tsql","data-types"]
pubDate: "2026-05-29"
---

### UTF8-enabled collation

### Unicode string

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

A constant, also known as a literal or a scalar value, is a symbol that represents a specific data

value. The format of a constant depends on the data type of the value it represents.

Character string constants are enclosed in single quotation marks and include alphanumeric

characters (

-

,

-

, and

-

) and special characters, such as exclamation point (

), at sign

(

), and number sign (

). Character string constants are assigned the default collation of the

current database. If the COLLATE clause is used, the conversion to the database default code

page still happens before the conversion to the collation specified by the COLLATE clause.

Character strings typed by users are evaluated through the code page of the computer and are

translated to the database default code page if it's required.

If the QUOTED_IDENTIFIER option has been set OFF for a connection, character strings can also

be enclosed in double quotation marks, but the

Microsoft OLE DB Driver for SQL Server

and

ODBC Driver for SQL Server

automatically use. We recommend

using single quotation marks.

If a character string enclosed in single quotation marks contains an embedded quotation mark,

represent the embedded single quotation mark with two single quotation marks. This isn't

required in strings embedded in double quotation marks.

７

Note

The term

constant

in application development and the concept of a

constant

in Transact-

SQL (T-SQL) aren't the same. There's no specific way to set a global static value in T-SQL.

Constants in T-SQL are the equivalent of string literal values.

７

Note

When a

is specified using the COLLATE clause, conversion to the

database default code page still happens before the conversion to the collation specified

by the COLLATE clause. Conversion isn't done directly to the specified Unicode-enabled

collation. For more information, see.

### varchar(max)

```sql
a
```

```sql
z
```

```sql
A
```

```sql
Z
```

```sql
0
```

```sql
9
```

```sql
!
```

```sql
@
```

```sql
#
```

```sql
SET QUOTED_IDENTIFIER ON
```
