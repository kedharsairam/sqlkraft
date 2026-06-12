---
title: "Interpreting SQL Server Unit Test Results"
topic: "ssb-diagnose"
description: |
  09/10/2025

  When you run a SQL Server unit test, test results are automatically produced, saved to disk, and

  summarized in the

  window. As soon as you start a test run, the

  window appears and displa
tags:
  - "ssb-diagnose"
  - "interpreting-sql-server-unit-test-results"
pubDate: 2025-12-01
---

09/10/2025

When you run a SQL Server unit test, test results are automatically produced, saved to disk, and

summarized in the

window. As soon as you start a test run, the

window appears and displays the progress of the test run. This display includes tests that are

running and tests that have completed.

To see detailed information about a test result, double-click it in the

window to

display the

page. For more information about a test result, double-click it.

For more information about how to change the display of the

window, see

How to:

Add or Remove Columns in Test Windows (Visual Studio 2010)

or

How to: Add or Remove

Columns in Test Windows (Visual Studio 2012).

Results of unit tests are automatically stored on your hard disk in files that have the extension. A

file is an XML file that contains the details of a test run. You can load

files

from previous test runs to review the results from the test runs or to rerun earlier tests. For

more information, see

How to: Rerun a Test (Visual Studio 2010).

If your team is using a Azure DevOps Server team project to help manage its work, you can

also publish your test data to a SQL Server database known as an operational store.

For more information about how to save test results, reuse them, and share them with your

team, see

How to: Save and Open Test Results in Visual Studio 2010

or

How to: Save and Open

Test Results in Visual Studio 2012.

Run SQL Server unit tests

７

Note

You can't run unit tests remotely.

```cmd.trx.trx.trx
```
