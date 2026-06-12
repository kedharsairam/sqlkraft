---
name: "sys.selective_xml_index_paths"
title: "sys.selective_xml_index_paths"
category: "indexes"
description: "Available beginning in SQL Server 2012 (11.x) Service Pack 1, each row in sys.selective_xml_index_paths represents one promoted path for particular selective xml index. If you create a selective xml index on xmlcol of table T using following statement, There will be two new rows in sys.selective_xml_index_paths corresponding to the index sxi1. Unique id of the selective xml index. Promoted path. F"
tags: ["indexes","catalog-view"]
pubDate: 2026-05-29
syntax: |
  CREATE
              SELECTIVE
              XML
              INDEX
              sxi1
              ON
              T(xmlcol)
              FOR
              ( path1 =
              '/a/b/c'
              AS
              XQUERY
              'xs:string'
              ,
              path2 =
              '/a/b/d'
              AS
              XQUERY
              'xs:double'
              )
---

## Description

Available beginning in SQL Server 2012 (11.x) Service Pack 1, each row in sys.selective_xml_index_paths represents one promoted path for particular selective xml index. If you create a selective xml index on xmlcol of table T using following statement, There will be two new rows in sys.selective_xml_index_paths corresponding to the index sxi1. Unique id of the selective xml index. Promoted path. For example, '/a/b/c/d/e'.

## Syntax

```sql
CREATE
SELECTIVE
XML
INDEX sxi1
ON
T(xmlcol)
FOR ( path1 =
'/a/b/c'
AS
XQUERY
'xs:string'
,
path2 =
'/a/b/d'
AS
XQUERY
'xs:double'
)
```
