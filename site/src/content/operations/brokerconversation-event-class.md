---
title: "Broker:Conversation Event Class"
topic: "event-classes"
description: "generates a event to report the progress of a Service Broker conversation."
tags: ["event-classes","brokerconversation-event-class"]
pubDate: "2025-12-01"
---

generates a

event to report the progress of a Service Broker

conversation.

Description

The name of the client application that

created the connection to an instance of. This column is populated with

the values passed by the application

instead of the displayed name of the

program.

10

Yes

The ID assigned by the host computer to

the process where the client application is

running. This data column is populated if

the client process ID is provided by the

client.

9

Yes

The ID of the database that is specified by

the

statement. If no

statement was issued, this

column specifies the ID of the default

database. SQL Server Profiler displays the

name of the database if the

data column is captured in the trace and

the server is available. Determine the value

for a database by using the

function.

3

Yes

The type of event class captured. Always

for.

27

No

Sequence number for this event.

51

No

The type of event subclass. This provides

more information about each event class.

21

Yes

The conversation ID of the dialog. This

identifier is transmitted as part of the

54

No

ﾉ

Expand table

```cmd
Broker:Conversation
ApplicationName
ClientProcessID
DatabaseID
USE <database>
```
