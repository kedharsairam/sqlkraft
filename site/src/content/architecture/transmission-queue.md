---
title: "Transmission Queue"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker uses a transmission queue as a holding area for messages. Each database

  contains a separate transmission queue. The tra
tags:
  - "service-broker"
  - "transmission-queue"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker uses a transmission queue as a holding area for messages. Each database

contains a separate transmission queue. The transmission queue is stored in the primary

filegroup for the database.

Outgoing messages are added to the transmission queue in the database that sends the

message. The message remains in the transmission queue until the destination has

acknowledged receipt of the message.

Incoming messages are generally directly added to the queue for the destination service.

However, if the destination queue is

, incoming messages are held in the transmission

queue for the database that contains the destination queue.

In cases where both sides of the conversation are in the same instance, Service Broker might

optimize message delivery by placing the message directly on the destination queue.

If Service Broker message delivery isn't active in the database that sends the message, or the

destination database is unavailable, messages remain in the transmission queue for the

database that sent the message.

If the destination database is available, but the destination queue is unavailable, the message is

held in the transmission queue for the database that contains the destination service.

sys.transmission_queue (Transact-SQL)

Conversation architecture

Service Broker communication protocols

```sql
OFF
```
