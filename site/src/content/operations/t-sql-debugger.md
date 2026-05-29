---
title: "T-SQL Debugger"
topic: "ssb-diagnose"
description: |
  09/15/2025
  
  Applies to:
  
  SQL Server
  
  The Transact-SQL debugger helps you find errors in Transact-SQL code by investigating the
  
  run-time behavior of the code. After you set the Database Engine Query E
tags:
  - "ssb-diagnose"
  - "t-sql-debugger"
pubDate: 2025-12-01
---

09/15/2025

Applies to:

SQL Server

The Transact-SQL debugger helps you find errors in Transact-SQL code by investigating the

run-time behavior of the code. After you set the Database Engine Query Editor window to

debug mode, you can pause execution on specific lines of code and inspect information and

data that is used by or returned by those Transact-SQL statements.

T-SQL debugging is available in

SQL Server Data Tools

for Visual Studio.

The Transact-SQL debugger provides the following options that you can use to navigate

through Transact-SQL code when the Database Engine Query Editor window is in debug mode:

Set breakpoints on individual Transact-SQL statements.

A breakpoint specifies a point at which you want execution to pause so you can examine

data. When you start the debugger, it pauses on the first line of code in the Query Editor

window. To run to the first breakpoint, use

. You can also use

to run to

the next breakpoint from any location at which the window is currently paused. You can

edit breakpoints to specify actions such as the conditions under which the breakpoint

should pause execution, information to print to the

window, and change the

location of the breakpoint.

Step into the next statement.

This option enables you to navigate through a set of statements one by one, and to

observe their behavior as you go.

Step either into or over a call to a stored procedure or function.

If you're sure there are no errors in a stored procedure, you can step over it. The

procedure is executed in full, and the results are returned to the code.

If you want to debug a stored procedure or function, you can step into the module. A

new Database Engine Query Editor window opens that populates with the source code for

the module. The window is in debug mode, and execution pauses on the first statement

in the module. You can then navigate through the module code, for example, by setting

breakpoints or stepping through the code.