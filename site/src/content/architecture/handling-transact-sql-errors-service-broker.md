---
title: "Handling Transact-SQL Errors (Service Broker)"
topic: "service-broker"
description: |
  08/29/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Two general principles apply when handling Transact-SQL errors in a Service Broker application.
  
  First, an application shouldn't perman
tags:
  - "service-broker"
  - "handling-transact-sql-errors-service-broker"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Two general principles apply when handling Transact-SQL errors in a Service Broker application.

First, an application shouldn't permanently remove a message from a queue without acting

upon the message. In most cases, this means that an application should always receive a

message within a transaction.

Second, an application should always hold a lock on a conversation group before updating the

state of the conversation group or the state of any message in the conversation group. When

an application receives a message within a transaction, the application automatically locks the

conversation group.

SAVE TRANSACTION (Transact-SQL)

Understanding Database Engine Errors