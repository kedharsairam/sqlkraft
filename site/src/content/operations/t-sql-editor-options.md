---
title: "T-SQL Editor Options"
topic: "ssb-diagnose"
description: |
  09/09/2025
          
            This article describes some of the options of the Transact-SQL Editor. To set these options, go
          
            to the
          
            dialog through the
          
            >
          
            menu.
          
            Description
          
            The default value of
          
            indicates that SQL
tags: ["ssb-diagnose","t-sql-editor-options"]
pubDate: 2025-12-01
---

This article describes some of the options of the Transact-SQL Editor. To set these options, go

to the

dialog through the

>

menu.

Description

The default value of

indicates that SQL Server waits for results until all

results are received. Provide a value greater than

if you want SQL

Server to halt the query after it obtains the specified number of rows. To

turn off this option (so that all rows are returned), specify.

The default value of 2,147,483,647 bytes indicates that SQL Server

provides a complete data field up to the limit of the

,

,

, and

data fields. It doesn't affect the XML

data type. Provide a smaller number to limit results when there are large

values. Columns greater than the provided number are truncated.

This value indicates the number of seconds to wait before canceling the

query. A value of

indicates an infinite wait, or no time-out.

Select this checkbox to open new queries in SQLCMD mode. This

checkbox is visible only when you open the dialog through the

menu.

When you select this option, be aware of the following limitations:

- IntelliSense in the Database Engine Query Editor is turned off.

- Because the Query Editor doesn't run from the command line, you can't

pass in command-line parameters such as variables.

- Because the Query Editor can't respond to operating-system prompts,

you must be careful not to run interactive statements.

This property stops the message that indicates the number of rows

affected by a Transact-SQL statement from being returned as part of the

results. For more information, see

SET NOCOUNT.

When the value is

, this property tells SQL Server to compile each

batch of Transact-SQL statements but not to run them. When the value is

ﾉ

Expand table

```cmd
SET ROWCOUNT
0
0
SET ROWCOUNT 0
SET TEXTSIZE
```
