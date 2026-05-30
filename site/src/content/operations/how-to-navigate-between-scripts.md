---
title: "How to: Navigate Between Scripts"
topic: "ssb-diagnose"
description: |
  09/10/2025

  The Transact-SQL Editor for offline development provides two useful navigation tools that are

  familiar to Visual Studio users: Go To Definition and Find All References. For example, you c
tags:
  - "ssb-diagnose"
  - "how-to-navigate-between-scripts"
pubDate: 2025-12-01
---

09/10/2025

The Transact-SQL Editor for offline development provides two useful navigation tools that are

familiar to Visual Studio users: Go To Definition and Find All References. For example, you can

right-click a table name and use "Find All References" to list all references to the table in the

project. You can double-click a search result to go to the specific code file. In this file, you can

right-click the table name again, and choose "Go to Definition" to go back to the table

definition.

1. Expand the

folder in

and double-click

.

2. Right-click

in this line of code and select

3.

is automatically opened, showing the location where the

type is

defined.

4. Go back to

. This time selects

in the

contextual menu for

. In the

pane, you see a list of

locations where the

table is referenced. Double-clicking any of the search

results bring you to the location of the reference.

２

Warning

The following procedure uses entities created in previous procedures in the

SQL database

sections.

```cmd
GetProductsBySupplier.sql
Products
Products.sql
Products
GetProductsBySupplier.sql
```
