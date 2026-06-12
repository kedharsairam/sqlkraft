---
title: "Service Broker Message Forwarding"
topic: "service-broker"
description: "09/11/2025 Service Broker message forwarding allows an instance of SQL Server to accept messages from outside the instance and send those message"
tags: ["service-broker","service-broker-message-forwarding"]
pubDate: 2025-12-01
---

Service Broker message forwarding allows an instance of SQL Server to accept messages from

outside the instance and send those messages to a different instance.

An administrator can use message forwarding to:

Provide connectivity between servers in different trust domains.

Simplify administration by creating a single centralized instance that holds the routing

information for a domain.

Distribute work among several instances.

When forwarding is enabled, the routing table in

determines whether a

message that arrives from another instance is forwarded. If the address for the matching route

isn't

, SQL Server forwards the message to the address specified. Otherwise, the message

is delivered locally.

Each Service Broker message contains a maximum lifetime and a count of the number of times

that the message has been forwarded. When an instance forwards the message, that instance

increases the count in the message. If the message exceeds the maximum lifetime, the

forwarding instance discards the message. This strategy helps avoid problems in situations

where a routing loop might exist.

An instance that forwards a message doesn't acknowledge the message to the sender. Only the

final destination acknowledges the message. If the sender doesn't receive an acknowledgment

from the destination after a period of time, the sender retries the message.

An instance that performs message forwarding doesn't need to store forwarded messages.

Instead, SQL Server holds messages to be forwarded in memory. The amount of memory

available for message forwarding is specified as part of the Service Broker endpoint

configuration. This strategy allows efficient, stateless message forwarding. In the event that an

instance that performs message forwarding fails, no messages are lost. Each message is always

maintained at the sender until the final destination acknowledges the message, as described in

Service Broker communication protocols.

```sql
msdb.sys.routes
LOCAL
```
