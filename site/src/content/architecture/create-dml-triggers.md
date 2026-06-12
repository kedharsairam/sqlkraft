---
title: "Create DML Triggers"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This article describes how to create a Transact-SQL Data Manipulation Language (DML) trigger

tags:
  - "change-data-capture"
  - "create-dml-triggers"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This article describes how to create a Transact-SQL Data Manipulation Language (DML) trigger

with SQL Server Management Studio, or the Transact-SQL

statement.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

For a list of limitations and restrictions related to creating DML triggers, see

CREATE TRIGGER.

Requires

permission on the table or view on which the trigger is being created.

You can use one of the following methods:

Management Studio

Transact-SQL

1. In

, connect to an instance of Database Engine and then expand that

instance.

2. Expand

, expand the

database, expand

, and then

expand the table.

3. Right-click

, and then select.

4. On the

menu, select. Alternatively, you

can press (Ctrl-Shift-M) to open the

dialog box.

5. In the

dialog box, enter the following values for

the parameters shown.

```sql
CREATE TRIGGER
AdventureWorks2025
AdventureWorksDW2025
ALTER
AdventureWorks2025
Purchasing.PurchaseOrderHeader
```
