---
title: "SqlPipe Object"
topic: "clr-integration"
description: "SqlPipe object In previous versions of SQL Server, it was common to write a stored procedure (or an extended stored procedure) that sent results or o"
tags: ["clr-integration","sqlpipe-object"]
pubDate: 2025-12-01
---

SqlPipe object

In previous versions of SQL Server, it was common to write a stored procedure (or an extended

stored procedure) that sent results or output parameters to the calling client.

In a Transact-SQL stored procedure, any

statement that returns zero or more rows

sends the results to the connected caller's "pipe."

For common language runtime (CLR) database objects running in SQL Server, you can send

results to the connected pipe using the

methods of the

object. Access the

property of the

object to obtain the

object. The

class is

conceptually similar to the

class found in ASP.NET.

For more information, see

Microsoft.SqlServer.Server.SqlPipe.

The

object has a

method, which has three overloads. They are:

The

method sends data straight to the client or caller. It's usually the client that consumes

the output from the

, but with nested CLR stored procedures, the output consumer can

also be a stored procedure. For example,

calls

with the

command text.

is also a managed stored procedure. If

now calls

, the row is sent to the reader in

, not the

client.

The

method sends a string message that appears on the client as an information

message, equivalent to

in Transact-SQL. It can also send a single-row result-set using

, or a multi-row result-set using a.

The

object also has an

method. This method can be used to execute a

command (passed as a

object) and send results directly back to the caller. If there

are errors in the command that was submitted, exceptions are sent to the pipe, and a copy is

sent to calling managed code. If the calling code doesn't catch the exception, it propagates up

```sql
SELECT
Send
SqlPipe
Pipe
SqlContext
SqlPipe
SqlPipe
Response
SqlPipe
Send void Send(string message) void Send(SqlDataReader reader) void Send(SqlDataRecord record)
Send
SqlPipe
Procedure1
SqlCommand.ExecuteReader()
EXEC Procedure2
Procedure2
Procedure2
SqlPipe.Send(SqlDataRecord)
Procedure1
Send
PRINT
SqlDataRecord
SqlDataReader
SqlPipe
ExecuteAndSend
SqlCommand
```
