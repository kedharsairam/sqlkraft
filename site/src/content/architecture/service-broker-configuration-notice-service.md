---
title: "Service Broker Configuration Notice Service"
topic: "service-broker"
description: |
  09/12/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  You can create a Broker Configuration Notice (BCN) service on an initiating server which
  
  automatically binds conversations to a specif
tags:
  - "service-broker"
  - "service-broker-configuration-notice-service"
pubDate: 2025-12-01
---

09/12/2025

Applies to:

SQL Server

Azure SQL Managed Instance

You can create a Broker Configuration Notice (BCN) service on an initiating server which

automatically binds conversations to a specific user on a target server.

When a BCN service is created, the initiating service sends a

message to the BCN service to ask if a user context is available for the conversation on the

target server. When the BCN service responds that a user context is available, the user context

is bound to the conversation, and all messages are added to the queue under the context of

the user. If

, the dialog won't proceed until the BCN service confirms that a

user context is available. If

, the dialog proceeds after the BCN ends the

conversation.

The BCN service also manages dynamic routing. For more information about creating a Broker

Configuration Notice Service, see

Service Broker dynamic routing

.

Service Broker dynamic routing

７

Note

If a BCN service is created, the initiating service requests the user context regardless of the

encryption status.

```sql
ENCRYPTION = ON
ENCRYPTION = OFF
```