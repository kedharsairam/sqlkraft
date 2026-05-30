---
title: "Broker:Message Undeliverable Event Class"
topic: "event-classes"
description: |
  Article

  •

  03/31/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  SQL Server generates a

  event when Service Broker is unable to

  retain a received message that should have been delivered t
tags:
  - "event-classes"
  - "brokermessage-undeliverable-event-class"
pubDate: 2025-12-01
---

Article

•

03/31/2025

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server generates a

event when Service Broker is unable to

retain a received message that should have been delivered to a service in this instance. For

messages that should have been forwarded, see

Broker:Forwarded Message Dropped Event

Class

.

Description

The name of the client application that

created the connection to an instance of

SQL Server. This column is populated with

the values passed by the application rather

than the displayed name of the program.

10

Yes

The sequence number of the undeliverable

message.

52

No

The sequence number of the last message

successfully acknowledged.

53

No

The ID assigned by the host computer to

the process where the client application is

running. This data column is populated if

the client process ID is provided by the

client.

9

Yes

The ID of the database specified by the

statement, or the ID of the

default database if no

statement was issued for a given instance.

SQL Server Profiler displays the name of

the database if the

data

column is captured in the trace and the

server is available. Determine the value for

a database by using the

function.

3

Yes

ﾉ

Expand table

```cmd
Broker:Message Undeliverable
Application
Name
BigintData1
BigintData2
ClientProcessID
```
