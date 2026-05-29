---
title: "How to: Create SQL Server Unit Tests for Functions, Triggers, & Stored Procedures"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  You can write unit tests that evaluate changes to any database object. However SQL Server
  
  Data Tools includes support for creating tests for database functions, triggers, and stored
  
  proc
tags:
  - "ssb-diagnose"
  - "how-to-create-sql-server-unit-tests-for-functions-triggers-stored-procedures"
pubDate: 2025-12-01
---

09/10/2025

You can write unit tests that evaluate changes to any database object. However SQL Server

Data Tools includes support for creating tests for database functions, triggers, and stored

procedures from a database project node in SQL Server Object Explorer. Transact-SQL code

stubs can be automatically generated for you to customize.

1. See

Walkthrough: Create and run a SQL Server unit test

for an example of adding a unit

test for a stored procedure, in the "To create a SQL Server unit test for the stored

procedures" section.

The Inconclusive test condition is the default condition that is added to every test. This

test condition is included to indicate that test verification isn't implemented yet. Delete

this test condition from your test after you add other test conditions. For more

information, see

How to: Add Test Conditions to SQL Server Unit Tests

.

Create and define SQL Server unit tests

How to: Create an Empty SQL Server Unit Test