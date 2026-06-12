---
title: "Analyze project code"
topic: "ssms"
description: ""
tags: ["ssms","analyze-project-code"]
pubDate: "2025-12-01"
---

You can improve the quality of the Transact-SQL code in a database schema by importing it

into a database project and analyzing the code against a set of rules. For example, you might

want to find any errors in a schema that you didn't develop and whose quality hasn't been

verified. For more information, see the

code analysis overview.

For this initial assessment, you want to find all the potential problems in the database code.

You review the warnings and the code that caused those warnings. To improve the T-SQL code,

you correct warnings, potentially suppress a warning, and iteratively analyze the database

project.

Before you can analyze the code in a database project, you must already have a SQL project.

For more information on using an existing database to create a project, see

Tutorial: start from

an existing database.

To enable SQL code analysis in Visual Studio, right-click the project in

and

select. In the

tab of the properties window, select the checkbox for.

Save the project properties window and return to solution explorer.

To analyze the code in a database project with code analysis enabled on build, right-click the

project in

and select.

The

window displays the results of the overall build process.

The T-SQL code in your database project is analyzed during build. Errors and warnings from

code analysis appear in the. If the

doesn't appear, open the View menu, and

select. You can double-click a warning to navigate to the line of code that caused the

warning.
