---
title: "Validate, Query, & Change"
topic: "json-data"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  The built-in support for JSON in the SQL Database Engine incl
tags:
  - "json-data"
  - "validate-query-change"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

The built-in support for JSON in the SQL Database Engine includes the following functions:

ISJSON

tests whether a string contains valid JSON.

JSON_VALUE

extracts a scalar value from a JSON string.

JSON_QUERY

extracts an object or an array from a JSON string.

JSON_MODIFY

updates the value of a property in a JSON string and returns the updated

JSON string.

For all JSON functions, review

JSON functions (Transact-SQL).

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

The examples on this page use the JSON text similar to the content shown in the following

example:

JSON

```sql
AdventureWorks2025
AdventureWorksDW2025
{
"id"
:
"DesaiFamily"
,
"parents"
: [
{
"familyName"
:
"Desai"
,
"givenName"
:
"Prashanth"
},
{
"familyName"
:
"Miller"
,
"givenName"
:
"Helen"
}
],
"children"
: [
{
"familyName"
:
"Desai"
,
"givenName"
:
"Jesse"
,
"gender"
:
"female"
,
"grade"
: 1,
"pets"
: [
{
"givenName"
:
"Goofy"
},
{
"givenName"
:
"Shadow"
}
]
},
{
"familyName"
:
"Desai"
,
"givenName"
:
"Lisa"
,
```
