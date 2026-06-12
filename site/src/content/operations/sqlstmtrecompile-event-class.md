---
title: "SQL:StmtRecompile Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","sqlstmtrecompile-event-class"]
pubDate: 2025-12-01
---

SQL:StmtRecompile Event Class

The SQL:StmtRecompile event class indicates statement-level recompilations caused by all

types of batches: stored procedures, triggers, ad hoc batches, and queries. Queries can be

submitted by using sp_executesql, dynamic SQL, Prepare methods, Execute methods, or similar

interfaces. The SQL:StmtRecompile event class should be used instead of the SP:Recompile

event class.

Description

ApplicationName

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the values

passed by the application rather than the

displayed name of the program

10

Yes

ClientProcessID

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the process ID.

9

Yes

DatabaseID

ID of the database in which the stored

procedure is running. Determine the value for a

database by using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the stored

procedure is running.

35

Yes

EventSequence

The sequence of an event within the request.

51

No

EventSubClass

Describes the cause of the recompilation:

1 = Schema changed

2 = Statistics changed

3 = Deferred compile

4 = Set option changed

21

Yes

SQL:StmtRecompile Event Class Data Columns

ﾉ

Expand table
