---
title: "How to: Create a Test Project for SQL Server Database Unit Testing"
topic: "ssb-diagnose"
description: |
  09/10/2025

  Before you can start to write unit tests that evaluate database objects, you must first create a

  test project. This project contains SQL Server unit tests, but it could contain other type
tags:
  - "ssb-diagnose"
  - "how-to-create-a-test-project-for-sql-server-database-unit-testing"
pubDate: 2025-12-01
---

09/10/2025

Before you can start to write unit tests that evaluate database objects, you must first create a

test project. This project contains SQL Server unit tests, but it could contain other types of

tests.

You can place all of your SQL Server unit tests for a given database project within a single test

project. However, you might want to create more test projects based on your answers to the

following questions:

Do different SQL Server unit tests need

to access different database connections

for test execution or test validation?

If yes, you need more than one test project. You can't specify

more than one database connection for test execution.

However, you can specify a different database connection for

test validation.

Do you want to deploy different

database projects for different unit tests?

If yes, you need more than one test project. A test project can

only deploy a single database project.

For more information about each of these questions, see

How to: Configure SQL Server unit

test execution. As an alternative to creating multiple test projects, you can also provide your

own

DatabaseTestService

Microsoft.Data.Schema.UnitTesting.DatabaseTestService

implementation.

You have three options for adding a test project to a solution that contains a database project:

Add a test project to the solution. The test project contains a standard unit test, which

you can delete. This project doesn't contain a SQL Server unit test class, which you must

add.

Add a new SQL Server unit test from the

menu. When you add the unit test, SQL

Server Data Tools also creates a test project if you request it. This project contains a SQL

Server unit test class. SQL Server unit test classes contain one or more unit tests.

ﾉ

Expand table
