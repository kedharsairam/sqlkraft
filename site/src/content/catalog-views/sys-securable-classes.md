---
name: 'sys.securable_classes'
title: 'sys.securable_classes'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric


## Returns a list of securable classes

## Description
Name of the class.

Numerical designation of the class.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following example returns the securable classes supported by this instance of SQL Server.

SQL

Securables

Last updated on 11/18/2025

ﾉ

Expand table

See Also

```sql
SELECT
*
FROM
sys.securable_classes
ORDER
BY
class
;
```
