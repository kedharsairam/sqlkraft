---
title: "Change Existing Columns"
topic: "xml-data"
description: "The ALTER TABLE statement supports the data type."
tags: ["xml-data","change-existing-columns"]
pubDate: "2025-12-01"
---

The ALTER TABLE statement supports the

data type. For example, you can alter any string

type column to the

data type. In these cases, the documents contained in the column must

be well formed. Also, if you're changing the type of the column from string to typed xml, the

documents in the column are validated against the specified XSD schemas.

You can change an

type column from untyped XML to typed XML. For example:

In the previous example, all the instances stored in the column are validated and typed against

the XSD schemas in the specified collection. If the column contains one or more XML instances

that are invalid regarding the specified schema, the

statement will fail and you

won't be able to change your untyped XML column into typed XML.

７

Note

The script will run against

database, because the XML schema

collection,

, is created as part of the

database.

```sql
ALTER TABLE
CREATE
TABLE
T (Col1 int primary key
, Col2 nvarchar (
max
));
GO
INSERT
INTO
T
VALUES (1,
'<Root><Product ProductID="1"/></Root>'
);
GO
ALTER
TABLE
T
ALTER
COLUMN
Col2 xml
;
CREATE
TABLE
T (Col1 int primary key
, Col2 xml
);
GO
INSERT
INTO
T values (1,
'<p1:ProductDescription ProductModelID="1"
xmlns:p1="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelDescription">
</p1:ProductDescription>'
);
GO
-- Make it a typed xml column by specifying a schema collection.
ALTER
TABLE
T
ALTER
COLUMN
Col2 xml (Production.ProductDescriptionSchemaCollection);
AdventureWorks2025
Production.ProductDescriptionSchemaCollection
AdventureWorks2025
```
