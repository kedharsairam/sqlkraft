---
title: "Specify default values for Columns"
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
  - "specify-default-values-for-columns"
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

You can use SQL Server Management Studio (SSMS) to specify a default value that is entered

into the table column. You can set a default by using the Object Explorer, or by executing

Transact-SQL.

If you don't assign a default value to the column, and the user leaves the column blank, then:

If you set the option to allow null values,

is inserted into the column.

If you don't set the option to allow null values, the column remains blank, but the user or

application can't insert the row until they supply a value for the column.

You can use a default constraint for various tasks to ensure database-level data consistency:

Set the row value for an "active" or "enable" column to

upon insertion.

Set the row value for a date field to the current date.

Set the row value for a field to a deterministic system function, for example,

.

Before you begin, be aware of the following limitations and restrictions:

If your entry in the

field replaces a bound default (which is shown without

parentheses), you're prompted to unbind the default and replace it with your new default.

To enter a text string, enclose the value in single quotation marks (

). Don't use double

quotation marks (

), because they're reserved for quoted identifiers.

To enter a numeric default, enter the number without quotation marks around it.

To enter an object/function, enter the name of the object/function without quotation

marks around it.

In Azure Synapse Analytics, only constants can be used for a default constraint. An

expression can't be used with a default constraint.

The actions described in this article require

permission on the table.

```sql
NULL
1
DB_NAME()
'
"
ALTER
```
