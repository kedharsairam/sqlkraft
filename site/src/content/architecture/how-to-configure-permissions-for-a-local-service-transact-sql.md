---
title: "How to: Configure Permissions for a Local Service (Transact-SQL)"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  SQL Server enforces

  permission for each service and

  permissions for each queue.

  The security principal that owns the initiating serv
tags:
  - "service-broker"
  - "how-to-configure-permissions-for-a-local-service-transact-sql"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server enforces

permission for each service and

permissions for each queue.

The security principal that owns the initiating service must have

permission on the target

service. The security principal for an application must have

permission for each queue

that the application receives messages from.

This procedure is a simplified form of the procedure for creating a remote security

configuration. In both cases, you grant

permission on the destination service and

permission on the queue for the service that sends the messages. For a remote security

configuration, however, you must also configure Service Broker security to correctly identify the

remote user. For a configuration within a single database, you only need to grant permissions.

1. Grant permission for the user to receive from the queue that the application uses.

2. Grant permission for the user that owns the initiating service to send messages to the

services that the application communicates with.

This example configures permissions to allow

to send messages from

the service that uses the queue

to the service Ordering. This procedure

assumes that the user, the services, and the queue already exist.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
SEND
RECEIVE
SEND
RECEIVE
SEND
RECEIVE
BrokerApplicationUser
StoreFrontQueue
AdventureWorks2022
```
