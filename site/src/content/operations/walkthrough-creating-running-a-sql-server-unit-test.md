---
title: "Walkthrough: Creating & Running a SQL Server Unit Test"
topic: "ssb-diagnose"
description: |
  09/10/2025

  In this walkthrough, you create a SQL Server unit test that verifies the behavior of several

  stored procedures. You create SQL Server unit tests to help identify code defects that might

tags:
  - "ssb-diagnose"
  - "walkthrough-creating-running-a-sql-server-unit-test"
pubDate: 2025-12-01
---

09/10/2025

In this walkthrough, you create a SQL Server unit test that verifies the behavior of several

stored procedures. You create SQL Server unit tests to help identify code defects that might

cause incorrect application behavior. You can run SQL Server unit tests and application tests as

part of an automated suite of tests.

In this walkthrough, you perform the following tasks:

Create a script that contains a database schema

Create a database project and import that schema

Deploy the database project to an isolated development environment

Create SQL Server unit tests

Define test logic

Run SQL Server unit tests

Add a negative unit test

After one of the unit tests detects an error in a stored procedure, you correct that error and

rerun your test.

To complete this walkthrough, you must be able to connect to a database server (or LocalDB

database) on which you have permissions to create and deploy a database. For more

information, see

Required Permissions for Database Features of Visual Studio

.

1. On the

menu, point to

, and then select

.

The

dialog box appears.

2. In the

list, select

if it's not already highlighted.

3. In the

list, select

Sql File

, and then select

.

The Transact-SQL editor opens.

4. Copy the following Transact-SQL code, and paste it into the Transact-SQL editor.
