---
title: "AUTO Mode Heuristics in Shaping Returned XML"
topic: "xml-data"
description: "AUTO mode determines the shape of returned XML based on the query. In determining how elemen"
tags: ["xml-data","auto-mode-heuristics-in-shaping-returned-xml"]
pubDate: 2025-12-01
---

AUTO mode determines the shape of returned XML based on the query. In determining how

elements are to be nested, AUTO mode heuristics compare column values in adjacent rows.

Columns of all types, except

,

,

, and

, are compared. Columns of type

and

are compared.

The following example illustrates the AUTO mode heuristics that determine the shape of the

resulting XML:

To determine where a new

element starts, all column values of T1, except

,

,

and

, are compared if the key on the table T1 isn't specified. Next, assume that the

column is

and the SELECT statement returns this rowset:

Output

The AUTO mode heuristics compare all the values of table T1, the Id, and Name columns. The

first two rows have the same values for the

and

columns. As a result, a single

element, having two

child elements, is added to the result.

Following is the XML that is returned:

XML

```sql
<T1>
Id
Name
<T1>
<T2>
SELECT
T1.Id, T2.Id, T1.Name
FROM
T1, T2
WHERE
Col1 = 1
/* actual predicate goes here*/
ORDER
BY
T1.Id
FOR
XML
AUTO
;
T1.Id T1.Name T2.Id
-----------------------
1 Andrew 2
1 Andrew 3
1 Nancy 4
<T1
Id
=
"1"
Name
=
"Andrew"
>
<T2
Id
=
"2"
/>
<T2
Id
=
"3"
/>
</T1>
```
