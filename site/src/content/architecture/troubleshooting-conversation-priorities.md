---
title: "Troubleshooting Conversation Priorities"
topic: "service-broker"
description: |
  09/03/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article provides suggestions for correcting common symptoms related to Service Broker

  conversation priorities.

  Use the

  column t
tags:
  - "service-broker"
  - "troubleshooting-conversation-priorities"
pubDate: 2025-12-01
---

09/03/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article provides suggestions for correcting common symptoms related to Service Broker

conversation priorities.

Use the

column to determine the state of the

database option:

SQL

Open a SQL Server Profiler trace and review the Broker Remote Message Ack events. A value of

1 in the

column indicates the priority of messages was elevated to

prevent starvation. A value of 0 in the

column indicates the

option wasn't enabled in the sending database.

Also review the Broker/DBM Transport System Monitor counter to see the transmission rates

for messages of different priority levels.

```sql
sys.databasesis_broker_priority_honored
HONOR_BROKER_PRIORITY
StarvationElevation
HonorBrokerPriority
HONOR_BROKER_PRIORITY
SELECT
name
AS
database_name,
CASE
is_broker_priority_honored
WHEN
0
THEN
N
'OFF'
WHEN
1
THEN
N
'ON'
END
AS
is_broker_priority_honored
FROM
sys.databases
ORDER
BY
database_name;
```
