---
name: "Singleton checks"
title: "Singleton checks"
category: "statements"
description: "When reporting errors,"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Example: Known singleton

When reporting errors,

data type methods raise a single error in the following format:

For example:

Location steps, function parameters, and operators that require singletons will return an error if

the compiler can't determine whether a singleton is guaranteed at run time. This problem

occurs frequently with untyped data. For example, the lookup of an attribute requires a

singleton parent element. An ordinal that selects a single parent node is sufficient. The

evaluation of a

-

combination to extract attribute values might not require the

ordinal specification. This is shown in the next example.

In this example, the

method generates a separate row for each

element. The

method that is evaluated on a

node extracts the value of

and, being an

attribute, is a singleton.

７

Note

Parsing errors raised by the XQuery parser (such as syntax errors in the XML referenced as

part of the XML data type method, for example), abort the active transaction, regardless of

the

setting of the current session.

### value()

## Example: Using value()

XML schema is used for type checking of typed XML. If a node is specified as a singleton in the

XML schema, the compiler uses that information and no error occurs. Otherwise, an ordinal

that selects a single node is required. In particular, the use of descendant-or-self axis (//) axis,

such as in

, loses singleton cardinality inference for the

element, even if

the XML schema specifies it to be so. Therefore, you should rewrite it as

.

It's important to remain aware of the difference between

and

for type checking. The former returns a sequence of

nodes in which each

node is the leftmost

node among its siblings. The latter returns the first singleton

node in document order in the XML instance.

The following query on an untyped XML column results in a static, compilation error. This is

because

expects a singleton node as the first argument and the compiler can't

determine whether only one

node will occur at run time:

Following is a solution that you could consider:

However, this solution doesn't solve the error, because multiple

nodes might occur in

each XML instance. The following rewrite works:

This query returns the value of the first

element in each XML instance.

xml Data Type Methods

Related content

```sql
<book>
```

```sql
<book>
```

```sql
@genre
```

```sql
Msg errorNumber, Level levelNumber, State stateNumber:
XQuery [database.table.method]: description_of_error
Msg 2396, Level 16, State 1:
XQuery [xmldb_test.xmlcol.query()]: Attribute may not appear outside of an element
```

```sql
SELECT nref.value(
'@genre'
,
'VARCHAR(max)'
) LastName
FROM
T
CROSS
APPLY xCol.nodes(
'//book'
)
AS
R(nref)
```

```sql
/book//title
```

```sql
<title>
```

```sql
(/book//title)[1]
```

```sql
//first-name[1]
```

```sql
(//first-name)
[1]
```

```sql
<first-name>
```

```sql
<first-name>
```

```sql
<first-name>
```

```sql
<last-name>
```

```sql
<author>
```

```sql
<last-name>
```

```sql
SELECT xCol.value(
'//author/last-name'
,
'NVARCHAR(50)'
) LastName
FROM
T
SELECT xCol.value(
'//author/last-name[1]'
,
'NVARCHAR(50)'
) LastName
FROM
T
SELECT xCol.value(
'(//author/last-name/text())[1]'
,
'NVARCHAR(50)'
) LastName
FROM
T
```
