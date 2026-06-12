---
title: "How to: Create an Empty SQL Server Unit Test"
topic: "ssb-diagnose"
description: |
  09/09/2025
          
            Include unit tests in your database project to verify changes you make to database objects
          
            don't break existing functionality. The following procedures explain how to create SQL Server
          
            u
tags: ["ssb-diagnose","how-to-create-an-empty-sql-server-unit-test"]
pubDate: 2025-12-01
---

Include unit tests in your database project to verify changes you make to database objects

don't break existing functionality. The following procedures explain how to create SQL Server

unit tests for any database object. SQL Server Data Tools includes some extra support for

database functions, triggers, and stored procedures. For more information, see

How to: Create

Unit Tests for Functions, Triggers, and Stored Procedures.

When you create a SQL Server unit test using the first procedure, a test project is automatically

created for you if no test project exists. If test projects already exist, you have the option of

adding the new test to one of those projects or you can create a new test project. For more

information about test projects, see

How to: Create a Test Project for SQL Server Database Unit

Testing.

You have two options for creating a SQL Server unit test:

Create a new SQL Server unit test inside a new test class.

All SQL Server unit tests within a given test class use the same TestInitialize and

TestCleanup scripts. Create a new test class if you want your unit test to use different

TestInitialize and TestCleanup scripts than other unit tests. For more information, see

Scripts in SQL Server Unit Tests.

Create a new SQL Server unit test inside an existing test class.

Choose this option if your unit test uses the same TestInitialize and TestCleanup scripts as

other unit tests within the class.

1. On the

menu, select.

The

dialog box appears.

2. Under

, select

Unit Test.

3. Under

, enter a name for the test.

4. Under

, select an existing test project, into which to add this test. If no

test project exists or if you want to create a new test project, select.
