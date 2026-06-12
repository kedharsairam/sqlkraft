---
title: "Frequently used values with computed columns"
topic: "xml-data"
description: "If queries are made principally on a few element and attribute values, you may want to promote those q"
tags: ["xml-data","frequently-used-values-with-computed-columns"]
pubDate: "2025-12-01"
---

If queries are made principally on a few element and attribute values, you may want to

promote those quantities into relational columns. This is helpful when queries are issued on a

small part of the XML data while the whole XML instance is retrieved. Creating an XML index on

the XML column is not required. Instead, the promoted column can be indexed. Queries must

be written to use the promoted column. That is, the query optimizer doesn't target again the

queries on the XML column to the promoted column.

The promoted column can be a computed column in the same table or it can be a separate,

user-maintained column in a table. This is sufficient when singleton values are promoted from

each XML instance. However, for multi-valued properties, you have to create a separate table

for the property, as described in the following section.

A computed column can be created by using a user-defined function that invokes

data

type methods. The type of the computed column can be any SQL type, including XML. This is

illustrated in the following example.

Create the user-defined function for a book ISBN number:

Add a computed column to the table for the ISBN:

```sql
CREATE
FUNCTION udf_get_book_ISBN (@xData xml
)
RETURNS varchar (20)
BEGIN
DECLARE
@ISBN varchar (20)
SELECT
@ISBN = @xData.value(
'/book[1]/@ISBN'
,
'varchar(20)'
)
RETURN
@ISBN
END
;
```
