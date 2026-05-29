---
title: "QN:Subscription Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The QN:Subscription event reports information on notification subscriptions.
  
  Description
  
  Ap
tags:
  - "event-classes"
  - "qnsubscription-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The QN:Subscription event reports information on notification subscriptions.

Description

ApplicationName

The name of the client application that created

the connection to an instance of SQL Server.

This column is populated with the values passed

by the application rather than the displayed

name of the program.

10

Yes

ClientProcessID

The ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

process ID is provided by the client.

9

Yes

DatabaseID

The ID of the database specified by the USE

database

statement, or the ID of the default

database if no USE

database

statement has been

issued for a given instance. SQL Server Profiler

displays the name of the database if the Server

Name data column is captured in the trace and

the server is available. Determine the value for a

database by using the DB_ID function.

3

Yes

DatabaseName

The name of the database in which the user

statement is running.

35

Yes

EventClass

Type of event = 199.

27

No

EventSequence

Sequence number for this event.

51

No

EventSubClass

The type of event subclass, providing further

information about each event class. This column

may contain the following values:

: Indicates when the

query notification subscription is successfully

registered in the database.

21

Yes

ﾉ

Expand table