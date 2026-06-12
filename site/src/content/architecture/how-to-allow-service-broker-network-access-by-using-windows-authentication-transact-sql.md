---
title: "How to: Allow Service Broker Network Access by Using Windows Authentication (Transact-SQL)"
topic: "service-broker"
description: ""
tags: ["service-broker","how-to-allow-service-broker-network-access-by-using-windows-authentication-transact-sql"]
pubDate: "2025-12-01"
---

To allow another instance to send messages using Windows Authentication for transport

security, you create a user in the

database for the startup service account for the other

instance.

1. Create a login for the startup service account for the other instance.

2. Grant that user

permission to the Service Broker endpoint.

Once access is configured in each instance, then communications between the two instances

use Service Broker transport security when the transport security configuration option is set in

both databases.

７

Note

If both instances run as the same domain account, then the instances can always

communicate using Windows Authentication for transport security. If the instances run as

the

account, the login name is MachineName$, and Kerberos must be

available on the network to use the machine account.

```sql
master
CONNECT
LocalSystem
USE master
;
GO
CREATE
LOGIN [
DOMAIN
\
user
]
FROM
WINDOWS;
GO
```
