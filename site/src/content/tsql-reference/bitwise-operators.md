---
name: "Bitwise operators"
title: "Bitwise operators"
category: "data-types"
description: ""
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

Operator

Bitwise math

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure

Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in Microsoft

Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Bitwise operators perform bit manipulations between two expressions of any of the data types of the integer data type category.

Bitwise operators convert two integer values to binary bits, perform the

,

, or operation on each bit, producing a result. Then converts the result to an integer.

For example, the integer converts to binary.

The integer converts to binary.

If bits at any position are both

, the result is.

= 170

= 75

---

= 10

If either bit at any position is

, the result is.

= 170

= 75

---

= 235

Reverses the bit value at every bit position.

= 170

---

= 85

The following articles provide more information about the bitwise operators available in the Database Engine:
& (Bitwise AND)

&= (Bitwise AND assignment)

| (Bitwise OR)

|= (Bitwise OR assignment)

^ (Bitwise exclusive OR)

image

Left operand

Right operand

int

smallint

tinyint

int

smallint

tinyint

bit

bigint

int

smallint

tinyint

binary

varbinary

int

smallint

tinyint

binary

varbinary

int

smallint

tinyint

binary

varbinary

int

smallint

tinyint

binary

varbinary

int

smallint

tinyint

^= (Bitwise exclusive OR assignment)

~ (Bitwise NOT)

The following bitwise operators were introduced in SQL Server 2022 (16.x): RIGHT_SHIFT

LEFT_SHIFT

Operands for bitwise operators can be any one of the data types of the integer or binary string data type categories (except for the data type), except that both operands can't be any one of the data types of the binary string data type category. The following table shows the supported operand data types.

binary

,

, or bit

,

,

, or bigint

,

,

,

,

, or int

,

,

,

, or smallint

,

,

,

, or tinyint

,

,

,

, or varbinary

,

, or Operators (Transact-SQL)

Data types (Transact-SQL)

Compound Operators (Transact-SQL)

`AND`

`OR`

`NOT`

```sql
170
```

```sql
1010 1010
```

```sql
75
```

```sql
0100 1011
```

`AND`

```sql
1
```

```sql
1
```

```sql
1010 1010
```

```sql
0100 1011
```

```sql
0000 1010
```

`OR`

```sql
1
```

```sql
1
```

```sql
1010 1010
```

```sql
0100 1011
```

```sql
1110 1011
```

`NOT`

```sql
1010 1010
```

```sql
0101 0101
```
