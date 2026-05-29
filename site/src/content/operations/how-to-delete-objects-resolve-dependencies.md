---
title: "How to: Delete Objects & Resolve Dependencies"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  When you rename or delete an object in
  
  SQL Server Object Explorer
  
  , SQL Server Data Tools
  
  (SSDT) automatically detects all its dependency objects, and prepares an
  
  script to
  
  rename or 
tags:
  - "ssb-diagnose"
  - "how-to-delete-objects-resolve-dependencies"
pubDate: 2025-12-01
---

09/10/2025

When you rename or delete an object in

SQL Server Object Explorer

, SQL Server Data Tools

(SSDT) automatically detects all its dependency objects, and prepares an

script to

rename or drop the dependency as needed.

1. Right-click a database in

SQL Server Object Explorer

, and select

.

2. Accept all the default settings in the

dialog, and select

.

1. Make sure that the

table isn't opened in either the Table Designer or the

Transact-SQL Editor.

2. Expand the

node in

SQL Server Object Explorer

. Right-click the

table

and select

.

3. Change the table name to

and press ENTER.

4. A

operation is immediately invoked on your behalf. SSDT calls the

stored procedure on your behalf to rename the table. If there are any

dependent objects such as foreign key constraints, they're also updated.

5. Apply the change following the steps in the previous

How to: Update a connected

database with Power Buffer

procedure.

6. Right-click the

table in

SQL Server Object Explorer

again, and select

. Table data is intact after the rename operation.

２

Warning

Script-based dependencies such as references to a table from a view, or stored

procedures aren't automatically updated by SSDT. After the rename, you can use the

pane to locate all other dependencies and manually fix them.

```cmd
ALTER
Customer
Customer
sp_rename
Customers
```