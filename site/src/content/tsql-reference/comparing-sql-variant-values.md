---
name: "Comparing sql_variant Values"
title: "Comparing sql_variant Values"
category: "queries"
description: "ODBC does not fully support"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

ODBC does not fully support

sql_variant. Therefore, queries of sql_variant columns are returned as binary data when you use Microsoft OLE DB Provider for ODBC (MSDASQL). For example, a sql_variant column that contains the character string data 'PS2091' is returned as
0x505332303931.

The

sql_variant

data type belongs to the top of the data type hierarchy list for conversion. For sql_variant comparisons, the SQL Server data type hierarchy order is grouped into data type families.

sql_variant

sql_variant

Date and time

Date and time

Date and time

Date and time

Date and time

Date and time

Approximate numeric

Approximate numeric

Exact numeric

Exact numeric

Exact numeric

Exact numeric

Exact numeric

Exact numeric

Exact numeric

Exact numeric

Data type hierarchy

Data type family

nvarchar

nchar

varchar

char

varbinary

binary

uniqueidentifier

char

varchar

nchar

nvarchar

datetimeoffset

geography

geometry
