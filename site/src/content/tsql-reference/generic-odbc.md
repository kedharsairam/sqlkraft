---
name: "Generic ODBC"
title: "Generic ODBC"
category: "statements"
description: "Make sure to configure the driver to sample all the necessary data."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Key name

Default

Required

## Description

Make sure to configure the driver to sample all the necessary data.

Documents that aren't sampled don't get included in the schema

definition, and thus don't become available in ODBC applications.

Typically, sampling a large number of documents results in a schema

data in the database. However, the sampling process might take longer

database contains complex, nested data structures.

Forward

No

This option specifies how the driver samples data when generating a

temporary schema definition.

Forward

database, then samples the next record, and so on.

Backward

database, then samples the preceding record, and so on.

Random

random until the SamplingLimit is reached.

Clear

(

)

No

server.

Enabled

(1): The driver uses SSL to connect to the server.

Disabled

(0): The driver doesn't use SSL to connect to the server.

Valid

that you can specify for PolyBase Generic ODBC External Data Source are driver

specific. If not using a Microsoft-provided ODBC provider (see previous section), consult the driver's

documentation for valid key-value pairs.

There are some valid key-value pairs in PolyBase that are available to all generic ODBC drivers. The following

keys were added to SQL Server 2019 in CU5.

Key

Possible

values

## Description

,

Indicates whether or not the driver supports the SQLRowCount

function being called on ODBC catalog functions. Default is false. For

example:.

,

statement attribute. Default is false. For example:.

,

Indicates whether or not the driver supports bind offsets for row-wise

binding of result sets. If not, use column binding. Default is false. For

example:.

Key

Possible

values

## Description

,

operator

to the backend.

pushdown. If the user specifies

,

as the format string. If the user specifies

,

the format string.

external data source and/or driver documentation. For example:.

Data virtualization with PolyBase in SQL Server

CREATE EXTERNAL DATA SOURCE (Transact-SQL)

PolyBase Frequently asked questions
