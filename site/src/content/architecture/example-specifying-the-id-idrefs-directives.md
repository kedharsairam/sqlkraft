---
title: "Example: Specifying the ID & IDREFS Directives"
topic: "xml-data"
description: ""
tags: ["xml-data","example-specifying-the-id-idrefs-directives"]
pubDate: "2025-12-01"
---

An element attribute can be specified as an

type attribute, and the

attribute can

then be used to refer to it. This enables intra-document links and is similar to the primary key

and foreign key relationships in relational databases.

This example illustrates how the

and

directives can be used to create attributes of

and

types. Because IDs can't be integer values, the ID values in this example are

converted. In other words, they're type casted. Prefixes are used for the ID values.

Assume that you want to construct XML as shown in the following:

XML

The

attribute of the

element is a multivalued attribute that refers

to the

attribute of the

element. To establish this link, the

attribute must be declared of

type, and the

attribute of the

element must be declared of

type. Because a customer can request several

orders, the

type is used.

Elements of

type also have more than one value. Therefore, you have to use a separate

select clause that will reuse the same tag, parent, and key column information. The

then has to ensure that the sequence of rows that make up the

values appears

grouped together under their parent element.

This is the query that produces the XML you want. The query uses the

and

directives

to overwrite the types in the column names (

,

).

```sql
SalesOrderIDList
<Customer>
SalesOrderID
<SalesOrder>
SalesOrderID
ID
SalesOrderIDList
<Customer>
IDREFS
IDREFS
ORDER BY
ID
IDREFS
SalesOrder!2!SalesOrderID!ID
Customer!1!SalesOrderIDList!IDREFS
<Customer
CustomerID
=
"C1"
SalesOrderIDList
=
" O11 O22 O33."
>
<SalesOrder
SalesOrderID
=
"O11"
OrderDate
=
"."
/>
<SalesOrder
SalesOrderID
=
"O22"
OrderDate
=
"."
/>
<SalesOrder
SalesOrderID
=
"O33"
OrderDate
=
"."
/>.
</Customer>
USE
AdventureWorks2022;
GO
```
