---
title: "Event-Based Activation"
topic: "service-broker"
description: "08/29/2025 SQL Server provides a queue activation event to notify external applications when a queue has messages to process. This topic describe"
tags: ["service-broker","event-based-activation"]
pubDate: 2025-12-01
---

provides a queue activation event to notify external applications when a queue has

messages to process. This topic describes the event and strategies for receiving and

responding to the event.

includes a QUEUE_ACTIVATION event. This event reports that there's useful work for

another queue reader. The activation event contains the name of the queue and the name of

the database and schema that contain the queue. An external program can use this

information to start the correct program to read from the queue.

can't track the capacity or the number of external processes that are reading from

the queue. Therefore, SQL Server produces queue activation events periodically for as long as

activation is required.

An external application that uses event-based activation typically creates an event notification

on the queue that receives messages for the service. The external application creates a service

and queue for receiving the activation messages, then monitors that queue for messages that

report QUEUE_ACTIVATION events.

This strategy allows the external application to use the activation logic that's built in to Service

Broker to determine when there's more work for a queue reader. Further, it's possible for one

external application to monitor activation for a number of queues and start the appropriate

program when activation is required.

CREATE EVENT NOTIFICATION (Transact-SQL)

Event notifications
