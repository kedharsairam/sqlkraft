---
title: "Store documents"
topic: "json-data"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The SQL Database Engine provides native JSON functions that e
tags:
  - "json-data"
  - "store-documents"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

The SQL Database Engine provides native JSON functions that enable you to parse JSON

documents using standard SQL language. You can store JSON documents in the SQL Database

Engine and query JSON data as in a NoSQL database. This article describes the options for

storing JSON documents.

The first storage design decision is how to store JSON documents in the tables. There are two

available options:

- JSON documents can be stored as-is in columns with the data type

or

. This is the best way for quick data load and ingestion because the loading

speed matches the loading speed of string columns. This approach might introduce an

additional performance penalty on query/analysis time if indexing on JSON values is not

performed, because the raw JSON documents must be parsed while the queries are

running.

- JSON documents can be parsed while they are inserted in the table

using

,

or

functions. Fragments from the input JSON

documents can be stored in the columns containing JSON sub-elements with data types

or

. This approach increases the load time because JSON parsing is done

during load; however, queries match the performance of classic queries on the relational

data.

Currently in SQL Server, JSON is not a built-in data type.

７

Note

The

:

is generally available for Azure SQL Database and Azure SQL Managed Instance with

the

SQL Server 2025

or

.

is in preview for SQL Server 2025 (17.x) and SQL database in Fabric.

```sql
OPENJSON
JSON_VALUE
JSON_QUERY
```