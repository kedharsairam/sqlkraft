---
title: "QN:Template Event Class"
topic: "event-classes"
description: "The QN:Template event reports information on the internal use of query templates."
tags: ["event-classes","qntemplate-event-class"]
pubDate: "2025-12-01"
---

The QN:Template event reports information on the internal use of query templates. Query

templates are the mechanism that the Database Engine uses to share definitions of a query for

notification. These templates are created along with parameter tables. The Database Engine

creates an event of this type when a query template is created, used, or destroyed.

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

Type of event = 201.

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

21

Yes

ﾉ

Expand table
