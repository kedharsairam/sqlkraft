---
title: "How to: Create Database Objects Using Table Designer"
topic: "ssb-diagnose"
description: ""
tags: ["ssb-diagnose","how-to-create-database-objects-using-table-designer"]
pubDate: "2025-12-01"
---

Not only is the

node in

Object Explorer

similar to SQL Server

Management Studio (SSMS) visually, but you can create new objects using contextual menus

that function like their SSMS counterparts.

For example, you can create a new database under the

node. Similarly, you can

select a specific database and create or edit table definitions and their related programming

objects on-the-fly using the new Table Designer. From the Table Designer, you can switch to a

script pane, which allows you to directly edit the script that defines this table.

1. In

Object Explorer

, under the

node, expand your connected

server instance.

2. Right-click the

node and select.

3. Rename the new database to.

1. Expand the newly created

node. Right-click the

node and select.

2. The Table Designer opens in a new window. The designer consists of the Columns Grid,

Script pane, and Context pane. The Columns Grid lists all the columns in the table. We

revisit other components of the designer in later procedures.

3. In the Script pane, rename the new table to. Specifically, replace

with

```cmd
Trade
Trade
Suppliers
CREATE
TABLE
[dbo].[Table1]
CREATE
TABLE
[dbo].[Suppliers]
```
