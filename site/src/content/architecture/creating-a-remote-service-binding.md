---
title: "Creating a Remote Service Binding"
topic: "service-broker"
description: |
  09/16/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  To exchange messages with Service Broker, you must create the appropriate user security

  context. The most flexible way to do this is w
tags:
  - "service-broker"
  - "creating-a-remote-service-binding"
pubDate: 2025-12-01
---

09/16/2025

Applies to:

SQL Server

Azure SQL Managed Instance

To exchange messages with Service Broker, you must create the appropriate user security

context. The most flexible way to do this is with a remote service binding. A remote service

binding establishes a relationship between a local database user, the certificate for the user,

and the name of a remote service. Service Broker uses the remote service binding to provide

dialog security for conversations that target the remote service. This binding defines the

security credentials to use to initiate a conversation with a remote service.

When a conversation is initiated, Service Broker checks to see whether a remote service

binding is available for the target service. If a remote service binding isn't available, Service

Broker checks the routing table for the Broker Configuration Notice (BCN) service; the service

name is

. If a BCN route exists, Service Broker creates a

new conversation with the BCN and sends a message on that conversation that requests

creation of a remote service binding. The application defined for the BCN queue must then

respond to the request.

Requests for remote service bindings use the message type

. The message is in XML format and contains the name of the service for which

remote service binding information should be available.

For example, the following message is a request for a remote service binding to the service

:

XML

７

Note

The behavior is comparable to

.

```sql
SQL/ServiceBroker/BrokerConfiguration
https://schemas.microsoft.com/SQL/ServiceBroker/BrokerConfigurationNotice/MissingRemoteSe
rviceBinding
https://Adventure-Works.com/Elsewhere
<MissingRemoteServiceBinding
xmlns
=
"https://schemas.microsoft.com/SQL/ServiceBroker/BrokerConfigurationNotice/M
issingRemoteServiceBinding"
>
<SERVICE_NAME>
https://Adventure-Works.com/Elsewhere
</SERVICE_NAME>
</MissingRemoteServiceBinding>
```
