---
title: "Creating Service Broker Message Types"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  A message type defines the name of a specific kind of message and the validation that Service

  Broker performs on that kind of message.
tags:
  - "service-broker"
  - "creating-service-broker-message-types"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

A message type defines the name of a specific kind of message and the validation that Service

Broker performs on that kind of message. To determine the message types that your

application will use, you first plan out the tasks that your application must perform, and the

data that is necessary to perform each task.

The most common approach for an application is to structure the messages so that each

message includes the information required for one step of the task. When each message

contains the information for one step of the task, the application can easily receive the

message, complete the step, and send a response within a single transaction. Therefore, for

many applications, the easiest way to determine the message types and the content for the

message is to determine the transaction boundaries for the tasks performed by the application.

Each distinct step is a transaction, and each transaction corresponds to a message type

exchanged between the services. Status information, results, or output are also message types.

The Service Broker communications protocols are designed to work with this messaging style.

The Dialog Protocol fragments large messages for transit and guarantees that large messages

don't prevent small messages from being transmitted.

The validation specified for the message depends on the content of the message. A common

practice is to use the most restrictive validation available during testing, and then to choose

less-restrictive validation to improve performance when the application is deployed. For

example, it's possible to exchange a typed XML document as the body of a message that

specifies a validation of

. In this case, your application validates the message when

processing the XML.

The network format for a message includes the name of the message type. Therefore, message

type names are often chosen to avoid collation issues and naming conflicts. For more

information on naming, see

Naming Service Broker Objects

.

An application typically doesn't define new message types to indicate success or failure.

Instead, use the

statement to indicate that the conversation is complete and

```sql
NONE
END CONVERSATION
```
