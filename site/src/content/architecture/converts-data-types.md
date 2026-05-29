---
title: "Converts data types"
topic: "json-data"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  Azure Synapse Analytics (serverless SQL pool only)
  
  SQL
  
  analytics endpoint in Microsoft Fabric
tags:
  - "json-data"
  - "converts-data-types"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics (serverless SQL pool only)

SQL

analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in

Microsoft Fabric

The

clause uses the following rules to convert SQL Server data types to JSON types in

the JSON output.

SQL Server data type

Character

& string

types

,

,

,

string

Numeric

types

,

,

,

,

number

Bit type

(true or false)

Date &

time types

,

,

,

,

string

Binary

types

,

,

,

/

BASE64-encoded string

CLR types

,

,

other CLR types

Not supported. These types return an error.

In the

statement, use

or

, or use a CLR

property or method, to convert the source data to a SQL

Server data type that can be converted successfully to a JSON

type. For example, use

for the geometry type, or

use

for any CLR type. The type of the JSON output

value is then derived from the return type of the conversion

that you apply in the

statement.

Other

types

,

string

ﾉ

Expand table

```sql
FOR JSON
SELECT
CAST
CONVERT
STAsText()
ToString()
SELECT
```