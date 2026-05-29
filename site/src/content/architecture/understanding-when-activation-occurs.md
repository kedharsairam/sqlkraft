---
title: "Understanding When Activation Occurs"
topic: "service-broker"
description: |
  09/10/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  The Service Broker activation process consists of two steps. First, Service Broker determines
  
  whether activation is necessary. Second,
tags:
  - "service-broker"
  - "understanding-when-activation-occurs"
pubDate: 2025-12-01
---

09/10/2025

Applies to:

SQL Server

Azure SQL Managed Instance

The Service Broker activation process consists of two steps. First, Service Broker determines

whether activation is necessary. Second, Service Broker determines whether activation occurs.

Although the exact process is different for internal activation and external activation, the

overall concepts involved are the same for either strategy.

Activation is necessary whenever a new queue reader would have useful work to perform.

Queue monitors determine whether activation is necessary. Service Broker creates a queue

monitor for each queue with activation

or for which a

event

notification has been registered. The dynamic management view

sys.dm_broker_queue_monitors

lists the queue monitors active in the instance.

Each queue monitor tracks the following criteria:

Whether the queue contains messages that are ready for receive

How recently a

statement on the queue returned an empty result set

How many activation stored procedures are currently running for the queue

A queue monitor checks whether activation is necessary every few seconds and when one or

more of the following events occurs:

A new message arrives on the queue

SQL Server executes a

statement for the queue

A transaction that contains a

statement rolls back

All stored procedures started by the queue monitor exit

SQL Server executes an

statement for the queue

Activation is necessary if either of the following conditions is true:

A new message arrives on a queue that contains no unread messages and there are no

activation stored procedures running for the queue.

The queue contains unread messages, there's no session waiting in a

statement or a

statement without a

clause, and no

statement or

statement without a

clause has returned

```sql
STATUS = ON
QUEUE_ACTIVATION
RECEIVE
RECEIVE
RECEIVE
ALTER
GET CONVERSATION
GROUP
RECEIVE
WHERE
GET
CONVERSATION GROUP
RECEIVE
WHERE
```