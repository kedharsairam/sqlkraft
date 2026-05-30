---
title: "How to: Deactivate Service Broker Message Forwarding (Transact-SQL)"
topic: "service-broker"
description: |
  09/02/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Message forwarding allows an instance of SQL Server to accept messages from outside the

  instance and send those messages to a differen
tags:
  - "service-broker"
  - "how-to-deactivate-service-broker-message-forwarding-transact-sql"
pubDate: 2025-12-01
---

09/02/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Message forwarding allows an instance of SQL Server to accept messages from outside the

instance and send those messages to a different instance. Message forwarding is configured

on a Service Broker endpoint.

Alter the endpoint to deactivate message forwarding.

How to: Activate Service Broker networking (Transact-SQL)

How to: Activate Service Broker message forwarding (Transact-SQL)

```sql
USE master
;
GO
ALTER
ENDPOINT BrokerEndpoint
FOR
SERVICE_BROKER (MESSAGE_FORWARDING = DISABLED);
GO
```
