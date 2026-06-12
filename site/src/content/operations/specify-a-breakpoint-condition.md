---
title: "Specify a Breakpoint Condition"
topic: "ssb-diagnose"
description: "09/10/2025 A breakpoint condition is a Transact-SQL expression that the debugger evaluates when the breakpoint is reached."
tags: ["ssb-diagnose","specify-a-breakpoint-condition"]
pubDate: "2025-12-01"
---

A breakpoint condition is a Transact-SQL expression that the debugger evaluates when the

breakpoint is reached. If the condition is satisfied and any specified hit count reached, the

debugger either breaks or performs the action specified for the breakpoint.

The expression specified must be a valid Transact-SQL expression that evaluates to a Boolean

value. For more information, see

Expressions.

If you specify a breakpoint condition with invalid syntax, a warning message appears

immediately. If you specify a condition with valid syntax but invalid semantics, a warning

message is displayed the first time the breakpoint is hit. In either case, the debugger breaks

execution when the invalid breakpoint is hit.

1. In the editor window, right-click the breakpoint glyph, and then select

on

the shortcut menu.

-or-

In the

window, right-click the breakpoint glyph, and then select

on

the shortcut menu.

2. In the

dialog box, select the

option and select

from the dropdown list.

3. Enter a valid Boolean expression for the.

4. Select

if you want to break when the expression evaluates to

, or select

if you want to break when the value of the expression changes.

７

Note

The debugger doesn't evaluate the Boolean expression until the first time the

breakpoint is reached. If you choose

, the debugger doesn't consider
