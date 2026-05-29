---
title: "Remote Service Bindings"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  A remote service binding establishes a relationship between a local database user, the
  
  certificate for the user, and the name of a rem
tags:
  - "service-broker"
  - "remote-service-bindings"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

A remote service binding establishes a relationship between a local database user, the

certificate for the user, and the name of a remote service. Service Broker uses the remote

service binding to provide dialog security for conversations that target the remote service.

Service Broker determines the users for a conversation when a conversation begins, using the

information in the database that hosts the initiating service. A conversation that uses dialog

security involves four users. Each database must contain a user for the initiator of the

conversation and a user for the target of the conversation. The initiator of the conversation is

the user that begins the dialog. The remote service binding specifies the user for the target of

the conversation. An initiating service can act as

in the remote database by specifying

=

in the remote service binding.

CREATE CERTIFICATE (Transact-SQL)

CREATE LOGIN (Transact-SQL)

CREATE USER (Transact-SQL)

CREATE REMOTE SERVICE BINDING (Transact-SQL)

ALTER REMOTE SERVICE BINDING (Transact-SQL)

DROP REMOTE SERVICE BINDING (Transact-SQL)

```sql
ANONYMOUS
ON
```