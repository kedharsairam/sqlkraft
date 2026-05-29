---
name: "xquery-primary-expressions"
title: "XQuery - Primary Expressions"
category: "xquery"
description: "XQuery Language Reference: Primary Expressions"
syntax: "&lt;"
tags:
  - "xquery"
  - "primary-expressions"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

The XQuery primary expressions include literals, variable references, context item expressions,

constructors, and function calls.

XQuery literals can be numeric or string literals. A string literal can include predefined entity

references, and an entity reference is a sequence of characters. The sequence starts with an

ampersand that represents a single character that otherwise might have syntactic significance.

Following are the predefined entity references for XQuery.

<

>

&

"

'

A string literal can also contain a character reference, an XML-style reference to a Unicode

character, that is identified by its decimal or hexadecimal code point. For example, the Euro

symbol can be represented by the character reference, "&#8364;".

The following examples illustrate the use of literals and also entity and character references.

This code returns an error, because the

and

characters have special meaning.

ﾉ

Expand table

７

Note

SQL Server uses XML version 1.0 as the basis for parsing.

```sql
&lt;
&gt;
&amp;
&quot;
&apos;
<'
'>
```
