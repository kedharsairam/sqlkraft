---
title: "How to: Activate Service Broker Networking (Transact-SQL)"
topic: "service-broker"
description: |
  08/29/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Service Broker doesn't send or receive messages over the network by default. To activate
  
  Service Broker networking in an instance, cre
tags:
  - "service-broker"
  - "how-to-activate-service-broker-networking-transact-sql"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker doesn't send or receive messages over the network by default. To activate

Service Broker networking in an instance, create an endpoint for Service Broker.

Creating a Service Broker endpoint causes SQL Server to accept TCP/IP connections on the port

specified. Service Broker transport security allows you to require authorization for connections

to the port. If the computer that runs SQL Server has a firewall enabled, the firewall

configuration on that computer must allow both incoming connections for the port specified in

the endpoint. For more information on Service Broker transport security, see

Service Broker

Transport Security

.

Create a Service Broker endpoint, specifying the port number and the authentication level.

SQL

How to: Pause Service Broker networking (Transact-SQL)

How to: Resume Service Broker networking (Transact-SQL)

```sql
USE
master
;
GO
CREATE
ENDPOINT BrokerEndpoint
STATE = STARTED
AS
TCP (
LISTENER_PORT = 4037
)
FOR
SERVICE_BROKER (
AUTHENTICATION
= WINDOWS
);
GO
```