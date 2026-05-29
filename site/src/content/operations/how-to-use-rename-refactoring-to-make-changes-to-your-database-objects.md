---
title: "How to: Use Rename & Refactoring to Make Changes to your Database Objects"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  The
  
  contextual menu in the Transact-SQL Editor allows you to rename or move an
  
  object to a different schema and preview all affected areas before committing the change. You
  
  can also use
tags:
  - "ssb-diagnose"
  - "how-to-use-rename-refactoring-to-make-changes-to-your-database-objects"
pubDate: 2025-12-01
---

09/10/2025

The

contextual menu in the Transact-SQL Editor allows you to rename or move an

object to a different schema and preview all affected areas before committing the change. You

can also use the

menu to fully qualify all references to database objects, or expand

any wildcard characters in

statements in your database project.

1. Right-click the

table (

) in

, and select

to open the script in Transact-SQL Editor.

2. Right-click

in the script, select

, and

.

3. In the

field, change it to

. Leave the

option checked

and select

.

4. In the next screen, you can preview a list of scripts that this rename operation is going to

affect. Specifically, all the places that refer to

are highlighted. This process is

similar to the Find All References task in the previous procedure. Select anything on the

top pane and view the actual change in the scripts (highlighted in green) in the bottom

pane.

5. Select

.

6. For script files that are already opened in Table Designer or Transact-SQL Editor, the

Transact-SQL Editor highlights the locations where changes took place with a green bar

on the left.

7. Notice the addition of

in

. Double-click to open

it. It contains an XML representation of all the changes in this session.

8. Press

to build and deploy the project to the local database.

２

Warning

The following procedure uses entities created in previous procedures in the

SQL database

sections.

```cmd
SELECT
Products
Products.sql
[Products]
Product
```