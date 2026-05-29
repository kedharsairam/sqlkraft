---
title: "Services"
topic: "service-broker"
description: |
  09/15/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  A Service Broker service is a name for a specific business task or set of business tasks.

  Conversations occur between services. Servic
tags:
  - "service-broker"
  - "services"
pubDate: 2025-12-01
---

09/15/2025

Applies to:

SQL Server

Azure SQL Managed Instance

A Service Broker service is a name for a specific business task or set of business tasks.

Conversations occur between services. Service Broker uses the name of the service to:

Deliver messages to the correct queue within a database.

Route messages.

Enforce the contract for a conversation.

Determine the remote security for a new conversation.

Each service specifies a queue to hold incoming messages. The contracts associated with the

service define the specific tasks that the service accepts new conversations for. Therefore, a

target service specifies one or more contracts that conversations with the service must follow.

A service that initiates conversations but doesn't receive new conversations from other services

doesn't need to specify contracts. If the service can receive messages on the

contract,

the

contract must be included in the service definition.

CREATE SERVICE (Transact-SQL)

ALTER SERVICE (Transact-SQL)

DROP SERVICE (Transact-SQL)

Service Broker routing

Understand when activation occurs

Create Service Broker services

```sql
DEFAULT
DEFAULT
```
