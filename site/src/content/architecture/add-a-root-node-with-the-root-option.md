---
title: "Add a root node with the ROOT option"
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
  - "add-a-root-node-with-the-root-option"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

(serverless SQL pool only)

analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in

Microsoft Fabric

To add a single, top-level element to the JSON output of the

clause, specify the

option.

If you don't specify the

option, the JSON output doesn't include a root element.

The following table shows the output of the

clause with and without the

option.

The examples in the following table assume that the optional

RootName

argument is empty. If

you provide a name for the root element, this value replaces the value

in the examples.

JSON

JSON

JSON

```sql
FOR JSON
ROOT
ROOT
FOR JSON
ROOT root
{
<<json properties>>
}
[
<<json array elements>>
]
{
"root"
: {
<<json properties>>
}
}
```
