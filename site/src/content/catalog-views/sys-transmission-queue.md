---
name: "sys.transmission_queue"
title: "sys.transmission_queue"
category: "compatibility"
description: "Specifies whether poison message handling is enabled for the queue. The default is ON. A queue that has poison message handling set to OFF will not be disabled after five consecutive transaction rollbacks. This allows for a custom poison message handing system to be defined by the application. Specifies the SQL Server filegroup on which to create this queue. You can use the parameter to identify a"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.transmission_queue"
---

## Description

Specifies whether poison message handling is enabled for the queue. The default is ON. A queue that has poison message handling set to OFF will not be disabled after five consecutive transaction rollbacks. This allows for a custom poison message handing system to be defined by the application. Specifies the SQL Server filegroup on which to create this queue. You can use the parameter to identify a filegroup, or use the DEFAULT identifier to use the default filegroup for the service broker database. In the context of this clause, DEFAULT is not a keyword, and must be delimited as an identifier. When no filegroup is specified, the queue uses the default filegroup for the database. A queue can be the target of a SELECT statement. However, the contents of a queue can only be modified using statements that operate on Service Broker conversations, such as SEND, The SEND statement transmits a message from the services on one end of one or more Service

## Syntax

```sql
sys.transmission_queue
```

## Remarks

Specifies whether poison message handling is enabled for the queue. The default is ON.

A queue that has poison message handling set to OFF will not be disabled after five

consecutive transaction rollbacks. This allows for a custom poison message handing system to

be defined by the application.

Specifies the SQL Server filegroup on which to create this queue. You can use the

parameter to identify a filegroup, or use the DEFAULT identifier to use the default filegroup for

the service broker database. In the context of this clause, DEFAULT is not a keyword, and must

be delimited as an identifier. When no filegroup is specified, the queue uses the default

filegroup for the database.

A queue can be the target of a SELECT statement. However, the contents of a queue can only

be modified using statements that operate on Service Broker conversations, such as SEND,

RECEIVE, and END CONVERSATION. A queue cannot be the target of an INSERT, UPDATE,

DELETE, or TRUNCATE statement.

A queue might not be a temporary object. Therefore, queue names starting with

Creating a queue in an inactive state lets you get the infrastructure in place for a service before

allowing messages to be received on the queue.

Service Broker does not stop activation stored procedures when there are no messages on the

queue. An activation stored procedure should exit when no messages are available on the

queue for a short time.

Permissions for the activation stored procedure are checked when Service Broker starts the

stored procedure, not when the queue is created. The CREATE QUEUE statement does not

verify that the user specified in the EXECUTE AS clause has permission to execute the stored

procedure specified in the PROCEDURE NAME clause.

When a queue is unavailable, Service Broker holds messages for services that use the queue in

the transmission queue for the database. The

catalog view provides a

view of the transmission queue.

A queue is a schema-owned object. Queues appear in the

catalog view.

The following table lists the columns in a queue.

The SEND statement transmits a message from the services on one end of one or more Service

Broker conversations to the services on the other end of these conversations. The RECEIVE

statement is then used to retrieve the sent message from the queues associated with the target

The conversation handles supplied to the ON CONVERSATION clause comes from one of three

When a sent message isn't in response to a message received from another service, use

the conversation handle that returns from the BEGIN DIALOG statement that created the

conversation.

When a sent message is a response to a message previously received from another

service, use the conversation handle returned by the RECEIVE statement that returned the

original message.

The code that contains the SEND statement is sometimes separate from the code that

contains either the BEGIN DIALOG or RECEIVE statements supplying conversation handle.

In these cases, the conversation handle must be one of the data items in the state

information that is passed to the code containing the SEND statement.

Messages that are sent to services in other instances of the SQL Server Database Engine are

stored in a transmission queue in the current database until they can be transmitted to the

service queues in the remote instances. Messages sent to services in the same instance of the

Database Engine are put directly into the queues associated with these services. If a condition

prevents a local message from going directly into the target service queue, the transmission

queue can store it until the condition resolves. Examples of these occurrences include some

types of errors or the target service queue being inactive. You can use the

system view to see the messages in the transmission queue.

SEND is an atomic statement. If a SEND statement sends a message on multiple conversations

and fails, such as when a conversation is in an errored state, no messages get stored in the

transmission queue or put in any target service queue.

Service Broker optimizes the storage and transmission of messages that are sent on multiple

conversations in the same SEND statement.

Messages in the transmission queues for an instance are transmitted in sequence based on:

If the SEND statement isn't the first statement in a batch or stored procedure, the

preceding statement must be terminated with a semicolon (;).
