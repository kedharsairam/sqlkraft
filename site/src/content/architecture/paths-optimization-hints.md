---
title: "Paths & optimization hints"
topic: "xml-data"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  This article describes how to specify node paths to index and optimization hints for indexing
  
  when you
tags:
  - "xml-data"
  - "paths-optimization-hints"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This article describes how to specify node paths to index and optimization hints for indexing

when you create or alter selective XML indexes.

You specify node paths and optimization hints at the same time in one of the following

statements:

In the

clause of a

statement. For more information, see

CREATE SELECTIVE

XML INDEX (Transact-SQL)

.

In the

clause of an

statement. For more information, see

ALTER INDEX

(Selective XML Indexes)

.

For more information about selective XML indexes, see

Selective XML Indexes (SXI)

.

Selective XML indexes support two type systems: XQuery types and SQL Server types. The

indexed path can be used either to match an XQuery expression, or to match the return type of

the

method of the

data type.

When a path to index isn't annotated, or is annotated with the XQUERY keyword, the path

matches an XQuery expression. There are two variations for XQUERY-annotated node

paths:

If you don't specify the XQUERY keyword and the XQuery data type, then default

mappings are used. Typically performance and storage aren't optimal.

If you specify the XQUERY keyword and the XQuery data type, and optionally other

optimization hints, then you can achieve the best possible performance and the most

efficient possible storage. However, a cast can fail.

When a path to index is annotated with the SQL keyword, the path matches the return

type of the

method of the

data type. Specify the appropriate SQL Server

data type, which is the return type that you expect from the

method.

```sql
value()
value()
value()
```