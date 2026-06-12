---
title: "Specify a Breakpoint Filter"
topic: "ssb-diagnose"
description: |
  09/10/2025

  Applies to:

  SQL Server

  A breakpoint filter limits the breakpoint to acting only on specified computers, operating

  system processes, and threads. Breakpoint filters are typically used wh
tags:
  - "ssb-diagnose"
  - "specify-a-breakpoint-filter"
pubDate: 2025-12-01
---

09/10/2025

SQL Server

A breakpoint filter limits the breakpoint to acting only on specified computers, operating

system processes, and threads. Breakpoint filters are typically used when debugging parallel

applications.

Breakpoint filters aren't typically used with the Transact-SQL debugger because Transact-SQL

scripts and stored procedures aren't parallel applications.

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

options and select

from the dropdown list.

3. Use the

box to specify computers by name, or operating system processes and

threads by either name or ID number:

is the computer running the instance of the Database Engine.

, and

are the operating system process running the instance

of the Database Engine.

and

are the operating system thread running the Transact-

SQL batch, procedure, or function in the instance of the Database Engine.

4. Select

to implement the changes.
