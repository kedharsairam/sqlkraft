---
title: "Using T-SQL Assertions in SQL Server Unit Tests"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  In a SQL Server unit test, a Transact-SQL test script runs and returns a result. Sometimes, the
  
  results are returned as a results set. You can validate results by using test conditions. F
tags:
  - "ssb-diagnose"
  - "using-t-sql-assertions-in-sql-server-unit-tests"
pubDate: 2025-12-01
---

09/10/2025

In a SQL Server unit test, a Transact-SQL test script runs and returns a result. Sometimes, the

results are returned as a results set. You can validate results by using test conditions. For

example, you can use a test condition to check how many rows were returned in a specific

result set or to verify how long a particular test took to run. For more information about test

conditions, see

Use test conditions in SQL Server unit tests

.

Instead of using test conditions, you can also use Transact-SQL assertions, which are

or

statements in a Transact-SQL script. In certain circumstances, you might prefer to

use a Transact-SQL assertion instead of a test condition.

You should consider the following points before you decide to validate data either by using

Transact-SQL assertions or by using test conditions.

. It's faster to run a Transact-SQL assertion on the server than to first move

data to a client computer and manipulate it locally.

. You might prefer a particular language based on your current

expertise and therefore choose Transact-SQL assertions or C# or Visual Basic test

conditions.

. In some instances, you can build more complex tests in C# or

Visual Basic and validate your tests on the client.

. It's often simpler to use a pre-defined test condition than to write the

equivalent script in Transact-SQL.

. If you already have code that performs validation, you can use

it in a SQL Server unit test instead of using test conditions.

To mark a SQL Server unit test method with expected exceptions, add the following attribute:

```cmd
THROW
RAISERROR
```