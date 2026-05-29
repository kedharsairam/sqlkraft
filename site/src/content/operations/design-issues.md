---
title: "Design issues"
topic: "ssms"
description: |
  Article
  
  •
  
  11/22/2024
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  When you analyze the T-SQL code in your database project, one or more
tags:
  - "ssms"
  - "design-issues"
pubDate: 2025-12-01
---

Article

•

11/22/2024

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

When you analyze the T-SQL code in your database project, one or more warnings might be

categorized as design issues. You should address design issues to avoid the following

situations:

Subsequent changes to your database might break applications that depend on it.

The code might not produce the expected result.

The code might break if you run it with future releases of SQL Server.

In general, you shouldn't suppress a design issue because it might break your application,

either now or in the future.

The provided rules identify the following design issues:

SR0001: Avoid SELECT * in stored procedures, views, and table-valued functions

SR0008: Consider using SCOPE_IDENTITY instead of @@IDENTITY

SR0009: Avoid using types of variable length that are size 1 or 2

SR0010: Avoid using deprecated syntax when you join tables or views

SR0013: Output parameter (parameter) is not populated in all code paths

SR0014: Data loss might occur when casting from {Type1} to {Type2}

If you use a wildcard character in a stored procedure, view, or table-valued function to select all

columns in a table or view, the number or shape of returned columns might change if the

underlying table or view changes. The shape of a column is a combination of its type and size.

This variance could cause problems in applications that consume the stored procedure, view, or

table-valued function because those consumers will expect a different number of columns.

You can protect consumers of the stored procedure, view, or table-valued function from

schema changes by replacing the wildcard character with a fully qualified list of column names.