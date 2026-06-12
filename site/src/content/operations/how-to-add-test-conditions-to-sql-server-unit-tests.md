---
title: "How to: Add Test Conditions to SQL Server Unit Tests"
topic: "ssb-diagnose"
description: |
  09/10/2025
          
            You can add test conditions to a SQL Server unit test by using the
          
            SQL Server Unit Test
          
            . When you save the test class, the test conditions are automatically saved in your test
          
            project
tags: ["ssb-diagnose","how-to-add-test-conditions-to-sql-server-unit-tests"]
pubDate: 2025-12-01
---

You can add test conditions to a SQL Server unit test by using the

Unit Test. When you save the test class, the test conditions are automatically saved in your test

project as C# or Visual Basic code in the source-code file containing the test class. After you

save a test condition, you can edit it either in the

Unit Test Designer

or in its

source-code file.

1. Open a SQL Server unit test in the

Unit Test Designer.

The name of the test you opened is displayed in the navigation bar at the top of the SQL

Server Unit Test Designer. By using the navigation bar, you can select the different test

methods that are in your test class.

2. In the navigation bar, select the test method to which you want to add test conditions, or

select.

Common scripts don't belong to a particular unit test. Rather, they precede or follow unit

tests in the test class. For more information, see

Scripts in SQL Server Unit Tests.

3. In the navigation bar, select the Transact-SQL script to which you want to add test

conditions. You can add test conditions to the pre-test, test, or post-test script.

The Transact-SQL script for that test appears in the Transact-SQL editor and its test

conditions appear in the

pane.

4. In the

selection list, select a test condition and then select

(+).

The test condition is added to the unit test method.

You can reorder test conditions within a test method by selecting a test condition and

then selecting the up and down arrows in the

pane.

5. Select the test condition you just added and view the

window.

Configure the test condition in the Properties window. For example, you can change the

property of an Execution Time test condition. If you set this property, you
