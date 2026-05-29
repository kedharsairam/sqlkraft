---
title: "How to: Open a SQL Server Unit Test to Edit"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  After you create a SQL Server unit test, you use the
  
  SQL Server Unit Test Designer
  
  to add
  
  Transact-SQL statements and test conditions. The tests created by using the designer generate
  
  
tags:
  - "ssb-diagnose"
  - "how-to-open-a-sql-server-unit-test-to-edit"
pubDate: 2025-12-01
---

09/10/2025

After you create a SQL Server unit test, you use the

SQL Server Unit Test Designer

to add

Transact-SQL statements and test conditions. The tests created by using the designer generate

C# or Visual Basic code. This code is what executes when your test runs.

If you're satisfied with your test, you can run it as it's. If you want to add more functionality to

this unit test, you can edit its code. This code resides in a

or

file in your test project.

For more information, see

SQL Server Unit Test Files

. You can also customize your tests by

creating new test conditions. For more information, see

How to: Create Test Conditions for the

Database Unit Test Designer (Visual Studio 2010)

.

In

, right-click the source-code file that contains the SQL Server unit test, and

then select

.

The test method of the unit test appears in the main editing window of Visual Studio when the

file opens.

1. Run a unit test. For more information, see the "Run SQL Server Unit Tests" section in

Walkthrough: Create and run a SQL Server unit test

.

2. In the Test View window, right-click the test, and then select

.

７

Note

If you delete a test method by editing the

or

file, the test method still appears in

the

SQL Server Unit Test Designer

. This situation occurs because the InitializeComponent

method of the test class still contains member variables for that test. Although the test

appears in the designer, you can't run the test because its code is no longer present. To

regenerate the test method for this test, edit the Transact-SQL in the editor, and then

either save the

or

test file or rebuild the test project.

```cmd
.cs
.vb
.cs
.vb
.cs
```