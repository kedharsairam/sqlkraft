---
title: "Creating & Defining SQL Server Unit Tests"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  You can run SQL Server unit tests to verify whether changes to one or more database objects in
  
  a schema have broken existing functionality in a database application. These tests complemen
tags:
  - "ssb-diagnose"
  - "creating-defining-sql-server-unit-tests"
pubDate: 2025-12-01
---

09/10/2025

You can run SQL Server unit tests to verify whether changes to one or more database objects in

a schema have broken existing functionality in a database application. These tests complement

the unit tests that your software developers create. You must run both kinds of tests to verify

the behavior of your application.

You can verify the behavior of any object in your schema by adding a SQL Server unit test and

adding a Transact-SQL script to test that object. As an alternative, you can automatically

generate a stub of a Transact-SQL script if you want to verify the behavior of a particular

function, trigger, or stored procedure. After you generate the stub, you must customize it to

obtain meaningful results.

In the following table, you can find descriptions of common tasks that support this scenario

and links to more information about how you can successfully complete those tasks.

: You can follow an introductory walkthrough to become

familiar with how to create and run a simple SQL Server unit test.

-

Walkthrough: Create

and run a SQL Server

unit test

: You can learn more about the files and

scripts that compose a SQL Server unit test. You can also learn about how to use

test conditions and Transact-SQL assertions in your unit tests.

-

Scripts in SQL Server

Unit Tests

-

SQL Server Unit Test

Files

-

Use test conditions

in SQL Server unit

tests

-

Use Transact-SQL

７

Note

You can create an empty test, add code to it, and run it without having a SQL Server

database project open. However, you can't automatically generate a Transact-SQL stub

that tests a function, trigger, or stored procedure without opening the project that

contains the object that you want to test.

ﾉ

Expand table