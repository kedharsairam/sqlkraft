---
title: "Use results in application code"
topic: "xml-data"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  By using FOR XML clauses with SQL queries, you can retrieve and cast query results as XML
  
  da
tags:
  - "xml-data"
  - "use-results-in-application-code"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

By using FOR XML clauses with SQL queries, you can retrieve and cast query results as XML

data. When you use FOR XML query results in XML application code, you can:

Query SQL tables for instances of

XML Data (SQL Server)

values

Apply the

TYPE Directive in FOR XML Queries

to return the result of queries that contain

text or image typed data as XML

This article provides examples that demonstrate these approaches.

The ADO

object or other objects that support the COM

interface, such as the

Active Server Pages (ASP)

and

objects, can contain the results when you're

working with FOR XML queries.

For example, the following ASP code shows the results of querying an

data type column,

Demographics, in the

table of the AdventureWorks sample database. Specifically,

the query looks for the instance value of this column for the row where the CustomerID is

equal to 3.

```sql
Sales.Store
<!-- BeginRecordAndStreamVBS -->
<%@ LANGUAGE = VBScript %>
<!-- %
Option
Explicit
% -->
<!--
'Request.ServerVariables("SERVER_NAME") & ";" & _ -->
<HTML>
<HEAD>
<META NAME=
"GENERATOR"
Content=
"Microsoft Developer Studio"
/>
<META HTTP-EQUIV=
"Content-Type"
content=
"text/html"
; charset=
"iso-8859-1"
>
<TITLE>
FOR
XML Query Example</TITLE>
<STYLE>
BODY
{
FONT-FAMILY: Tahoma;
FONT-SIZE: 8pt;
OVERFLOW: auto
}
H3
{
```