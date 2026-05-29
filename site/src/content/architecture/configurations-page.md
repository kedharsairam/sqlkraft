---
title: "Configurations page"
topic: "collation"
description: |
  Article
  
  •
  
  01/07/2025
  
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  Azure Synapse Analytics
  
  SQL database in Microsoft Fabric
  
  Use the
  
  pag
tags:
  - "collation"
  - "configurations-page"
pubDate: 2025-12-01
---

Article

•

01/07/2025

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

SQL database in Microsoft Fabric

Use the

page to view or modify options for the selected database. For

more information about the options available on this page, see

ALTER DATABASE SCOPED

CONFIGURATION

.

Displays the name of the database scoped option for the database.

Displays the option value for the primary database.

Displays the option value for all secondary databases.

sys.database_scoped_configurations

）

Important

Different

options are supported in different versions of

SQL Server, and in different Azure or Fabric platforms using the SQL Database Engine.

```sql
DATABASE SCOPED CONFIGURATION
```