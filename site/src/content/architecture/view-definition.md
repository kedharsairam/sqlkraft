---
title: "View definition"
topic: "spatial-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  SQL database in Microsoft

  Fabric

  This article describes how to view
tags:
  - "spatial-data"
  - "view-definition"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

This article describes how to view the definition of procedure in Object Explorer or T-SQL.

:

1. In Object Explorer, connect to an instance of Database Engine and then expand that

instance.

2. Expand

, expand the database in which the procedure belongs, and then

expand

.

3. Expand

, right-click the procedure and then select

, and then select one of the following:

,

, or

.

4. Select

. This will display the procedure definition.

In T-SQL, you can use one of the following three commands:

sp_helptext

OBJECT_DEFINITION

sys.sql_modules

７

Note

The system stored procedure

is not supported in Azure Synapse Analytics.

Instead, use

object catalog view.

```sql
sp_helptext
sys.sql_modules
```
