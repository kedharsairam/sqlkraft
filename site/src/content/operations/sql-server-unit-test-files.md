---
title: "SQL Server Unit Test Files"
topic: "ssb-diagnose"
description: |
  SQL Server unit test files

  09/10/2025

  Like the unit tests for managed code, SQL Server unit tests reside in test projects. You can see

  the items that compose a SQL Server unit test in the hierarchy
tags:
  - "ssb-diagnose"
  - "sql-server-unit-test-files"
pubDate: 2025-12-01
---

unit test files

09/10/2025

Like the unit tests for managed code, SQL Server unit tests reside in test projects. You can see

the items that compose a SQL Server unit test in the hierarchy of a test project in.

A SQL Server unit test consists of multiple items that are contained in several files. The

following table describes the files that interact to form a SQL Server unit test.

Description

or

This source-code file contains a class that is decorated with the [TestClass]

attribute. This class contains a single test method for each of the contained

unit tests. These methods are decorated with the [TestMethod]

attribute.

Each test method contains the appropriate code to exercise the Transact-

SQL test script. This code is generated when the test methods are created,

and you can modify it.

NOTE:

If you double-click this file in

, the test class opens

in the SQL Server Unit Test Designer. To open the

or

file to see its

source code, right-click the file in

, and then select.

This resource file contains the Transact-SQL scripts for all tests in the

associated

or

file. This group of scripts includes the pre-test script,

the test script, and the post-test script. The resource file contains XML, which

you can edit. The resource file is compiled into the test assembly.

You should code your Transact-SQL scripts by using the

Unit Test. For more information about the scripts that are used in SQL Server

unit tests, see

Scripts in SQL Server Unit Tests.

This file stores the database connection strings for the test project, in

addition to other SQL Server unit test configuration settings such as

command timeout. For more information, see

Scripts in SQL Server Unit

Tests.

or

This file contains a class that prepares the test environment for all SQL

Server unit tests in the test project. Based on the configuration settings in

the app.config file, it might deploy a SQL Server Database Project to the test

database.

ﾉ

Expand table

```cmd.cs.vb.cs.vb.resx
```
