---
title: "How to: Configure SQL Server Unit Test Execution"
topic: "ssb-diagnose"
description: |
  09/10/2025
          
            By configuring your test project, you can specify several settings that control aspects of how
          
            your SQL Server unit tests are run. These configuration settings are stored in your test pro
tags: ["ssb-diagnose","how-to-configure-sql-server-unit-test-execution"]
pubDate: 2025-12-01
---

By configuring your test project, you can specify several settings that control aspects of how

your SQL Server unit tests are run. These configuration settings are stored in your test project's

app.config file. If you edit this file directly, the new values appear in the test configuration

dialog box.

Your solution can contain multiple test projects. Each test project contains one app.config file

(that is, one set of configuration settings). As a result, your solution can contain different sets of

unit tests (one set for each test project) that are configured to run differently.

These settings control how your test connects to the database that you test, how you deploy a

schema from a database project to that database:. You use this setting to specify the connection strings that are

used to connect to the database that you're testing. For more information, see

Specify

Connection Strings. A database project is an offline representation of your database.

The database project represents the structure of your database objects but contains no

data. After you make schema changes in a database project, you can test them in an

actual database. In the schema deployment step, database objects that you want to test

are copied from your database project into the database on which you run tests. For

more information about schema deployment, see

Deploy a Database Schema.

７

Note

Tests don't run in the solution folder but in a separate folder on the local hard disk.

Although you can configure aspects of test deployment, you typically don't need to

configure them for unit tests. For more information about test deployment, see.
