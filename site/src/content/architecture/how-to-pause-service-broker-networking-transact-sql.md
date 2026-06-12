---
title: "How to: Pause Service Broker Networking (Transact-SQL)"
topic: "service-broker"
description: "09/02/2025 Service Broker sends and receives messages over the network while any endpoint for Service Broker is in the state. To pause Service B"
tags: ["service-broker","how-to-pause-service-broker-networking-transact-sql"]
pubDate: "2025-12-01"
---

Service Broker sends and receives messages over the network while any endpoint for Service

Broker is in the

state. To pause Service Broker networking, alter all Service Broker

endpoints to set the state to. This state prevents Service Broker from transmitting

messages out of the instance or receiving messages from outside of the instance, but doesn't

affect message delivery within the instance. To prevent message delivery to a specific database,

use

to deactivate Service Broker in that database.

Alter all Service Broker endpoints to set the state to.

How to: Deactivate Service Broker networking (Transact-SQL)

How to: Resume Service Broker networking (Transact-SQL)

ALTER DATABASE (Transact-SQL)

ALTER ENDPOINT (Transact-SQL)

CREATE ENDPOINT (Transact-SQL)

```sql
STARTED
STOPPED
ALTER DATABASE
STOPPED
USE master
;
GO
ALTER
ENDPOINT BrokerEndpoint
STATE = STOPPED;
GO
```
