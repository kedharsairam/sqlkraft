---
title: "Use in Applications"
topic: "xml-data"
description: |
  Article

  •

  08/10/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  This article describes the options that are available to you for working with the

  data type in

  your a
tags:
  - "xml-data"
  - "use-in-applications"
pubDate: 2025-12-01
---

Article

•

08/10/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This article describes the options that are available to you for working with the

data type in

your application. The article includes information about the following:

Handling XML from an

type column by using ADO and SQL Server Native Client

Handling XML from an

type column by using ADO.NET

Handling

type in parameters by using ADO.NET

To use MDAC components to access the types and features that were introduced in SQL Server

2005 (9.x), you must set the DataTypeCompatibility initialization property in the ADO

connection string.

For example, the following Visual Basic Scripting Edition (VBScript) sample shows the results of

querying an

data type column,

, in the

table of the

sample database. Specifically, the query looks for the instance value of this

column for the row where the

is equal to.

VB

```sql
Demographics
Sales.Store
AdventureWorks2022
CustomerID
3
Const
DS =
"MyServer"
Const
DB =
"AdventureWorks2022"
Set objConn = CreateObject(
"ADODB.Connection"
)
Set objRs = CreateObject(
"ADODB.Recordset"
)
CommandText =
"SELECT Demographics"
& _
" FROM Sales.Store"
& _
" INNER JOIN Sales.Customer"
& _
" ON Sales.Store.BusinessEntityID = sales.customer.StoreID"
& _
" WHERE Sales.Customer.CustomerID = 3"
& _
" OR Sales.Customer.CustomerID = 4"
ConnectionString =
"Provider=MSOLEDBSQL"
& _
";Data Source="
& DS & _
";Initial Catalog="
& DB & _
";Integrated Security=SSPI;"
& _
"DataTypeCompatibility=80"
```
