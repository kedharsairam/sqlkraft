---
title: "How to: Write a SQL Server Unit Test that Runs within the Scope of a Single Transaction"
topic: "ssb-diagnose"
description: |
  09/10/2025

  You can modify unit tests to run within the scope of a single transaction. If you take this

  approach, you can roll back any changes that the test enacted after the test ends. The

  followi
tags:
  - "ssb-diagnose"
  - "how-to-write-a-sql-server-unit-test-that-runs-within-the-scope-of-a-single-transaction"
pubDate: 2025-12-01
---

09/10/2025

You can modify unit tests to run within the scope of a single transaction. If you take this

approach, you can roll back any changes that the test enacted after the test ends. The

following procedures explain how to:

Create a transaction in your Transact-SQL test script that uses

and.

Create a transaction for a single test method in a test class.

Create a transaction for all test methods in a given test class.

For some procedures in this article, the Distributed Transaction Coordinator service must be

running on the computer on which you run unit tests. For more information, see the procedure

at the end of this article.

1. Open a unit test in the SQL Server Unit Test Designer. (Double-click the source code file

for the unit test to display the designer.)

2. Specify the type of script for which you want to create the transaction. For example, you

can specify pre-test, test, or post-test.

3. Enter a test script in the Transact-SQL editor.

4. Insert

and

statements, as shown in this simple

example. The example uses a database table that is named OrderDetails and that contains

50 rows of data:

```cmd
BEGIN TRANSACTION
ROLLBACK TRANSACTION
BEGIN TRANSACTION
ROLLBACK TRANSACTION
BEGIN
TRANSACTION
TestTransaction;
UPDATE
"OrderDetails"
SET
Quantity = Quantity + 10;
```
