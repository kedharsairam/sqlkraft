---
name: "Date-time constants"
title: "Date-time constants"
category: "data-types"
description: "Binary constants have the prefix"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

Binary constants have the prefix

and are a string of hexadecimal numbers. They aren't

enclosed in quotation marks.

The following are examples of binary strings are:

text

Boolean (

) constants are represented by the numbers

or

, and aren't enclosed in

quotation marks. If a number larger than

is used, it's converted to.

constants are represented by using character date values in specific formats,

enclosed in single quotation marks.

The following are examples of

constants:

text

## Examples of datetime constants are:

text

７

Note

Binary constants greater than 8000 bytes are typed as

data.

```sql
0x
```

```sql
0
```

```sql
1
```

```sql
1
```

```sql
1
```

```sql
0xAE
0x12Ef
0x69048AEFDD010E
0x (empty binary string)
```

```sql
'December 5, 1985'
'5 December, 1985'
'851205'
'12/5/98'
'14:30:24'
'04:24 PM'
```
