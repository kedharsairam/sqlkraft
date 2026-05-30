---
title: "How to: Activate Service Broker Message Forwarding (Transact-SQL)"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Message forwarding allows an instance of SQL Server to accept messages from outside the

  instance and send those messages to a differen
tags:
  - "service-broker"
  - "how-to-activate-service-broker-message-forwarding-transact-sql"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Message forwarding allows an instance of SQL Server to accept messages from outside the

instance and send those messages to a different instance. Message forwarding is configured

on a Service Broker endpoint.

1. Activate Service Broker networking if networking isn't already active. For more

information on Service Broker networking, see

How to: Activate Service Broker

networking

.

2. Alter the endpoint to activate message forwarding, and specify the maximum size, in

megabytes, for forwarded messages.

How to: Activate Service Broker networking (Transact-SQL)

How to: Deactivate Service Broker Message Forwarding (Transact-SQL)

```sql
USE master
;
GO
ALTER
ENDPOINT BrokerEndpoint
FOR
SERVICE_BROKER (
MESSAGE_FORWARDING = ENABLED,
MESSAGE_FORWARD_SIZE = 10
);
GO
```
