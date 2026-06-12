---
title: "Format results as JSON"
topic: "json-data"
description: "2016 (13.x) and later versions Azure SQL Managed Instance Azure Synapse Analytics (serverless SQL pool only) SQL analytics endpoint in Microsoft Fabric"
tags: ["json-data","format-results-as-json"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

(serverless SQL pool only)

analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in

Microsoft Fabric

Format query results as JSON, or export data from SQL Server as JSON, by adding the

clause to a

statement. Use the

clause to simplify client applications by

delegating the formatting of JSON output from the app to SQL Server.

In Fabric Data Warehouse,

must be the last operator in the query, and so you can't

use it inside subqueries.

When you use the

clause, you can specify the structure of the JSON output explicitly,

or let the structure of the

statement determine the output.

To maintain full control over the format of the JSON output, use. You can

create wrapper objects and nest complex properties.

To format the JSON output automatically based on the structure of the

statement,

use.

Here's an example of a

statement with the

clause and its output.

７

Note

The

can auto-format the JSON results (as seen

in this article) instead of displaying an unformatted string.

```sql
FOR JSON
SELECT
FOR JSON
FOR JSON
FOR JSON
SELECT
FOR JSON PATH
SELECT
FOR JSON AUTO
SELECT
FOR JSON
```
