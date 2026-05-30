---
title: "Run the T-SQL Debugger"
topic: "ssb-diagnose"
description: |
  09/10/2025

  Applies to:

  SQL Server

  You can start the Transact-SQL debugger after you open a Database Engine Query Editor

  window. You can set options to customize how the debugger runs and run your
tags:
  - "ssb-diagnose"
  - "run-the-t-sql-debugger"
pubDate: 2025-12-01
---

09/10/2025

Applies to:

SQL Server

You can start the Transact-SQL debugger after you open a Database Engine Query Editor

window. You can set options to customize how the debugger runs and run your Transact-SQL

code in debug mode until you stop the debugger.

The requirements to start the Transact-SQL debugger are as follows:

If the Database Engine Query Editor is connected to an instance of the Database Engine

on another computer, you must configure the debugger for remote debugging. For more

information, see

Configure firewall rules before running the Transact-SQL debugger

.

The Database Engine Query Editor window must be connected by using either a Windows

Authentication or SQL Server Authentication login that is a member of the

fixed

server role.

The Database Engine Query Editor window must be connected to an instance of the SQL

Server Database Engine. You can't run the debugger when the Query Editor window is

connected to an instance that is in single-user mode.

We recommend debugging Transact-SQL code on a test server, not a production server, for the

following reasons:

Debugging is a highly privileged operation. Therefore, only members of the

fixed server role are allowed to debug in SQL Server.

Debugging sessions often run for long periods of time while you investigate the

operations of several Transact-SQL statements. Locks, such as update locks, that are

acquired by the session might be held for extended periods, until the session is ended or

the transaction committed or rolled back.

Starting the Transact-SQL debugger puts the Query Editor window into debug mode. When the

Query Editor window enters debug mode, the debugger pauses at the first line of code. You

can then step through the code, pause the execution on specific Transact-SQL statements, and

use the debugger windows to view the current execution state. You can start the debugger by

selecting the

button on the

toolbar or selecting

on the

menu.
