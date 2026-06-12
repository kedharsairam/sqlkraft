---
name: "xml data type"
title: "Xml data type"
category: "data-types"
description: "When you convert between"
tags: ["tsql","data-types"]
pubDate: "2026-05-29"
---

When you convert between

and the character types

,

,

, and

, the converted time zone offset part should always have double digits for both

and. For example,.

Because Unicode data always uses an even number of bytes, use caution when you convert

or

to or from Unicode supported data types. For example, the following

conversion doesn't return a hexadecimal value of 41. It returns a hexadecimal value of 4100:

For more information, see

Collation and Unicode Support.

Large-value data types have the same implicit and explicit conversion behavior as their smaller

counterparts - specifically, the

,

, and

data types. However, consider

the following guidelines:

Conversion from

to

, and vice-versa, operates as an implicit

conversion, as do conversions between

and

, and

and.

Conversion from large-value data types, such as

, to a smaller counterpart

data type, such as

, is an implicit conversion, but truncation occurs if the size of

the large value exceeds the specified length of the smaller data type.

Conversion from

,

, or

to their corresponding large-value data

types happens implicitly.

Conversion from the

sql_variant

data type to the large-value data types is an explicit

conversion.

Large-value data types can't be converted to the

sql_variant

data type.

For more information about conversion from the

data type, see

Create Instances of XML

Data.



Tip

A practical example on the

can be seen

later in this section.

#### From data type

#### To data type

#### Result

`HH`

`MM`

```sql
-08:00
```

```sql
SELECT
CAST (
CAST (0x41
AS nvarchar
)
AS varbinary);
```
