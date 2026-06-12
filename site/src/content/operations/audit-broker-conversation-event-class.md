---
title: "Audit Broker Conversation Event Class"
topic: "event-classes"
description: "creates an event to report audit messages related to Service Broker dialog security. Desc"
tags: ["event-classes","audit-broker-conversation-event-class"]
pubDate: 2025-12-01
---

creates an

event to report audit messages related to

Service Broker dialog security.

Description

The name of the client application that

created the connection to an instance of. This column is populated with

the values passed by the application rather

than the displayed name of the program.

10

Yes

The message sequence number of the

message.

52

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

statement has been issued for a given

instance. SQL Server Profiler displays the

name of the database if the

data column is captured in the trace and

the server is available. Determine the value

for a database by using the DB_ID function.

3

Yes

The SQL Server error number, if this event

reports an error.

31

No

The type of event class captured. Always

for.

27

No

ﾉ

Expand table

```cmd
Audit Broker Conversation
ApplicationName
BigintData1
ClientProcessID
DatabaseID
```
