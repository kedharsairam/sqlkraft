---
title: "Internal Activation Context"
topic: "service-broker"
description: |
  09/03/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes the execution context for a stored procedure that is started by internal

  activation.

  A queue configured for ac
tags:
  - "service-broker"
  - "internal-activation-context"
pubDate: 2025-12-01
---

09/03/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes the execution context for a stored procedure that is started by internal

activation.

A queue configured for activation must also specify the user that the activation stored

procedure runs as. SQL Server impersonates this user before starting the stored procedure.

When the stored procedure also specifies an

clause, two impersonations occur.

SQL Server first impersonates the user specified for the queue and executes the stored

procedure. When the stored procedure executes, the procedure impersonates the user

specified in the

clause of the procedure.

The user specified for a remote service binding is generally a different user from the user

specified for activation. The permissions required for each user also differ. The remote service

binding user doesn't need permission to read from the queue or execute stored procedures in

the database, while the user specified for activation doesn't need permission to send messages

to the service. For more information on user permissions, see

Identity and access control

(Service Broker)

and

Service Broker dialog security

.

Service Broker executes internally activated service programs on a background session distinct

from the connection that created the message. The options set for this session are the default

options for the database.

Within a session started by Service Broker, SQL Server writes the output of

and

statements to the SQL Server error log. Service Broker doesn't provide parameters

to an activated stored procedure. Service Broker doesn't consider return values from an

activated stored procedure and doesn't process result sets from an activated stored procedure.

An activated stored procedure is responsible for managing transactions. SQL Server doesn't

start a transaction before activating the stored procedure, and the stored procedure runs in a

```sql
EXECUTE AS
EXECUTE AS
PRINT
RAISERROR
```
