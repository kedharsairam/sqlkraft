---
title: "PowerShell Cmdlets"
topic: "high-availability"
description: "Microsoft PowerShell is a task-based command-line shell and scripting language designed especially for system administration. Always On availability g"
tags: ["high-availability","powershell-cmdlets"]
pubDate: 2025-12-01
---

Microsoft PowerShell is a task-based command-line shell and scripting language designed

especially for system administration. Always On availability groups provides a set of PowerShell

cmdlets in SQL Server that enable you to deploy, manage, and monitor availability groups,

availability replicas, and availability databases.

Description

SqlAlwaysOn

Disables the Always On availability groups feature

on a server instance.

The server instance that is

specified by the

,

, or

parameter. (Must be an

edition of SQL Server that

supports Always On

availability groups.)

７

Note

A PowerShell cmdlet can complete by successfully initiating an action. This does not

indicate that the intended work, such as the fail over of an availability group, has

completed. When scripting a sequence of actions, you might have to check the status of

actions, and wait for them to complete.

７

Note

For a list of topics in SQL Server Books Online that describe how to use cmdlets to

perform Always On availability groups tasks, see the "Related Tasks" section of.

ﾉ

Expand table
