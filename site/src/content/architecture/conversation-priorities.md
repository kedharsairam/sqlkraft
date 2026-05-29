---
title: "Conversation Priorities"
topic: "service-broker"
description: |
  08/29/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Conversation priorities are a set of user-defined rules, each of which specifies a priority level
  
  and the criteria for determining whi
tags:
  - "service-broker"
  - "conversation-priorities"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Conversation priorities are a set of user-defined rules, each of which specifies a priority level

and the criteria for determining which Service Broker conversations to assign the priority level.

Messages from conversations that have high priority levels are typically sent or received before

messages from conversations that have low priority levels.

Conversation priorities can be used to do the following:

Identify conversations that have precedence over others.

Support different tiers of service, where messages from customers who pay higher rates

are sent before messages from customers who pay lower rates.

Favor customer requests over background tasks. For example, new customer registrations

should have a higher priority than sending business transaction summaries to a data

warehouse.

Conversation priorities are created in each database using the

statement. Each conversation priority defines the following:

A name for the conversation priority.

A priority level to assign Service Broker conversations. The levels are specified as integers

from 1 (lowest) to 10 (highest). The default is 5.

The criteria that determine which conversations the priority level applies to the following:

A contract name, or

A local service name, or

A remote service name, or

Service Broker assigns the priority levels to conversation endpoints when the endpoints are

created. Each conversation has two conversation endpoints:

```sql
CREATE BROKER PRIORITY
ANY
ANY
ANY
```