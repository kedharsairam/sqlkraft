---
title: "Service Broker Dynamic Routing"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  For most scenarios, Service Broker applications use routes configured by an administrator. In

  some cases, you might need to dynamicall
tags:
  - "service-broker"
  - "service-broker-dynamic-routing"
pubDate: 2025-12-01
---

09/11/2025

SQL Server

Azure SQL Managed Instance

For most scenarios, Service Broker applications use routes configured by an administrator. In

some cases, you might need to dynamically configure routes. In this case, you implement a

Broker Configuration Notice service.

doesn't provide a built-in solution for dynamically creating routing tables. Instead,

provides functionality that allows developers to create applications that provide

dynamic routing.

When Service Broker can't find a route for a conversation, Service Broker checks the routing

table for a service named

SQL/ServiceBroker/BrokerConfiguration. If an entry exists for that

service, Service Broker creates a new conversation to that service and sends a message on that

conversation requesting that a route be created. When the conversation to the

service ends, Service Broker again attempts to route the message. If no

route exists at that point, Service Broker marks all messages for the conversation as.

After a timeout period, Service Broker again requests a route from the

service.

To create a service for dynamic routing, create a service named

SQL/ServiceBroker/BrokerConfiguration

that accepts conversations on the contract. Then, create a

route to the service in the routing table for database that will use dynamic routing.

Requests for routes use the message type.

The message is in XML format, and contains the name of the service for which routing

information should be available.

For example, the following message is a request for a route to the service

:

XML

```sql
DELAYED https://schemas.microsoft.com/SQL/ServiceBroker/BrokerConfigurationNotice https://schemas.microsoft.com/SQL/ServiceBroker/BrokerConfigurationNotice/MissingRoute https://Adventure-
Works.com/Elsewhere
```
