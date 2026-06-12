---
title: "Using Test Conditions in SQL Server Unit Tests"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
    In a SQL Server unit test, one or more Transact-SQL test scripts are executed. The results can be
  
    evaluated within the Transact-SQL script and
  
    or
  
    used to return an error and
  
    fail the t
tags: ["ssb-diagnose","using-test-conditions-in-sql-server-unit-tests"]
pubDate: "2025-12-01"
---

In a SQL Server unit test, one or more Transact-SQL test scripts are executed. The results can be

evaluated within the Transact-SQL script and

or

used to return an error and

fail the test, or test conditions can be defined in the test to evaluate the results. The test returns

an instance of the

SqlExecutionResult

class. The instance of this class contains one or more

DataSets, the execution time, and the rows affected by the script. All of this information is

collected during execution of the script. These results can be evaluated by using test

conditions. SQL Server Data Tools provides a set of predefined test conditions. You can also

create and use custom conditions; see

Custom Test Conditions for SQL Server Unit Tests.

The following table lists the predefined test conditions that you can add by using the Test

Conditions pane in the SQL Server Unit Test Designer.

Data

Checksum

Fails if the checksum of the result set returned from the Transact-SQL script doesn't

match the expected checksum. For more information, see

Specifying a Data Checksum.

Note:

This test condition isn't recommended if you're returning data that varies between

test runs. For example, if your result set contains generated dates or times, or contains

identity columns, your tests fail because the checksum is different on each run.

Empty

ResultSet

Fails if the result set returned from the Transact-SQL script isn't empty.

Execution

Time

Fails if the Transact-SQL test script takes longer than expected to execute. The default

execution time is 30 seconds.

The execution time applies to the test script test only, not to the pre-test script or the

post-test script.

Expected

Schema

Fails if the columns and data types of the result set don't match those specified for the

test condition. You must specify a schema through the properties of the test condition.

For more information, see

Specifying an Expected Schema.

Inconclusive

Always produces a test with a result of Inconclusive. This is the default condition added

to every test. This test condition is included to indicate that test verification hasn't been

ﾉ

Expand table

```cmd
THROW
RAISERROR
```
