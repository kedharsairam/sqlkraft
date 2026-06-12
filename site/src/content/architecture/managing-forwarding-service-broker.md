---
title: "Managing Forwarding (Service Broker)"
topic: "service-broker"
description: |
  09/03/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Message forwarding allows a SQL Server instance to forward Service Broker messages between

  two or more other instances of SQL Server.
tags:
  - "service-broker"
  - "managing-forwarding-service-broker"
pubDate: 2025-12-01
---

09/03/2025

SQL Server

Azure SQL Managed Instance

Message forwarding allows a SQL Server instance to forward Service Broker messages between

two or more other instances of SQL Server. Several considerations apply to management of a

instance that performs message forwarding.

Service Broker uses the routes in the

database for both forwarded messages and

incoming messages. After you make changes to the routing configuration for forwarding, you

must back up.

stores messages to be forwarded in memory, in a data structure called the

transmitter queue. The endpoint option

sets the maximum amount of

memory (in megabytes) that SQL Server uses for storing messages to be forwarded. SQL Server

allocates memory as necessary to hold messages to be forwarded, up to this limit. If a message

arrives that would cause the size of the transmitter queue to exceed this limit, SQL Server drops

the message. However, if a large message has been fragmented, the forwarding instance

doesn't reassemble the fragments, but instead forward the message fragments to the

destination. In this manner, a forwarding instance can successfully forward a message that is

larger than the

option that is configured for the instance.

An instance that performs message forwarding often functions as a bridge between two

networks. For this configuration, the

option for the Service Broker

endpoint might need to be relatively large, since all traffic between the two networks passes

through the instance.

The dynamic management view

shows the messages that

are stored for forwarding.

ALTER ENDPOINT (Transact-SQL)

CREATE ENDPOINT (Transact-SQL)

sys.dm_broker_forwarded_messages (Transact-SQL)

Service Broker Endpoints

Service Broker Message Forwarding

```sql
msdb msdb
MESSAGE_FORWARDING_SIZE
MESSAGE_FORWARDING_SIZE
MESSAGE_FORWARDING_SIZE sys.dm_broker_forwarded_messages
```
