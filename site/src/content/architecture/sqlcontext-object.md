---
title: "SqlContext Object"
topic: "clr-integration"
description: |
  SqlContext object

  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  You invoke managed code in the server when you call a procedure or function, when you call a

  method on a common language runtime (C
tags:
  - "clr-integration"
  - "sqlcontext-object"
pubDate: 2025-12-01
---

SqlContext object

Article

•

12/30/2024

Applies to:

SQL Server

You invoke managed code in the server when you call a procedure or function, when you call a

method on a common language runtime (CLR) user-defined type, or when your action fires a

trigger defined in any of the .NET Framework languages. Because execution of this code is

requested as part of a user connection, access to the context of the caller from the code

running in the server is required. In addition, certain data access operations might only be valid

if run under the context of the caller. For example, access to inserted and deleted pseudo-

tables used in trigger operations is only valid under the context of the caller.

The context of the caller is abstracted in a

object. For more information, see

Microsoft.SqlServer.Server.SqlContext

.

provides access to the following components.

Description

This object represents the

pipe

through which results flow to the client. For more

information, see

SqlPipe object

.

This object can only be retrieved from within a CLR trigger. It provides information

about the operation that caused the trigger to fire and a map of the columns that

were updated. For more information, see

SqlTriggerContext object

.

This property is used to determine context availability.

This property is used to retrieve the Windows identity of the caller.

Query the

class to see if the currently executing code is running in-process, by

checking the

property of the

object. The

property is

read-only, and returns

if the calling code is running inside SQL Server and if other

members can be accessed. If the

property returns

, all the other

members throw an

, if used. If

returns

, any attempt to open a connection object that has "context connection=true" in the

connection string fails.

ﾉ

Expand table

```sql
SqlContext
SqlContext
SqlPipe
SqlTriggerContext
IsAvailable
WindowsIdentity
SqlContext
IsAvailable
SqlContext
IsAvailable
True
SqlContext
IsAvailable
False
SqlContext
InvalidOperationException
IsAvailable
False
```
