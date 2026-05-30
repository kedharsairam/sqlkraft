---
title: "Creating Service Broker Objects"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  An application uses Service Broker by executing Transact-SQL statements that operate on

  Service Broker objects defined in a database.
tags:
  - "service-broker"
  - "creating-service-broker-objects"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

An application uses Service Broker by executing Transact-SQL statements that operate on

Service Broker objects defined in a database. This section describes general considerations

when you create the Service Broker objects for an application.

Service Broker objects define the metadata and storage for a specific set of tasks:

Message types define the data that is exchanged in a conversation.

Contracts define tasks. Each contract specifies the message types that can be used in a

particular conversation, and which side of the conversation can send the message.

A queue stores incoming messages for a service.

A service represents a related set of business tasks. The name of the service is also used

to locate the queue for the service.

A contract depends on one or more message types. A service depends on a queue, and can

depend on one or more contracts. Therefore, contracts are created after message types and

dropped before message types. Services are created after queues and contracts, and dropped

before queues and contracts.

For more information on these objects, see

Conversation architecture

.

The procedure for creating a service follows the same basic outline regardless of whether your

service is an initiating service, a target service, or both.

The definition of a service specifies the contracts for which the service can be a target. In

contrast, an application can use a service to initiate a conversation that uses any contract

defined in the database. Service Broker takes this approach to enforce the general rule that a

service should only receive messages that the application can process. To ensure that the

application doesn't receive messages of an arbitrary or unknown type, Service Broker accepts a

new dialog only if the dialog follows a contract specified in the service. An initiating service
