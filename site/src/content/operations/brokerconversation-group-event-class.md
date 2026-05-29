---
title: "Broker:Conversation Group Event Class"
topic: "event-classes"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  SQL Server generates a
  
  event when Service Broker creates a new
  
  conversation group or drops an existing conversation group
tags:
  - "event-classes"
  - "brokerconversation-group-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server generates a

event when Service Broker creates a new

conversation group or drops an existing conversation group.

Description

The name of the client application that

created the connection to an instance of

SQL Server. This column is populated with

the values passed by the application

rather than the displayed name of the

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

The ID of the database specified by the

USE

database

statement, or the ID of the

default database if no USE

database

statement has been issued for a given

instance. SQL Server Profiler displays the

name of the database if the

data column is captured in the trace and

the server is available. Determine the

value for a database by using the DB_ID

function.

3

Yes

The type of event class captured. Always

for

.

27

No

Sequence number for this event.

51

No

The type of event subclass, providing

further information about each event

21

Yes

ﾉ

Expand table