---
title: "Compare a database and a project"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Understanding the object definition differences between a database and a SQL project can

  pro
tags:
  - "ssms"
  - "compare-a-database-and-a-project"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Understanding the object definition differences between a database and a SQL project can

provide valuable insights into the state of your database and project, including during ongoing

development or regression troubleshooting. SQL projects include tooling for visualizing

differences, analyzing changes required for updating a database, importing changes from a

database into a SQL project file set, and reviewing T-SQL scripts that would be executed to

update a database to match the project.

This article reviews methods for comparing a database and a SQL project using different

approaches:

You can use

to

visualize the differences

between databases and/or

projects. This comparison can help you identify changes that need to be synchronized

between the database and the project.

You can use a

to

summarize and automate reviews

of the changes required

to update a database.

You can use

or SqlPackage

to

import changes from a database

into a SQL project file set.

You can use SqlPackage

or

to

review the T-SQL

statements

that are executed to update a database to match the project.

Visual Studio 2022 Community, Professional, or Enterprise

Data Tools (SSDT) installed in Visual Studio

Graphical schema comparison isn't yet available in the SDK-style SQL projects preview in Visual

Studio. Use Visual Studio Code or Visual Studio to compare schemas.NET 8 SDK

SQL Database Projects extension

Schema compare is available in Visual Studio, or through the

MSSQL extension for Visual

Studio Code.
