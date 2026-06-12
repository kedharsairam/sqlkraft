---
title: "Add Columns"
topic: "tables"
description: ""
tags: ["tables","add-columns"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Analytics Platform System (PDW)

Warehouse in Microsoft Fabric

This article describes how to add new columns to a table in SQL Server by using SQL Server

Management Studio or Transact-SQL.

Using the

statement to add columns to a table automatically adds those columns

to the end of the table.

If you want the columns in a specific order in the table, you must use SQL Server Management

Studio. Though it isn't recommended, for more information on reordering tables, see

Change

Column Order in a Table.

To query existing columns, use the

sys.columns

object catalog view.

Requires

permission on the table.

Management Studio (SSMS) doesn't support all data definition language (DDL)

options in Azure Synapse. Use

T-SQL scripts

instead.

1. In

, right-click the table to which you want to add columns and choose.

2. Select the first blank cell in the

column.

3. Type the column name in the cell. The column name is a required value.

）

Important

Install the latest version of

Management Studio (SSMS).

```sql
ALTER TABLE
ALTER
```
