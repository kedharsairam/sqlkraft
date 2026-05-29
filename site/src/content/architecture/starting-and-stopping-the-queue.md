---
title: "Starting and Stopping the Queue"
topic: "service-broker"
description: |
  09/08/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Use the
  
  statement to start and stop a queue. When a queue is started, the queue
  
  is available to send and receive messages. When a que
tags:
  - "service-broker"
  - "starting-and-stopping-the-queue"
pubDate: 2025-12-01
---

09/08/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Use the

statement to start and stop a queue. When a queue is started, the queue

is available to send and receive messages. When a queue is stopped, Service Broker doesn't

deliver new messages to the queue, and doesn't allow applications to receive messages from

the queue.

Administrators often create queues in an unavailable state. This state prevents Service Broker

from placing messages on the queue until all of the objects for a service are created. When the

service is ready to receive messages, the administrator makes the queue available with the

following statement:

SQL

The following statement makes the queue unavailable for receive:

SQL

When a queue is unavailable for receive, an application can't process the messages in the

queue. Because Service Broker guarantees that a message only leaves the queue as part of a

receive operation, there's no way to remove messages from a stopped queue. Service Broker is

designed to allow maintenance while the queue continues to receive messages, so it's rarely

necessary to stop a queue once the queue is made available. Because most activation stored

procedures exit when a

operation fails or when no more messages are available, one

reason for stopping the queue is to replace an activation stored procedure for a service that

receives messages constantly.

When a message arrives for a queue that is unavailable, Service Broker holds the message in

the transmission queue for the database, rather than delivering the message to the queue.

ALTER QUEUE (Transact-SQL)

```sql
ALTER QUEUE
RECEIVE
ALTER
QUEUE dbo.ExpenseQueue
WITH
STATUS
=
ON
;
ALTER
QUEUE dbo.ExpenseQueue
WITH
STATUS
=
OFF
;
```