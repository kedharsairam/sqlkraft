---
name: "Unicode strings"
title: "Unicode strings"
category: "data-types"
description: "The following are examples of character strings:"
tags: ["tsql","data-types"]
pubDate: 2026-05-29
---

## nvarchar(max)

The following are examples of character strings:

text

Empty strings are represented as two single quotation marks with nothing in between. In 6.x

compatibility mode, an empty string is treated as a single space.

Character string constants support enhanced

collations.

Unicode strings have a format similar to character strings, but are prefixed with an

identifier

(N stands for National Language in the SQL-92 standard).

For example,

is a character constant while

is a Unicode constant. Unicode

constants are interpreted as Unicode data, and aren't evaluated by using a code page. Unicode

constants do have a collation. This collation primarily controls comparisons and case sensitivity.

Unicode constants are assigned the default collation of the current database. If the COLLATE

clause is used, the conversion to the database default collation still happens before the

conversion to the collation specified by the COLLATE clause. For more information, see

Collation and Unicode Support.

Unicode string constants support enhanced collations.

７

Note

Character constants greater than 8000 bytes are typed as

data.

）

Important

The

prefix must be uppercase.

７

Note

Unicode constants greater than 8000 bytes are typed as

data.

```sql
N
```

```sql
'Michél'
```

```sql
N'Michél'
```

```sql
'Cincinnati'
'O''Brien'
'Process X is 50% complete.'
'The level for job_id: %d should be between %d and %d.'
"O'Brien"
```

```sql
N
```
