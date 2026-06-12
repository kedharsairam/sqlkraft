---
title: "Broker:Activation Event Class"
topic: "event-classes"
description: "generates a event when a queue monitor starts an activation stored procedure, sends a QUEUE_ACTIVATION notific"
tags: ["event-classes","brokeractivation-event-class"]
pubDate: 2025-12-01
---

generates a

event when a queue monitor starts an activation

stored procedure, sends a QUEUE_ACTIVATION notification, or when an activation stored

procedure started by a queue monitor exits.

Description

The ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

process ID is provided by the client.

9

Yes

The ID of the database specified by the USE

database

statement, or the ID of the default

database if no USE

database

statement has been

issued for a given instance. SQL Server Profiler

displays the name of the database if the

data column is captured in the trace

and the server is available. Determine the value

for a database by using the DB_ID function.

3

Yes

The type of event class captured. Always

for.

27

No

Sequence number for this event.

51

No

The specific action that this event reports. One of

the following values:

: SQL Server started an activation stored

procedure.

: The activation stored procedure exited

normally.

: The activation stored procedure exited

with an error.

21

No

ﾉ

Expand table
