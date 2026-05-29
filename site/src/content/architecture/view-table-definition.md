---
title: "View Table Definition"
topic: "tables"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  Azure Synapse Analytics
  
  Analytics Platform System (PDW)
  
  SQL database in Microsoft Fabric
  
  You
tags:
  - "tables"
  - "view-table-definition"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

You can display properties for a table in SQL Server by using SQL Server Management Studio or

Transact-SQL.

You can only see properties in a table if you either own the table or have been granted

permissions to that table.

1. In Object Explorer, select the table for which you want to show properties.

2. Right-click the table and select

from the shortcut menu. For more information,

see

Table Properties - SSMS

.

You can script out existing objects from the Object Explorer in SSMS. For more information, see

Generate Scripts

.

1. In

, connect to an instance of Database Engine.

2. On the Standard bar, select

.

3. Copy and paste the following example into the query window and select

. The

example executes the system stored procedure

to return all column information

for the specified object. For more information, see

sp_help

.

```sql
sp_help
```