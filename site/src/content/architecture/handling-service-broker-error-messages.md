---
title: "Handling Service Broker Error Messages"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker applications must handle two types of error messages received from

  conversations: error messages created by an applicat
tags:
  - "service-broker"
  - "handling-service-broker-error-messages"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker applications must handle two types of error messages received from

conversations: error messages created by an application that uses Service Broker and system

messages created by Service Broker.

Service Broker applications are typically systems that consist of code running asynchronously

on different computers. The parts of the application communicate with each other by using

messages sent on Service Broker conversations. The part of the application on one side of a

Service Broker conversation can report application errors to the other side by sending error

messages. The receiving part of the application must have code to detect an error message

and correctly handle the error condition.

Service Broker applications can communicate errors by using either system-defined or

application-defined message types.

Use the

clause of the

statement to report application errors that

are severe enough to require ending the conversation. For example:

The

statement:

Generates a Service Broker system error message and sends it to the remote side of the

conversation. The error messages use the system-defined

message type.

Ends the local side of the conversation.

The part of the application that receives the

message should do any needed cleanup

and end its side of the conversation.

```sql
WITH ERROR
END CONVERSATION
END CONVERSATION WITH ERROR https://schemas.microsoft.com/SQL/ServiceBroker/Error
Error
END
CONVERSATION @ConversationHandle
WITH
ERROR
= 1234 DESCRIPTION =
'The account specified in the invoice does not exist, verify the account number.'
;
```
