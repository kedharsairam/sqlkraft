---
title: "Generate Elements for NULL Values with the XSINIL Parameter"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The

  directive constructs XML in which each column value maps to an element in the

  XML. By d
tags:
  - "xml-data"
  - "generate-elements-for-null-values-with-the-xsinil-parameter"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The

directive constructs XML in which each column value maps to an element in the

XML. By default, if the column value is NULL, no element is added. But by specifying the

optional

parameter on the ELEMENTS directive, you can request that an element is

created for the NULL value. In this case, an element that has the

attribute set to TRUE is

returned for each NULL column value.

Use RAW Mode with FOR XML

SELECT - FOR clause
