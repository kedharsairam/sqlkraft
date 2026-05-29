---
title: "Format nested output with PATH mode"
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
  - "format-nested-output-with-path-mode"
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

To maintain full control over the output of the

clause, specify the

option.

mode lets you create wrapper objects and nest complex properties. The results are

formatted as an array of JSON objects.

The alternative is to use the

option to format the output automatically based on the

structure of the

statement.

For more info about the

option, see

Format JSON output automatically with AUTO

mode

.

For an overview of both options, see

Format query results as JSON with FOR JSON

.

The following examples show how to use the

clause with the

option. Format

nested results by using dot-separated column names or by using nested queries, as shown in

the examples. By default, null values aren't included in

output.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

The following query formats the first five rows from the AdventureWorks

table as JSON.

７

Note

The

can auto-format the JSON results (as seen

in this article) instead of displaying an unformatted string.

```sql
FOR JSON
PATH
PATH
AUTO
SELECT
AUTO
FOR JSON
PATH
FOR JSON
AdventureWorks2025
AdventureWorksDW2025
Person
```