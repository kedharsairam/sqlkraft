---
title: "Identity and Access Control (Service Broker)"
topic: "service-broker"
description: |
  09/02/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Most Service Broker applications that involve more than one instance run in the security

  context of a database principal created speci
tags:
  - "service-broker"
  - "identity-and-access-control-service-broker"
pubDate: 2025-12-01
---

09/02/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Most Service Broker applications that involve more than one instance run in the security

context of a database principal created specifically for the application. These database

principals should have the minimum permissions required to accomplish the tasks that the

application performs.

The following considerations apply to database principals created for Service Broker

applications:

Service Broker remote authorization applies when a remote Service Broker application

connects to SQL Server and delivers a message to the instance. The database principal

specified for remote authorization must have

permission in the database that

hosts the initiating service and must have

permission for the initiating service itself.

The user must own the certificate used for authentication. There are no requirements for

the user to own other objects, to have other permissions, or to be able to log in with any

other mechanism.

For a database principal to begin a conversation, that principal must have

permissions on the queue for the initiating service.

The database principal that owns the initiating service must have

permissions on the

target service.

For a database principal to send messages to a service, that principal must have

permissions on the service. For services hosted in a different instance, Service Broker

dialog security determines the database principal in the remote instance. For more

information, see

Service Broker Dialog Security

. Service Broker doesn't consider

membership in Windows roles when checking

permissions.

The user specified as the user for an activation stored procedure must have permission to

execute the procedure. Frequently, the user specified has the permissions required to

execute the statements in the procedure. Notice, however, that if the stored procedure

itself is defined with an

clause, the statements in the stored procedure run

with the security context defined by the stored procedure. SQL Server first sets the

security context to the user specified for the queue. SQL Server then executes the stored

procedure and the stored procedure changes the security context to the user specified for

the procedure.

```sql
CONNECT
SEND
RECEIVE
SEND
SEND
SEND
EXECUTE AS
```
