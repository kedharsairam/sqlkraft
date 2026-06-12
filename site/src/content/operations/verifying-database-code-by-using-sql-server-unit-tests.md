---
title: "Verifying Database Code by Using SQL Server Unit Tests"
topic: "ssb-diagnose"
description: |
  09/10/2025
          
            You can use SQL Server unit tests to establish a baseline state for your database and then to
          
            verify any subsequent changes that you make to database objects.
          
            To establish a baseline sta
tags: ["ssb-diagnose","verifying-database-code-by-using-sql-server-unit-tests"]
pubDate: 2025-12-01
---

You can use SQL Server unit tests to establish a baseline state for your database and then to

verify any subsequent changes that you make to database objects.

To establish a baseline state for a database, you create a test project and write sets of Transact-

SQL that operate on your database objects. By using these tests, you can verify in an isolated

development environment whether those objects function as expected. SQL Server unit testing

works well in combination with offline database development using SQL Server database

projects. For more information,

What are SQL database projects?. Once you have a baseline set

of SQL Server unit tests, you can use these tests to verify that the database is working correctly

before checking in changes to version control.

You can create tests that verify changes to any database object. In addition, you can

automatically generate stubs of Transact-SQL code that test database functions, triggers, and

stored procedures.

As you or your team members change the database schema, you can use these tests to verify

whether the changes have broken existing functionality. You create SQL Server unit tests to

complement the software unit tests that your software developers create. You must complete

both sets of tests to verify the overall behavior of your application.

Your unit tests can verify that the procedures succeed when they are expected to succeed and

that procedures fail when they are expected to fail. Testing that appropriate failures occur is

referred to as negative testing.

７

Note

You can create and run SQL Server unit tests without having a database project open.

However, if you want to auto-generate test scripts to test specific database objects from

your project, you must open the database project that contains the objects that you want

to test.
