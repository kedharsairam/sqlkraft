---
title: "TransactionLog Event Class"
topic: "event-classes"
description: "Use the TransactionLog event class to monitor activity in the transaction logs in an instance"
tags: ["event-classes","transactionlog-event-class"]
pubDate: 2025-12-01
---

Use the TransactionLog event class to monitor activity in the transaction logs in an instance of

the SQL Server Database Engine.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

BinaryData

Binary value dependent on the event class

captured in the trace.

2

Yes

ClientProcessID

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process.

9

Yes

DatabaseID

ID of the database where the data is being

logged.

3

Yes

DatabaseName

Name of the database in which the user

statement is running.

35

Yes

EventClass

Type of event = 54.

27

No

EventSequence

Sequence of a given event within the request.

51

No

EventSubClass

Type of event subclass.

21

Yes

GroupID

ID of the workload group where the SQL Trace

event fires.

66

Yes

HostName

Name of the computer on which the client is

running. This data column is populated if the

client provides the host name. To determine the

host name, use the HOST_NAME function.

8

Yes

ﾉ

Expand table
