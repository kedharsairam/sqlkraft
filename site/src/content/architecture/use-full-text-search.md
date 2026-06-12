---
title: "Use Full-Text Search"
topic: "xml-data"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  You can create a full-text index on XML columns that indexes the content of the XML values,

  but ignore
tags:
  - "xml-data"
  - "use-full-text-search"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

You can create a full-text index on XML columns that indexes the content of the XML values,

but ignores the XML markup. Element tags are used as token boundaries. The following items

are indexed:

The content of XML elements.

The content of XML attributes of the top-level element only, unless those values are

numeric values.

When possible, you can combine full-text search with XML index in the following way:

1. First, filter the XML values of interest by using SQL full-text search.

2. Next, query those XML values that use XML index on the XML column.

After the full-text index has been created on the XML column, the following query checks that

an XML value contains the word "custom" in the title of a book:

The

method uses the full-text index to subset the XML values that contain the word

"custom" anywhere in the document. The

clause ensures that the word "custom"

occurs in the title of a book.

A full-text search that uses

and XQuery

has different semantics. The

latter is a substring match and the former is a token match that uses stemming. Therefore, if

the search is for the string that has "run" in the title, the matches will include "run", "runs", and

"running", because both the full-text

and the XQuery

are satisfied.

However, the query doesn't match the word "customizable" in the title in that the full-text

```sql
contains() exist() contains() contains() contains() contains()
SELECT
*
FROM
T
WHERE
CONTAINS(xCol,
'custom'
)
AND xCol.exist(
'/book/title/text()[contains(.,"custom")]'
) = 1;
```
