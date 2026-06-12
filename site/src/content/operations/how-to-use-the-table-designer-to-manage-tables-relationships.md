---
title: "How to: Use the Table Designer to Manage Tables & Relationships"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
    The Table Designer provides a visual experience alongside the Transact-SQL Editor for creating
  
    and editing table structure, including table-specific programming objects, for SQL Server
  
    d
tags: ["ssb-diagnose","how-to-use-the-table-designer-to-manage-tables-relationships"]
pubDate: "2025-12-01"
---

The Table Designer provides a visual experience alongside the Transact-SQL Editor for creating

and editing table structure, including table-specific programming objects, for SQL Server

databases. It launches when you create a new table for a connected database or a project, or

when you double-click to edit a table in either SQL Server Object Explorer or Solution Explorer.

The designer consists of the Columns Grid, Script pane, and Context pane. The Columns Grid

lists all the columns in the table. You can add, edit, and delete columns in this grid. The Context

pane gives you a logical view of the table definition (Keys, Indices, Constraints, Triggers, etc.),

and enables you to select an object to highlight its relationships to individual columns. You can

also add new objects to the table in this pane, and edit the properties of a selected object in

the Properties Grid. Script pane shows you the definition of the table structure, and highlights

the script of the selected object in the Context pane or Columns Grid. You can edit the script

side-by-side with the Columns Grid and Context pane in view. Any changes from any of the

three panes propagate to the other two immediately.

1. Open the TradeDev project you have been working on in previous procedures.

2. In

, expand the

folder, right-click the

folder, select

, and

then select.

3. Name the new table

and select.

4. The Table Designer opens. In the Columns Grid, add a new column to the table with name

and Data Type.

5. You can also edit the properties of columns in the

window. Select the

column, and in the

window, change the

of this column

to

, and

to. As you shift your focus out of the field, the Script pane

and the Columns Grid of the designer automatically update to reflect your change.

２

Warning

The following procedure uses entities created in previous procedures in the

SQL database

sections.

```cmd
Shipper
ShipperName
ShipperName
128
```
