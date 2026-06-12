---
title: "CursorImplicitConversion Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The

  event class describes cursor-implicit conversion events that

  occur in application progr
tags:
  - "event-classes"
  - "cursorimplicitconversion-event-class"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The

event class describes cursor-implicit conversion events that

occur in application programming interfaces (APIs) or Transact-SQL cursors. Cursor implicit

conversion events occur when the SQL Server Database Engine executes a Transact-SQL

statement that is not supported by server cursors of the type requested. The Database Engine

returns an error that indicates the cursor type has changed.

Include the

event class in traces that are recording the performance

of cursors.

When this event class is included in a trace, the amount of overhead incurred depends on how

frequently cursors that require implicit conversion are used against the database during the

trace. If cursors are used extensively, the trace may significantly impede performance.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

Resulting cursor type. Values are:

1 = Keyset

2 = Dynamic

4 = Forward only

8 = Static

16 = Fast forward

2

Yes

ﾉ

Expand table
