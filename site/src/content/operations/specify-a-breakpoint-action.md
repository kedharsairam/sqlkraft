---
title: "Specify a Breakpoint Action"
topic: "ssb-diagnose"
description: "09/09/2025 A breakpoint action specifies a custom task that the Transact-SQL debugger performs for a breakpoint. If the specified hit count is reached and a specified breakp"
tags: ["ssb-diagnose","specify-a-breakpoint-action"]
pubDate: "2025-12-01"
---

A breakpoint action specifies a custom task that the Transact-SQL debugger performs for a

breakpoint. If the specified hit count is reached and a specified breakpoint condition is

satisfied, the debugger performs the action specified for the breakpoint.

The default action for a breakpoint is to break execution when both the hit count and

breakpoint condition are satisfied. The primary use of an action in the Transact-SQL debugger

is to print information to the debugger

window.

The message is specified in the

box, and is specified

as a text string that includes expressions containing information from the Transact-SQL being

debugged. Expressions include:

A Transact-SQL expression contained in curly braces (

). The expressions can include

Transact-SQL variables, parameters, and built-in functions. Examples include

,

,

, or.

One of the following keywords:

returns the name of the stored procedure or user-defined function where the

breakpoint is set. If the breakpoint is set in the editor window,

returns the

name of the script file being edited.

and

return the same

information in the Transact-SQL debugger.

returns the name of the unit of Transact-SQL code that called a stored

procedure or function. If the breakpoint is in the editor window,

returns. If the breakpoint is in a stored procedure or user-defined function

called from the code in the editor window,

returns the name of the file being

edited. If the breakpoint is in a stored procedure or user-defined function called from

another stored procedure or function,

returns the name of the calling

procedure or function.

returns the call stack of functions in the chain that called the current stored

procedure or user-defined function. If the breakpoint is in the editor window,

returns the name of the script file being edited.

```cmd
{}
{@MyVariable}
{@NameParameter}
{@@SPID}
{SERVERPROPERTY('ProcessID')}
```
