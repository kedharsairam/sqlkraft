---
title: "How to: Deactivate Service Broker Networking (Transact-SQL)"
topic: "service-broker"
description: |
  09/02/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker sends and receives messages over the network while any Service Broker

  endpoint is in the

  state. To deactivate Service
tags:
  - "service-broker"
  - "how-to-deactivate-service-broker-networking-transact-sql"
pubDate: 2025-12-01
---

09/02/2025

SQL Server

Azure SQL Managed Instance

Service Broker sends and receives messages over the network while any Service Broker

endpoint is in the

state. To deactivate Service Broker networking, drop all Service

Broker endpoints.

Drop all Service Broker endpoints.

How to: Activate Service Broker networking (Transact-SQL)

How to: Pause Service Broker networking (Transact-SQL)

ALTER DATABASE (Transact-SQL)

ALTER ENDPOINT (Transact-SQL)

CREATE ENDPOINT (Transact-SQL)

```sql
STARTED
USE master
;
GO
DROP
ENDPOINT BrokerEndpoint;
GO
```
