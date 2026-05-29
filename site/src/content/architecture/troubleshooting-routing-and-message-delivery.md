---
title: "Troubleshooting Routing and Message Delivery"
topic: "service-broker"
description: |
  09/15/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This section provides suggestions to correct common problems related to routing and
  
  message delivery.
  
  If messages aren't successfully
tags:
  - "service-broker"
  - "troubleshooting-routing-and-message-delivery"
pubDate: 2025-12-01
---

09/15/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This section provides suggestions to correct common problems related to routing and

message delivery.

If messages aren't successfully delivered between two services, use the

utility to

generate a runtime report of a conversation. The runtime report displays any errors

encountered by the conversation operations. If errors are encountered,

also

analyzes the configuration between the services and report any configuration problems it finds.

For more information, see

ssbdiagnose utility (Service Broker)

.

Ensure that Service Broker message delivery is activated in the database. The

column of

shows whether broker message delivery is

activated, as shown in the following sample:

SQL

You can deactivate Broker message delivery to prevent messages from being delivered to the

wrong database. For more information about Service Broker message delivery, see

Manage

Service Broker identities

. For more information about how to activate Service Broker message

delivery, see

How to: Activate Service Broker message delivery in databases

.

If Service Broker message delivery is active, check the

column in the

catalog view for the messages. Common error messages include:

ﾉ

Expand table

```sql
is_broker_enabled
sys.databases
transmission_status
sys.transmission_queue
SELECT
is_broker_enabled
FROM
sys.databases
WHERE
database_id = DB_ID();
```