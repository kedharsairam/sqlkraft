---
title: "Scripts in SQL Server Unit Tests"
topic: "ssb-diagnose"
description: |
  09/09/2025

  Each SQL Server unit test contains a single pre-test action, test action, and post-test action.

  Each of these actions in turn contains:

  A Transact-SQL script that executes on a database.
tags:
  - "ssb-diagnose"
  - "scripts-in-sql-server-unit-tests"
pubDate: 2025-12-01
---

09/09/2025

Each SQL Server unit test contains a single pre-test action, test action, and post-test action.

Each of these actions in turn contains:

A Transact-SQL script that executes on a database.

Zero or more test conditions that evaluate the results returned from script execution.

The Transact-SQL test script in the test action is the only component that you must include in

every SQL Server unit test. In addition to the test script itself, you probably also want to specify

test conditions to verify whether the test script returned the value or set of values that you

expected. The test action exercises or changes a particular object in that database and then

evaluates that change.

For each test action, you can include one pre-test action and one post-test action. Similar to

the test action, each pre-test action and each post-test action contains one Transact-SQL script

and zero or more test conditions. You can use a pre-test action to make sure that the database

is in a state that allows your test action to run and return meaningful results. For example, you

can use a pre-test action to verify that a table contains data before the test script performs an

operation on that data.

After the pre-test action prepares the database and the test action returns meaningful results,

the post-test action can be used to return the database to the state that it was in before the

pre-test action ran. Or, in some cases, you might use the post-test action to validate the results

of the test action. This is because the post-test action can have greater database privileges

than the test action. For more information, see

Overview of connection strings and

permissions.

In addition to these three actions, there are also two test scripts (referred to as common

scripts), which run before and after every SQL Server unit test runs. As a result, up to five

Transact-SQL scripts can be run during execution of a single SQL Server unit test. Only the

Transact-SQL script that is contained within the test action is required; the common scripts and

the pre-test and post-test action scripts are optional.

The following table provides a complete list of scripts that are associated with any SQL Server

unit test.

ﾉ

Expand table
