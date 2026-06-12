---
title: "Debug"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  SQL Server provides support for debugging Transact-SQL and common language runtime (CLR)

  objects in the database. The key aspects of debugging in SQL
tags:
  - "clr-integration"
  - "debug"
pubDate: 2025-12-01
---

Article

•

12/30/2024

SQL Server

provides support for debugging Transact-SQL and common language runtime (CLR)

objects in the database. The key aspects of debugging in SQL Server are the ease of setup and

use, and the integration of the SQL Server debugger with the Microsoft Visual Studio

debugger. Furthermore, debugging works across languages. Users can step seamlessly into

CLR objects from Transact-SQL, and vice versa.

The Transact-SQL debugger in SQL Server Management Studio can't be used to debug

managed database objects, but you can debug the objects by using the debuggers in Visual

Studio. Managed database object debugging in Visual Studio supports all common debugging

features, such as

step into

and

step over

statements within routines executing on the server.

Debuggers can set breakpoints, inspect the call stack, inspect variables, and modify variable

values while debugging.

Debugging is a highly privileged operation, and therefore only members of the

fixed

server role are allowed to do so in SQL Server.

The following restrictions apply while debugging:

Debugging CLR routines is restricted to one debugger instance at a time. This limitation

applies because all CLR code execution freezes when a break point is hit, and execution

doesn't continue until the debugger advances from the break point. However, you can

continue debugging Transact-SQL in other connections. Although Transact-SQL

debugging doesn't freeze other executions on the server, it can cause other connections

to wait by holding a lock.

Existing connections can't be debugged, only new connections, as SQL Server requires

information about the client and debugger environment before the connection can be

made.

We recommend therefore that Transact-SQL and CLR code is debugged on a test server, and

not on a production server.
