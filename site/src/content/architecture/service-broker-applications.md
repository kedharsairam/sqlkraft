---
title: "Service Broker Applications"
topic: "service-broker"
description: "09/10/2025 Service Broker applications are made up of one or more programs and the database objects that those programs use. Applications communi"
tags: ["service-broker","service-broker-applications"]
pubDate: 2025-12-01
---

Service Broker applications are made up of one or more programs and the database objects

that those programs use. Applications communicate by creating conversations between

independent components called services and then exchanging messages within those

conversations. Applications use Service Broker by executing Transact-SQL statements in a SQL

Server database.

A Service Broker application is made up of:

One or more programs that implement a task or related set of tasks. Outside SQL Server,

applications can be written in any programming environment that can run Transact-SQL

statements in SQL Server. Inside SQL Server, applications can be written as stored

procedures using Transact-SQL or a common language runtime (CLR) compliant

language.

A service that exposes the tasks to other services. A service is a Service Broker object that

provides an addressable name for a set of related tasks. Other services start conversations

with this service to perform the tasks.

A contract and message types that define the structure and direction of the messages

that are used in communications between the services.

A queue to hold messages for the service.

Optionally, routes and remote service bindings. Routes associate a network address with

the name of a remote service. Remote service bindings associate a service name with a

local database principal. Service Broker uses the certificate associated with the specified

principal to handle authorization for the remote service and encryption of the messages

exchanged with the remote service. Service Broker permits the routes and remote service

bindings to be configured while the application is in deployment without requiring

changes to the application. This allows administrators to move services and change

security credentials without changes to application code. For more information on

configuring routes and remote service bindings, see

Administration (Service Broker).
