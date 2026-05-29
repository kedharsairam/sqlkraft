---
title: "Add database objects using item templates"
topic: "profiler"
description: |
  ﾃ

  Summarize this article for me

  Use the SQL Database Projects extension for Visual Studio Code to add common database

  objects to your project using item templates. Item templates generate properly
tags:
  - "profiler"
  - "add-database-objects-using-item-templates"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

Use the SQL Database Projects extension for Visual Studio Code to add common database

objects to your project using item templates. Item templates generate properly formatted

Transact-SQL (T-SQL) files with standard boilerplate code, helping you maintain consistency

across your database schema.

Database objects added to a SQL project are validated during the project build. This validation

helps you catch syntax and reference problems early, before deployment starts.

Visual Studio Code installed

The SQL Database Projects extension

An existing SQL database project (

)

The SQL Database Projects extension includes the following item templates:

Description

Creates a new database schema for organizing database objects into logical

groups.

Creates a function that returns a table result set.

Creates a sequence object that generates sequential numeric values.

Creates a DML trigger that runs when

,

, or

operations occur

on a table or view.

Creates a DDL trigger that runs in response to database-level events.

Add database objects to your project using item templates from the Database Projects view.

1. In the Database Projects view, right-click your SQL project or an included folder.

ﾉ

Expand table

```cmd
.sqlproj
INSERT
UPDATE
DELETE
```
