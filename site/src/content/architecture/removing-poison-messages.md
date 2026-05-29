---
title: "Removing Poison Messages"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  A poison message is a message containing information that an application can't successfully
  
  process. For example, a manufacturing work
tags:
  - "service-broker"
  - "removing-poison-messages"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

A poison message is a message containing information that an application can't successfully

process. For example, a manufacturing workstation might submit a request to withdraw a part

from inventory just before a change order makes the part obsolete. The change order becomes

effective while the request for inventory is in transit. The inventory management application

receives the request from the workstation, but can't successfully process the request, and the

database operation to update the number of parts in stock fails. The transaction containing the

receive operation then rolls back, returning the message to the queue. In this situation, the

application continues to receive the same message, the update continues to fail, and the

message returns to the queue.

A poison message isn't a corrupt message, and might not be an invalid request. Service Broker

contains message integrity checks that detect corrupt messages. An application also typically

validates the content of a message, and discards a message that contains an illegal request. In

contrast, many poison messages were valid when the message was created, but later became

impossible to process.

Service Broker provides automatic poison message detection. When a transaction that contains

a

statement rolls back five times, Service Broker disables all queues from which the

transaction received messages by automatically setting the queue status to

. In addition,

Service Broker generates an event of type

.

An administrator might use SQL Server Agent alerts to be notified when a queue is disabled. A

developer can also create an application that detects when a queue is disabled by Service

Broker. That application often inspects the messages in the queue to find the poison message.

Once the application determines which message can't be processed, the application sets the

queue status to

and ends the conversation for the message with an error. An application

that detects poison messages must be careful to clean up any state associated with the

conversation when ending the conversation. For more information on creating an application

to recover from poison messages, see

Handle poison messages

.

```sql
RECEIVE
OFF
ON
```