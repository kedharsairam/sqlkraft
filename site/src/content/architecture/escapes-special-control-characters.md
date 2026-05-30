---
title: "Escapes special & control characters"
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
  - "escapes-special-control-characters"
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

This article describes how the

clause of a SQL Server

statement escapes

special characters and represents control characters in the JSON output.

This article describes the built-in support for JSON in Microsoft SQL Server. For general

information about escaping and encoding in JSON, see Section 2.5 of the

JSON RFC

.

If the source data contains special characters, the

clause escapes them in the JSON

output with

, as shown in the following table. This escaping occurs both in the names of

properties and in their values.

Quotation mark (

)

Backslash (

)

Slash (

)

Backspace

Form feed

New line

Carriage return

Horizontal tab

ﾉ

Expand table

```sql
FOR JSON
SELECT
FOR JSON
\
"
\"
\
\\
/
\/
\b
\f
\n
\r
\t
```
