---
title: "Routes"
topic: "service-broker"
description: |
  09/04/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker uses routes to determine where to deliver messages. When a service sends a

  message on a conversation, SQL Server uses r
tags:
  - "service-broker"
  - "routes"
pubDate: 2025-12-01
---

09/04/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker uses routes to determine where to deliver messages. When a service sends a

message on a conversation, SQL Server uses routes to locate the service that will receive the

message. When that service responds, SQL Server again uses routes to locate the initiating

service. By default, each database contains a route that specifies that messages for any service

which doesn't have an explicit route are delivered within the SQL Server instance.

There are three basic components of a route:

Service name

The name of the service that this route specifies addressing for. This name must be an

exact match for the Service Name in the

command.

Broker instance identifier

A unique identifier for a specific database to send the messages to. This is the

column in the

table row for the database that this

route points to.

Network address

An actual machine address, a keyword that restricts the route to the local machine, or a

keyword that indicates that the transport layer deduces the address from the service

name. A network address can be the address of the broker that hosts the service, or it can

be the address of a forwarding broker.

To determine the route for a conversation, SQL Server matches the service name and the

broker instance identifier that were specified in the

statement

against the service name and broker instance identifier that are specified in the route. Routes

that don't provide a service name match any service name. Routes that don't provide a broker

instance identifier match any broker instance identifier. When more than one route matches a

conversation, SQL Server selects a route, as described in

Service Broker Routing

.

SQL Server guarantees that once the target acknowledges the first message, all subsequent

messages on that conversation route to the same database. However, other conversations on

the same conversation group aren't guaranteed to route to the same database. If an

application requires that messages on related conversations route to the same database, the

```sql
BEGIN DIALOG service_broker_guid sys.databases
BEGIN DIALOG CONVERSATION
```
