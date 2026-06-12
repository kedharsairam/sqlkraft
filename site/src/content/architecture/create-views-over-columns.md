---
title: "Create Views over Columns"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  You can use an

  type column to create views. The following example creates a view in which

  t
tags:
  - "xml-data"
  - "create-views-over-columns"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

You can use an

type column to create views. The following example creates a view in which

the value from an

type column is retrieved using the

method of the

data

type.

Execute the following query against the view:

This is the result:

Output

Note the following points about using the

data type to create views:

The

data type can be created in a materialized view. The materialized view can't be

based on an

data type method. However, it can be cast to an XML schema collection

```sql
xml value()
-- Create the table.
CREATE
TABLE
T (
ProductID
INT
PRIMARY
KEY
,
CatalogDescription
XML
);
GO
-- Insert sample data.
INSERT
INTO
T
VALUES (1,
'<ProductDescription ProductID="1" ProductName="SomeName"
/>'
);
GO
-- Create view (note the value() method used to retrieve ProductName
-- attribute value from the XML).
CREATE
VIEW
MyView
AS
SELECT
ProductID,
CatalogDescription.value(
'(/ProductDescription/@ProductName)[1]'
,
'varchar(40)'
)
AS
PName
FROM
T;
GO
SELECT
*
FROM
MyView;
ProductID PName
----------- ------------
1 SomeName
```
