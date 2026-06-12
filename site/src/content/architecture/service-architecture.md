---
title: "Service Architecture"
topic: "service-broker"
description: |
  09/12/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This section describes the database objects that specify the basic design of an application that

  uses Service Broker.

  At design time,
tags:
  - "service-broker"
  - "service-architecture"
pubDate: 2025-12-01
---

09/12/2025

SQL Server

Azure SQL Managed Instance

This section describes the database objects that specify the basic design of an application that

uses Service Broker.

At design time, Service Broker applications specify the following objects:

: Define the names of the messages exchanged between applications.

Optionally provide validation for the messages.

: Specify the direction and type of messages in a given conversation.

: Store messages. This storage mechanism allows for asynchronous

communication between services. Service Broker queues provide additional benefits, such

as automatically locking messages in the same conversation group.

: Are addressable endpoints for conversations. Service Broker messages are sent

from one service to another service. A service specifies a queue to hold messages, and

specifies the contracts for which the service can be the target. A contract provides a

service with a well-defined set of message types.

A Service Broker application uses the SQL Server objects in the preceding list to conduct a

conversation. Any program that can run Transact-SQL statements in SQL Server can use Service

Broker. Applications can be stored procedures written in Transact-SQL or a CLR-compliant

language, or they can be external programs that connect to an instance of SQL Server.

The following diagram shows a Service Broker service:
