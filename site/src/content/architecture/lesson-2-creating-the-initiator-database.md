---
title: "Lesson 2: Creating the Initiator Database"
topic: "service-broker"
description: |
  09/04/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  In this lesson, you learn to create the initiator database and all the initiator Service Broker

  objects that are used in this tutorial
tags:
  - "service-broker"
  - "lesson-2-creating-the-initiator-database"
pubDate: 2025-12-01
---

09/04/2025

SQL Server

Azure SQL Managed Instance

In this lesson, you learn to create the initiator database and all the initiator Service Broker

objects that are used in this tutorial. Run these steps from a copy of Management Studio that is

running on the same computer as the initiator instance the Database Engine.

Copy and paste the following code into a Query Editor window, then run it to create a

Service Broker endpoint for this instance of the Database Engine. A Service Broker

endpoint specifies the network address to which Service Broker messages are sent. This

endpoint uses the Service Broker default of TCP port 4022, and specifies that remote

instances of the Database Engine will use Windows Authentication connections to send

messages.

Windows Authentication works when both computers are in the same domain or are in

trusted domains. If the computers aren't in trusted domains, use certificate security for

the endpoints. For more information, see

How to: Create certificates for Service Broker

transport security.

```sql
USE master
;
GO
IF EXISTS (
SELECT
*
FROM sys.endpoints
WHERE name
= N
'InstInitiatorEndpoint'
)
DROP
ENDPOINT InstInitiatorEndpoint;
GO
CREATE
ENDPOINT InstInitiatorEndpoint
STATE = STARTED
AS
TCP (
LISTENER_PORT = 4022
)
FOR
SERVICE_BROKER (
AUTHENTICATION
= WINDOWS
```
