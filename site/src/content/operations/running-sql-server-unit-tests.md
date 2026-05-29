---
title: "Running SQL Server Unit Tests"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  To improve and maintain the quality of your code, you can create and run SQL Server unit tests
  
  that verify the behavior of any database object and then check in those tests to version con
tags:
  - "ssb-diagnose"
  - "running-sql-server-unit-tests"
pubDate: 2025-12-01
---

09/10/2025

To improve and maintain the quality of your code, you can create and run SQL Server unit tests

that verify the behavior of any database object and then check in those tests to version control.

As you or any member of your team changes the database schema, you run both SQL Server

unit tests and software unit tests to verify that the changes haven't broken existing

functionality. You can run individual tests, or you can run groups of tests, which are known as

test lists. For more information, see

Using Test Lists (Visual Studio 2010)

.

You can run SQL Server unit tests in several ways that vary based on the software that you have

installed, as the following shows:

Run tests by using the Visual Studio 2010

window. For more information, see

How to: Run SQL Server unit tests

and

How to: Run Automated Tests from Microsoft

Visual Studio 2010

. For Visual Studio 2012, see

How to: Run Automated Tests from

Microsoft Visual Studio 2012

.

Run tests by using the MSTest.exe command at a command prompt. For more

information, see

How to: Run Automated Tests from the Command Line Using MSTest

(Visual Studio 2010)

or

How to: Run Automated Tests from the Command Line Using

MSTest (Visual Studio 2012)

.

Run tests from

by running a test project. For more information, see

How to: Run Automated Tests from Microsoft Visual Studio 2010

or

How to: Run

Automated Tests from Microsoft Visual Studio 2012

.

Rerun tests from the

window. For more information, see

How to: Rerun a

Test (Visual Studio 2010)

.

Run individual tests or test lists (Visual Studio 2010) from the

window. For

more information, see

How to: Run Automated Tests from Microsoft Visual Studio 2010

or

How to: Run Automated Tests from Microsoft Visual Studio 2012

.

Run tests as you build a project in Team Foundation Build. For more information, see

How

to: Configure and Run Scheduled Tests After Building Your Application (Visual Studio

2010)

or

How to: Configure and Run Scheduled Tests After Building Your Application

(Visual Studio 2012)

.