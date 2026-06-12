---
name: "Bit manipulation functions"
title: "Bit manipulation functions"
category: "data-types"
description: "2022 (16.x)"
tags: ["tsql","data-types"]
pubDate: 2026-05-29
---

2022 (16.x)

Azure SQL Managed

Instance

Bit manipulation functions such as moving, retrieving (getting), setting, or counting single bits

within an integer or binary value, allow you to process and store data more efficiently than with

individual bits.

A

bit

has two values (

or

, which represent

or

, or

or

). A

byte

is made up

of a sequence of 8 bits. Bit manipulation functions in SQL Server treat the "leftmost" bit in a

byte as the biggest (the most significant). To the bit manipulation functions, bits are numbered

from right to left, with bit

being the rightmost and the smallest and bit

being the leftmost

and largest.

For example, a binary sequence of

is the decimal equivalent of the number. You

can calculate this out using powers of 2 as follows:

00000111 = (2^2 + 2^1 + 2^0 = 4 + 2 + 1 = 7)

What this means in practice is that while SQL Server stores this value as

(byte-

reversed), the bit manipulation functions will treat it as though it's.

When looking at multiple bytes, the first byte (reading left to right) is the biggest.

You can use the following images to visualize how SQL Server's bit manipulation functions

interpret bit and byte expression values and bit offsets.

## binary(

## n

## )

## varbinary(

## n

## )

```sql
1
```

```sql
0
```

`on`

`off`

`true`

`false`

```sql
0
```

```sql
7
```

```sql
00000111
```

```sql
7
```

```sql
11100000
```

```sql
00000111
```
