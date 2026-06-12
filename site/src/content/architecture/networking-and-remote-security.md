---
title: "Networking and Remote Security"
topic: "service-broker"
description: "09/11/2025 To help enable secure, reliable communication between different instances of SQL Server, Service Broker includes features to let you m"
tags: ["service-broker","networking-and-remote-security"]
pubDate: "2025-12-01"
---

To help enable secure, reliable communication between different instances of SQL Server,

Service Broker includes features to let you manage routing and establish security for the

conversation.

Description

Remote

service

bindings

Describes setting the certificate that the broker uses for dialog security. Dialog security

provides end-to-end encryption and remote authorization for conversations to specific

services.

Routes

Describes specifying the location of the service and the database that contains the

service. A route is required for Service Broker to deliver messages. By default, each

database contains a route that specifies that services with no other route defined are

delivered within the current instance.

Service

Broker

endpoints

Describes configuring SQL Server to send and receive messages over TCP/IP connections.

Endpoints can provide transport security, which prevents unauthorized connections to

the endpoint.

Remote service bindings

Routes

Service Broker endpoints

Service Broker dialog security

Service Broker transport security

ﾉ

Expand table
