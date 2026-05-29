---
title: "Format with AUTO mode"
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
  - "format-with-auto-mode"
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

To automatically format the output of the

clause based on the structure of the

statement, specify the

option.

When you specify the

option, the format of the JSON output is automatically determined

based on the order of columns in the SELECT list and their source tables. You can't change this

format.

Use the

option if you want to control the output.

For more info about the

option, see

Format nested JSON output with PATH mode

.

For an overview of both options, see

Format query results as JSON with FOR JSON

.

A query that uses the

option must have a

clause.

Here are some examples of the

clause with the

option.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

When a query references only one table, the results of the

clause are similar to

the results of

. In this case,

doesn't create nested objects. The

７

Note

The

can auto-format the JSON results (as seen

in this article) instead of displaying an unformatted string.

```sql
FOR JSON
SELECT
AUTO
AUTO
PATH
PATH
FOR JSON AUTO
FROM
FOR JSON
AUTO
AdventureWorks2025
AdventureWorksDW2025
FOR JSON AUTO
FOR JSON PATH
FOR JSON AUTO
```
