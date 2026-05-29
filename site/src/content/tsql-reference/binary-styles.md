---
name: "Binary styles"
title: "Binary styles"
category: "data-types"
description: "No commas every three digits to the left of the decimal point, and four digits to the right of"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

No commas every three digits to the left of the decimal point, and four digits to the right of

the decimal point

Example: 4235.9819.

Equivalent to style 2, when converting to

or

For an

expression

,

style

can have one of the values shown in the following table. Other

values are processed as 0.

(default)

Use default parsing behavior that discards insignificant white space, and doesn't allow for an

internal DTD subset.

Note:

When converting to the

data type, SQL Server insignificant white space is handled

differently than in XML 1.0. For more information, see

Create Instances of XML Data

.

Preserve insignificant white space. This style setting sets the default

handling to

match the behavior of

.

Enable limited internal DTD subset processing.

If enabled, the server can use the following information that is provided in an internal DTD

subset, to perform nonvalidating parse operations.

- Defaults for attributes are applied

- Internal entity references are resolved and expanded

- The DTD content model is checked for syntactical correctness

The parser ignores external DTD subsets. Also, it doesn't evaluate the XML declaration to see

whether the

standalone

attribute has a

or

value. Instead, it parses the XML instance as

a stand-alone document.

Preserve insignificant white space, and enable limited internal DTD subset processing.

For a

,

,

, or

expression

,

style

can have one of the values

shown in the following table. Style values not listed in the table will return an error.

ﾉ

Expand table

#### Value

#### Output

#### 0

#### 1

#### 2

### bigint

### xml

```sql
xml:space
```

```sql
xml:space="preserve"
```
