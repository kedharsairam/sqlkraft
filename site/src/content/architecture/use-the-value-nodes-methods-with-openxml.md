---
title: "Use the value() & nodes() Methods with OPENXML"
topic: "xml-data"
description: "You can use multiple methods on data type in a clause to generate a rowset of extracted values. The"
tags: ["xml-data","use-the-value-nodes-methods-with-openxml"]
pubDate: "2025-12-01"
---

You can use multiple

methods on

data type in a

clause to generate a

rowset of extracted values. The

method yields an internal reference for each selected

node that can be used for additional query. The combination of the

and

methods can be more efficient in generating the rowset when it has several columns and,

perhaps, when the path expressions used in its generation are complex.

The

method yields instances of a special

data type, each of which has its context

set to a different selected node. This kind of XML instance supports

,

,

,

and

methods and can be used in

aggregations. All other uses cause an error.

Assume that you want to extract the first and last names of authors, and the first name isn't

"David". Additionally, you want to extract this information as a rowset that contains two

columns, FirstName and LastName. By using

and

methods, you can

accomplish this as shown in the following:

In this example,

yields a rowset of references to

elements for each

XML instance. The first and last names of authors are obtained by evaluating

methods

relative to those references.

2000 provides the capability for generating a rowset from an XML instance by using. You can specify the relational schema for the rowset and how values inside the

XML instance map to columns in the rowset.

```sql
value() nodes() nodes() value() nodes() query() value() nodes() exist() count(*) nodes() value() nodes('//author')
<author>
value()
SELECT nref.value(
'(first-name/text())[1]'
,
'nvarchar(50)'
) FirstName,
nref.value(
'(last-name/text())[1]'
,
'nvarchar(50)'
) LastName
FROM
T
CROSS
APPLY xCol.nodes(
'//author'
)
AS
R(nref)
WHERE nref.exist(
'first-name[. != "David"]'
) = 1;
```
