---
title: "T-SQL Debugger Information"
topic: "ssb-diagnose"
description: |
  09/09/2025
  
  Applies to:
  
  SQL Server
  
  Every time that the debugger pauses execution on a specific Transact-SQL statement, you can
  
  use the various debugger windows to view the current execution state.
  
tags:
  - "ssb-diagnose"
  - "t-sql-debugger-information"
pubDate: 2025-12-01
---

09/09/2025

Applies to:

SQL Server

Every time that the debugger pauses execution on a specific Transact-SQL statement, you can

use the various debugger windows to view the current execution state.

In debugger mode, the debugger opens windows next to the Query Editor window. The

debugger displays its information in the selected windows. Each of the debugger windows has

tabs that you can select to control which set of information is displayed in the window. The

,

,

, and

tabs are contained in one window. The

,

,

, and

tabs are contained in one window. The

and

windows are displayed separately.

By default, not all of these tabs or windows are active. To open a particular window, on the

menu, select

, and then select the window you want to view.

Expressions are Transact-SQL clauses that evaluate to a single, scalar value, such as variables or

parameters. The debugger window can display the data values that are currently assigned to

expressions in up to five tabs or windows:

,

,

, and

.

The

window displays information about the local variables in the current scope of the

Transact-SQL debugger. The set of expressions that are listed in the

window changes as

the debugger runs through the different parts of the code.

The expressions in the four

windows aren't limited to just listing the identifier of a

variable. You can specify a Transact-SQL expression that evaluates to a single value, such as

adding a number to a variable, or a

statement that evaluates to a single value.

Examples include:

７

Note

The previous descriptions apply to the default locations of the debugger windows. You

can drag a tab to move it from one window to another, or you can undock a tab to create

a new window for selected tabs.

```cmd
SELECT
```