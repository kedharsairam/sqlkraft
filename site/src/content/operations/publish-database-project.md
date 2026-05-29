---
title: "Publish database project"
topic: "profiler"
description: |
  Use the SQL Database Projects extension for Visual Studio Code to deploy database schema
  
  changes directly from a SQL project.
  
  A SQL project deployment takes the schema you define in the project, com
tags:
  - "profiler"
  - "publish-database-project"
pubDate: 2025-12-01
---

Use the SQL Database Projects extension for Visual Studio Code to deploy database schema

changes directly from a SQL project.

A SQL project deployment takes the schema you define in the project, compares it to the

target database, and applies only the necessary changes to bring the database into the desired

state through a dynamically generated plan.

You can review changes, generate a deployment script, and publish updates to a target

database without leaving the editor.

Before you begin, make sure you have:

Visual Studio Code installed

The MSSQL extension for Visual Studio Code

The SQL Database Projects extension

An existing SQL database project (

)

Access to a SQL Server or Azure SQL Database target

You can open the Publish dialog from the

view.

1. Open the

view.

2. Right-click your SQL project.

3. Select

.

The Publish dialog opens in a new editor tab.

```cmd
.sqlproj
```