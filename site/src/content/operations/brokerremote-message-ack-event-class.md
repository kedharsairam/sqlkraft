---
title: "Broker:Remote Message Ack Event Class"
topic: "event-classes"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  SQL Server generates a
  
  event when Service Broker sends or
  
  receives a message acknowledgement.
  
  Description
  
  The name of t
tags:
  - "event-classes"
  - "brokerremote-message-ack-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server generates a

event when Service Broker sends or

receives a message acknowledgement.

Description

The name of the client application that

created the connection to an instance

of SQL Server. This column is

populated with the values that are

passed by the application, instead of

the displayed name of the program.

10

Yes

The sequence number of the message

that contains the acknowledgement.

52

No

The sequence number of the message

that is being acknowledged.

53

No

The ID assigned by the host computer

to the process where the client

application is running. This data

column is populated if the client

process ID is provided by the client.

9

Yes

The ID of the database that is specified

by the USE

database

statement. If no

USE

database

statement has been

issued for a given instance, the ID of

the default database. SQL Server

Profiler displays the name of the

database if the

data

column is captured in the trace and the

server is available. Determine the value

for a database by using the DB_ID

function.

3

Yes

ﾉ

Expand table