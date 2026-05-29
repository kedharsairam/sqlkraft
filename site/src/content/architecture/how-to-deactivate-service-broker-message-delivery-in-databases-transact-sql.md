---
title: "How to: Deactivate Service Broker Message Delivery in Databases (Transact-SQL)"
topic: "service-broker"
description: |
  09/02/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  When message delivery isn't active, messages remain in the transmission queue. To determine
  
  whether Service Broker is active for a dat
tags:
  - "service-broker"
  - "how-to-deactivate-service-broker-message-delivery-in-databases-transact-sql"
pubDate: 2025-12-01
---

09/02/2025

Applies to:

SQL Server

Azure SQL Managed Instance

When message delivery isn't active, messages remain in the transmission queue. To determine

whether Service Broker is active for a database, check the

column of the

catalog view.

Alter the database to set the

option.

SQL

７

Note

Deactivating Service Broker prevents messages from being sent from or delivered to the

database. However, this doesn't prevent messages from arriving in the instance. To

prevent messages from arriving in the instance, you must remove or stop the Service

Broker endpoint.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
is_broker_enabled
sys.databases
DISABLE_BROKER
AdventureWorks2022
USE
master
;
GO
ALTER
DATABASE
AdventureWorks2008R2
SET
DISABLE_BROKER;
GO
```