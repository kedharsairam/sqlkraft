---
name: "Supplementary characters (surrogate pairs)"
title: "Supplementary characters (surrogate pairs)"
category: "statements"
description: "A positive integer or"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

A positive integer or

expression that specifies how many characters of the

expression

are

returned. If

length

is negative, an error is generated and the statement is terminated. If the sum

of

start

and

length

is greater than the number of characters in

expression

, the whole value

expression beginning at

start

is returned. If

length

is omitted, all characters from the start

position to the end of the expression is returned.

You can use substring with an optional

length

argument. However, if you use

for

length

,

## returns

. Review

E. Use SUBSTRING with optional length argument

for an

example.

## Returns character data if

expression

is one of the supported character data types. Returns

binary data if

expression

is one of the supported

data types. The returned string is the

same type as the specified expression with the exceptions shown in the following table.

/

/

/

/

/

/

You must specify the values for

start

and

length

in number of characters for

,

, or

data types. For

,

,

, or

data types, you must specify these

values in bytes.

The

expression

must be

or

when the

start

or

length

contains a

value larger than 2,147,483,647.

When you use supplementary character (SC) collations, both

start

and

length

count each

surrogate pair in

expression

as a single character. For more information, see

Collation and

Unicode support

.

ﾉ

Expand table

#### name

#### Initial

#### ThirdAndFourthCharacters

```sql
NULL
```

```sql
SUBSTRING
```

```sql
NULL
```
