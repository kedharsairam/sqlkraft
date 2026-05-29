---
title: "How to: View & Edit Data in a Table"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  You can view, edit, and delete data in an existing table by using a visual Data Editor.
  
  1. Right-click the
  
  table in
  
  SQL Server Object Explorer
  
  , and select
  
  .
  
  2. The Data Editor launc
tags:
  - "ssb-diagnose"
  - "how-to-view-edit-data-in-a-table"
pubDate: 2025-12-01
---

09/10/2025

You can view, edit, and delete data in an existing table by using a visual Data Editor.

1. Right-click the

table in

SQL Server Object Explorer

, and select

.

2. The Data Editor launches. Notice the rows we added to the table in previous procedures.

3. Right-click the

table in SQL Server Object Explorer, and select

.

4. In the Data Editor, type

for

and

for

, then either press ENTER or TAB

to shift focus away from the new row to commit it to the database.

5. Repeat the previous step to enter

,

, and

,

to the table.

As you're editing a row, you can always revert the changes to a cell by pressing ESC.

6. You can view your edits as a script by selecting the

button on the toolbar.

Alternatively, you can use the

button to save them in a

script file to be

executed later.

7. Right-click the

database in

SQL Server Object Explorer

, and select

. In

the editor, type

and press the

button

to return the data represented by the

view.

２

Warning

The following procedure uses entities created in previous procedures in the

SQL database

sections.

```cmd
Products
Fruits
1
2
3
```