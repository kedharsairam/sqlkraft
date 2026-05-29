---
title: "Create Variables & Columns"
topic: "xml-data"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The

  data type is a built-in data type in SQL Server and is somewhat similar to other built-in

  types s
tags:
  - "xml-data"
  - "create-variables-columns"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The

data type is a built-in data type in SQL Server and is somewhat similar to other built-in

types such as

and

. As with other built-in types, you can use the

data type as a

column type when you create a table as a variable type, a parameter type, a function-return

type, or in

CAST and CONVERT

.

To create an

type column as part of a table, use a

statement, as shown in the

following example:

SQL

You can use a

to create a variable of

type, as the following example

shows.

SQL

Create a typed

variable by specifying an XML schema collection, as shown in the following

example.

SQL

To pass an

type parameter to a stored procedure, use a

statement, as

shown in the following example.

SQL

```sql
xml
CREATE TABLE
DECLARE statement
xml
xml
xml
CREATE PROCEDURE
CREATE
TABLE
T1(Col1
int
primary
key
, Col2
xml
);
DECLARE
@x
xml
;
DECLARE
@x
xml
(Sales.StoreSurveySchemaCollection)
CREATE
PROCEDURE
SampleProc(@XmlDoc
xml
)
AS
...
```
