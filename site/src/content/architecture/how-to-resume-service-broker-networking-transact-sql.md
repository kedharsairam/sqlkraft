---
title: "How to: Resume Service Broker Networking (Transact-SQL)"
topic: "service-broker"
description: |
  09/02/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker sends and receives messages over the network while any endpoint for Service

  Broker is in the

  state. To resume Service
tags:
  - "service-broker"
  - "how-to-resume-service-broker-networking-transact-sql"
pubDate: 2025-12-01
---

09/02/2025

SQL Server

Azure SQL Managed Instance

Service Broker sends and receives messages over the network while any endpoint for Service

Broker is in the

state. To resume Service Broker networking, alter the endpoints to set

the state to.

Alter an endpoint to set the state to.

How to: Activate Service Broker networking (Transact-SQL)

How to: Deactivate Service Broker networking (Transact-SQL)

How to: Pause Service Broker networking (Transact-SQL)

ALTER DATABASE (Transact-SQL)

ALTER ENDPOINT (Transact-SQL)

７

Note

Activating Service Broker networking allows Service Broker to send and receive messages

over the network. The authentication level set on the endpoint controls which network

connections the endpoint accepts. For more information on Service Broker networking

and security, see.

```sql
STARTED
STARTED
STARTED
USE master
;
GO
ALTER
ENDPOINT BrokerEndpoint
STATE = STARTED;
GO
```
