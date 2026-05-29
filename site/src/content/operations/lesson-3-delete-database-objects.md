---
title: "Lesson 3: Delete database objects"
topic: "configuration"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  Analytics Platform System (PDW)
  
  SQL database in Microsoft Fabric
  
  This short lesson removes the objects that you created in Le
tags:
  - "configuration"
  - "lesson-3-delete-database-objects"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

This short lesson removes the objects that you created in Lesson 1 and Lesson 2, and then

drops the database.

Before you delete objects, make sure you are in the correct database:

SQL

Use the

statement to remove execute permission for

on the stored procedure:

SQL

1. Use the

statement to remove permission for

to access the

database:

SQL

2. Use the

statement to remove permission for

to access this instance of SQL

Server 2005 (9.x):

SQL

７

Note

The

learning path provides more in-depth

content, along with practical examples.

```cmd
REVOKE
Mary
DROP
Mary
TestData
```