---
title: "Error Handling for Service Broker"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Error handling in an application that uses Service Broker has two distinct aspects. First, the

  application must handle errors raised b
tags:
  - "service-broker"
  - "error-handling-for-service-broker"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Error handling in an application that uses Service Broker has two distinct aspects. First, the

application must handle errors raised by the Database Engine through the normal Transact-SQL

error mechanism. Second, an application that uses Service Broker must handle asynchronous

errors that arrive as messages on the queue for the service. In either case, an application must

not permanently remove a message from a queue without acting on the message, and the

application must always hold a conversation group lock before updating state that is related to

the conversation group.

Description

Handle Transact-SQL errors

(Service Broker)

Describes strategies for working with Transact-SQL errors while

maintaining transactional messaging.

Handle Service Broker error

messages

Describes strategies for handling error messages delivered by Service

Broker.

Handle poison messages

Describes strategies for recovering from poison messages.

Understanding Database Engine Errors

ﾉ

Expand table
