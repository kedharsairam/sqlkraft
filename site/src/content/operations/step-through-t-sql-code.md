---
title: "Step Through T-SQL Code"
topic: "ssb-diagnose"
description: |
  09/10/2025

  Applies to:

  SQL Server

  The Transact-SQL debugger enables you to control which Transact-SQL statements are run in a

  Database Engine Query Editor window. You can pause the debugger on ind
tags:
  - "ssb-diagnose"
  - "step-through-t-sql-code"
pubDate: 2025-12-01
---

09/10/2025

Applies to:

SQL Server

The Transact-SQL debugger enables you to control which Transact-SQL statements are run in a

Database Engine Query Editor window. You can pause the debugger on individual statements

and then view the state of the code elements at that point.

A breakpoint signals the debugger to pause execution on a specific Transact-SQL statement.

For more information about breakpoints, see

Transact-SQL breakpoints

.

In the Transact-SQL debugger, you can specify the following options for executing from the

current statement in Transact-SQL code:

Run to the next breakpoint.

Step into the next statement.

If the next statement invokes a Transact-SQL stored procedure, function, or trigger, the

debugger displays a new Query Editor window that contains the code of the module. The

window is in debug mode, and execution pauses on the first statement in the module.

You can then move through the module code, for example, by setting breakpoints or

stepping through the code.

Step over the next statement.

The next statement is executed. If the statement invokes a stored procedure, function, or

trigger, the module code runs until it finishes, returning the results to the calling code. If

you're confident there are no errors in a stored procedure, you can step over it. Execution

pauses on the statement that follows the call to the stored procedure, function, or trigger.

Step out of a stored procedure, function, or trigger.

Execution pauses on the statement that follows the call to the stored procedure, function,

or trigger.

Run from the current location to the current location of the pointer, and ignore all

breakpoints.
