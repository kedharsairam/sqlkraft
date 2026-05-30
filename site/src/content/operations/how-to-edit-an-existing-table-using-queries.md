---
title: "How to: Edit an Existing Table using Queries"
topic: "ssb-diagnose"
description: |
  09/10/2025

  You can edit the definition of a table or its data by writing a Transact-SQL query. To view or

  enter data in a table visually, use the Data Editor as described in

  Connected Database

  Dev
tags:
  - "ssb-diagnose"
  - "how-to-edit-an-existing-table-using-queries"
pubDate: 2025-12-01
---

09/10/2025

You can edit the definition of a table or its data by writing a Transact-SQL query. To view or

enter data in a table visually, use the Data Editor as described in

Connected Database

Development

.

1. Expand the

node of the

database in

SQL Server Object Explorer

, and right-

click

.

2. Select

to view the table schema in the Table Designer.

3. Check the

box for the

column. The corresponding code in the script

pane is changed to

immediately.

4. Update the database following the steps in the

How to: Update a connected database

with Power Buffer

article.

1. Right-click the

database node and select

.

2. In the script pane, paste in the following code.

3. Select the

button to run this query. The following in the

pane

indicate that the rows are successfully added to the tables.

```cmd
Trade
Address
NULL
Trade
INSERT
INTO dbo.Suppliers
VALUES (1,
'NorthWind Traders'
,
'Seattle, WA'
),
(2,
'Contoso'
,
'Tacoma, WA'
);
GO
INSERT dbo.Customer
VALUES (1,
'Fourth Coffee'
);
GO
INSERT dbo.Products
VALUES (1,
'Apples'
, 0, 1, 1),
(2,
'Instant Coffee'
, 1, 2, 1);
GO
```
