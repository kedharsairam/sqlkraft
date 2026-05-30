---
name: "xquery-string-search-in-xquery"
title: "XQuery - String Search in XQuery"
category: "xquery"
description: "XQuery Language Reference: String Search in XQuery"
syntax: "where"
tags:
  - "xquery"
  - "string-search-in-xquery"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

This topic provides sample queries that show how to search text in XML documents.

In the previous query, the

in the FLOWR expression filters the result of the

expression and returns only elements that satisfy the

condition.

This is the result:

XML Data (SQL Server)

XQuery Language Reference (SQL Server)

```sql
where for
SELECT CatalogDescription.query('
declare namespace p1="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelDescription";
for $f in /p1:ProductDescription/p1:Features/*
where contains(string($f), "maintenance") return
$f ') as Result
FROM Production.ProductModel
WHERE ProductModelID=19
<p1:Maintenance xmlns:p1="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelWarrAndMain">
<p1:NoOfYears>10</p1:NoOfYears>
<p1:Description>maintenance contact available through your dealer or any AdventureWorks retail store.</p1:Description>
</p1:Maintenance>
```
