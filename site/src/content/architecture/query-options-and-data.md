---
title: "Query options and data"
topic: "xml-data"
description: |
  Article

  •

  03/17/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  This article describes the query options that you have to specify to query XML data. It also

  describes
tags:
  - "xml-data"
  - "query-options-and-data"
pubDate: 2025-12-01
---

Article

•

03/17/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This article describes the query options that you have to specify to query XML data. It also

describes the parts of XML instances that aren't preserved when they're stored in databases.

When you query

type columns or variables using

data type methods, the following

options must be set as shown.

ANSI_NULLS

ON

ANSI_PADDING

ON

ANSI_WARNINGS

ON

ARITHABORT

ON

CONCAT_NULL_YIELDS_NULL

ON

NUMERIC_ROUNDABORT

OFF

QUOTED_IDENTIFIER

ON

If the options aren't set as shown, queries and modifications on

data type methods will fail.

preserves the content of the XML instance, but doesn't preserve aspects of the XML

instance that aren't considered significant in the XML data model. This means that a retrieved

XML instance might not be identical to the instance that was stored in the server, but will

contain the same information.

The XML declaration in an instance isn't preserved when the instance is stored in the database.

For example:

ﾉ

Expand table
