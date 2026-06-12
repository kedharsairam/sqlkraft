---
title: "Namespace Support in PATH Mode"
topic: "xml-data"
description: "Namespace support in the PATH mode is provided by using WITH NAMESPACES."
tags: ["xml-data","namespace-support-in-path-mode"]
pubDate: "2025-12-01"
---

Namespace support in the PATH mode is provided by using WITH NAMESPACES. For example,

the following query demonstrates the WITH NAMESPACES syntax to declare a namespace ("a:")

that can then be used in the subsequent SELECT statement:

These samples illustrate the use of PATH mode in generating XML from a SELECT query. Many

of these queries are specified against the bicycle manufacturing instructions XML documents

that are stored in the Instructions column of the ProductModel table.

Use PATH Mode with FOR XML

```sql
WITH
XMLNAMESPACES (
'a'
as a)
SELECT
1 as
'a:b'
FOR
XML
PATH
;
```
