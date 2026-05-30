---
title: "Overview of Connection Strings & Permissions"
topic: "ssb-diagnose"
description: |
  09/10/2025

  To run SQL Server unit tests, you must connect to a database server by using one or two

  specific connection strings. Each connection string represents an account that has the specific

  pe
tags:
  - "ssb-diagnose"
  - "overview-of-connection-strings-permissions"
pubDate: 2025-12-01
---

09/10/2025

To run SQL Server unit tests, you must connect to a database server by using one or two

specific connection strings. Each connection string represents an account that has the specific

permissions that you must have to perform the task or set of tasks in a particular script as part

of the test. You can specify these strings in the

SQL Server Test Configuration

dialog box or by

manually editing the

file for your test project.

In the

SQL Server Test Configuration

dialog box, you can specify connection strings for each of

the following accounts.

(Required): a user account for running the test script. This connection

string should have the same credentials that you expect your users to have. This is

important because it ensures that the appropriate permissions have been applied to your

database. For more information, see

How to: Configure SQL Server unit test execution

.

In the

file for your test project, this is the

element.

(Optional): an account on the same database that has higher

permissions for running the pre-test action, post-test action, TestInitialize, and

TestCleanup scripts. These scripts set the database state and for the post-test action, can

be used to validate objects in the database. This connection string is also used to deploy

database changes and generate data.

In the

file for your test project, this element is the

element. If your SQL Server unit tests run the test script only, you don't have to specify a

privileged context.

The strings that you specify in the project configuration dialog box are stored in your test

project's

file. You could also edit that file directly and rebuild the project, after

７

Note

The execution context and privileged context only differ if you use SQL Server

authentication. If you use Windows authentication, the same credentials are used for both

connection strings.

```cmd
app.config
app.config
ExecutionContext
app.config
PrivilegedContext
```
