---
title: "Compatibility level"
topic: "collation"
description: "This article describes how to view or change the compatibility level of a database in SQL Ser"
tags: ["collation","compatibility-level"]
pubDate: "2025-12-01"
---

This article describes how to view or change the compatibility level of a database in SQL Server,

, or Azure SQL Managed Instance by using SQL Server Management Studio

or Transact-SQL.

Before you change the compatibility level of a database, you should understand the effect of

the change on your applications. For more information, see

ALTER DATABASE compatibility

level.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

Requires

permission on the database.

To view or change the compatibility level of a database using

Management Studio

(SSMS)

1. Connect to the appropriate server or instance hosting your database.

2. Select the server name in.

3. Expand

, and, depending on the database, either select a user database or

expand

and select a system database.

4. Right-click the database, and then select.

The

dialog box opens.

７

Note

You can't modify the compatibility level of system databases in Azure SQL Database.

```sql
AdventureWorks2025
AdventureWorksDW2025
ALTER
```
