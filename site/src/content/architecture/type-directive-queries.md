---
title: "TYPE directive queries"
topic: "xml-data"
description: |
  Article
  
  •
  
  08/10/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL Server support for the
  
  xml (Transact-SQL)
  
  data type enables you to optionally request that
  
  the r
tags:
  - "xml-data"
  - "type-directive-queries"
pubDate: 2025-12-01
---

Article

•

08/10/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL Server support for the

xml (Transact-SQL)

data type enables you to optionally request that

the result of a FOR XML query be returned as

by specifying the TYPE directive. This allows

you to process the result of a FOR XML query on the server. For example, you can specify an

XQuery against it, assign the result to an

type variable, or write

Nested FOR XML queries

.

The following examples illustrate the use of the TYPE directive with FOR XML queries.

The following query retrieves customer contact information from the

table. Because

the

directive is specified in

, the result is returned as

type.

SQL

This is the partial result:

XML

７

Note

SQL Server returns

data type instance data to the client as a result of different server-

constructs such as FOR XML queries that use the TYPE directive, or where the

data

type is used to return XML instance data values from SQL table columns and output

parameters. In client application code, the ADO.NET provider requests this

data type

information to be sent in a binary encoding from the server. However, if you are using

FOR XML without the TYPE directive, the XML data comes back as a string type. In any

case, the client provider will always be able to handle either form of XML. Note that top-

level FOR XML without the TYPE directive cannot be used with cursors.

```sql
Contacts
TYPE
FOR XML
USE
AdventureWorks2022;
Go
SELECT
BusinessEntityID, FirstName, LastName
FROM
Person.Person
ORDER
BY
BusinessEntityID
FOR
XML
AUTO
,
TYPE
;
```