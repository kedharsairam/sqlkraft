---
title: "Specify a Hit Count"
topic: "ssb-diagnose"
description: |
  09/09/2025

  Applies to:

  SQL Server

  A breakpoint hit count is a counter that the Transact-SQL debugger increments each time the

  breakpoint is reached. If the specified hit count is reached and any s
tags:
  - "ssb-diagnose"
  - "specify-a-hit-count"
pubDate: 2025-12-01
---

09/09/2025

SQL Server

A breakpoint hit count is a counter that the Transact-SQL debugger increments each time the

breakpoint is reached. If the specified hit count is reached and any specified breakpoint

condition is satisfied, the debugger performs the action specified for the breakpoint.

By default, execution breaks every time a breakpoint is hit. You can choose between the

following options:

Break always (the default)

Break when the hit count equals a specified value

Break when the hit count equals a multiple of a specified value

Break when the hit count is greater than or equal to a specified value

Breakpoint hit counts are incremented within the scope of a debugging session. All hit counts

are set to zero at the start of each debugging session.

To track the number of times a breakpoint is hit, without breaking execution, specify a hit count

with a high value so the breakpoint never breaks.

The default action for a breakpoint is to break execution when both the hit count and

breakpoint condition are satisfied. For information about specifying other actions, see

Specify a

breakpoint action.

1. In the editor window, right-click the breakpoint glyph, and then select

on

the shortcut menu.

-or-

In the

window, right-click the breakpoint glyph, and then select

on

the shortcut menu.

2. Select the

option, and select

from the dropdown list.

3. Select the break option from the dropdown list:

,

, or.
