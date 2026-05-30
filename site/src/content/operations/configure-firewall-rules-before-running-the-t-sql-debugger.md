---
title: "Configure firewall rules before running the T-SQL Debugger"
topic: "ssb-diagnose"
description: |
  09/09/2025

  Applies to:

  SQL Server

  Windows Firewall rules must be configured to enable Transact-SQL debugging when

  connected to an instance of the Database Engine that is running on a different com
tags:
  - "ssb-diagnose"
  - "configure-firewall-rules-before-running-the-t-sql-debugger"
pubDate: 2025-12-01
---

09/09/2025

Applies to:

SQL Server

Windows Firewall rules must be configured to enable Transact-SQL debugging when

connected to an instance of the Database Engine that is running on a different computer than

the Database Engine Query Editor.

The Transact-SQL debugger includes both server-side and client-side components. The server-

side debugger components are installed with each instance of the SQL Server Database Engine.

The client-side debugger components are included:

When you install Microsoft Visual Studio 2019 or later versions

When you install SQL Server Data Tools (SSDT) from the web download

There are no configuration requirements to run the Transact-SQL debugger when SQL Server

Data Tools is running on the same computer as the instance of the SQL Server Database

Engine. However, to run the Transact-SQL debugger when connected to a remote instance of

the Database Engine, program and port rules in the Windows Firewall must be enabled on both

computers. If you get errors attempting to open a remote debugging session, ensure the

following firewall rules are defined on your computer.

Use the

application to manage the firewall rules. In

both Windows 7 and Windows Server 2008 R2, open

, open

,

and select

. In Windows Server 2008 R2, you can also open

, expand

in the left pane, and expand

.

Ｕ

Caution

Enabling rules in the Windows Firewall can expose your computer to security threats that

the firewall is designed to block. Enabling rules for remote debugging unblocks the ports

and programs listed in this article.
