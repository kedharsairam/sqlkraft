---
title: "Delete a publication"
topic: "migration"
description: |
  Article
  
  •
  
  09/27/2024
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This topic describes how to delete a publication in SQL Server by using SQL Server
  
  Management Studio, Transact-SQL, or Rep
tags:
  - "migration"
  - "delete-a-publication"
pubDate: 2025-12-01
---

Article

•

09/27/2024

Applies to:

SQL Server

Azure SQL Managed Instance

This topic describes how to delete a publication in SQL Server by using SQL Server

Management Studio, Transact-SQL, or Replication Management Objects (RMO).

SQL Server Management Studio

Transact-SQL

Replication Management Objects (RMO)

Delete publications from the

folder in SQL Server Management Studio.

1. Connect to the Publisher in Management Studio, and then expand the server node.

2. Expand the

folder, and then expand the

folder.

3. Right-click the publication you want to delete, and then click

.

Publications can be deleted programmatically using replication stored procedures. The stored

procedures that you use depend on the type of publication being deleted.

７

Note

Deleting a publication does not remove published objects from the publication database

or the corresponding objects from the subscription database. Use the

command to manually remove these objects if necessary.

```cmd
DROP <object>
```