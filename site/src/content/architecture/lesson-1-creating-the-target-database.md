---
title: "Lesson 1: Creating the Target Database"
topic: "service-broker"
description: ""
tags: ["service-broker","lesson-1-creating-the-target-database"]
pubDate: 2025-12-01
---

In this lesson, you learn to create the target database and all the Service Broker target objects

that don't have dependencies on the initiator database. Run these steps from a copy of

Management Studio that's running on the same computer as the target instance the Database

Engine.

Copy and paste the following code into a Query Editor window, then run it to create a

Service Broker endpoint for this instance of the Database Engine. A Service Broker

endpoint establishes the network address to which Service Broker messages are sent. This

endpoint uses the Service Broker default of TCP port 4022, and establishes that the

remote instances of the Database Engine will use Windows Authentication connections to

send messages.

Windows Authentication works when both computers are in the same domain or trusted

domains. If the computers aren't in trusted domains, use certificate security for the

endpoints. For more information, see

How to: Create certificates for Service Broker

transport security.

```sql
USE master
;
GO
IF EXISTS (
SELECT
*
FROM master.sys.endpoints
WHERE name
= N
'InstTargetEndpoint'
)
DROP
ENDPOINT InstTargetEndpoint;
GO
CREATE
ENDPOINT InstTargetEndpoint
STATE = STARTED
AS
TCP (LISTENER_PORT = 4022)
FOR
SERVICE_BROKER (
AUTHENTICATION
= WINDOWS);
GO
```
