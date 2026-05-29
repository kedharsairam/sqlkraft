---
title: "How to: Activate Service Broker Message Delivery in Databases (Transact-SQL)"
topic: "service-broker"
description: |
  ﾃ
  
  Summarize this article for me
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  By default,
  
  Service Broker
  
  is enabled and message delivery is active in a database when the
  
  database is create
tags:
  - "service-broker"
  - "how-to-activate-service-broker-message-delivery-in-databases-transact-sql"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

Applies to:

SQL Server

Azure SQL Managed Instance

By default,

Service Broker

is enabled and message delivery is active in a database when the

database is created. When message delivery isn't active, messages remain in the transmission

queue. To determine whether Service Broker is active for a database, check the

column of the

catalog view.

Service Broker is enabled by default when a database is created. You can use the

ALTER

DATABASE

statement to disable Service Broker message delivery in a database. When you

disable Service Broker, messages remain in the transmission queue and aren't delivered to the

database.

To disable Service Broker, run the following Transact-SQL script:

SQL

７

Note

Activating Service Broker allows messages to be delivered to the database. You must

create a Service Broker endpoint to send and receive messages from outside of the

instance.

７

Note

If Service Broker is disabled on a database migrated to Azure SQL Managed Instance,

enabling Service Broker on the target SQL managed instance isn't available. To use Service

Broker on the target SQL managed instance, enable it on the source SQL Server database

before you migrate to SQL managed instance.

```sql
is_broker_enabled
sys.databases
USE
master
;
GO
ALTER
DATABASE
[<
database
name
>]
SET
DISABLE_BROKER;
```