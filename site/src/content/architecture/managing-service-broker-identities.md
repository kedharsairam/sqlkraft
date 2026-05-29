---
title: "Managing Service Broker Identities"
topic: "service-broker"
description: |
  09/03/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Each database contains a unique identifier that is used for routing Service Broker messages to

  that database. This topic describes Ser
tags:
  - "service-broker"
  - "managing-service-broker-identities"
pubDate: 2025-12-01
---

09/03/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Each database contains a unique identifier that is used for routing Service Broker messages to

that database. This topic describes Service Broker identifiers, how Service Broker protects

against message misdirection, and the options that are available to manage Service Broker

identifiers.

Each database contains a Service Broker identifier that distinguishes it from all other databases

in the network. The

column of the

catalog view shows the

Service Broker identifier for each database in the instance. Service Broker systems can be

designed to run multiple copies of a service. Each copy of the service runs in a separate

database. In a system that has multiple copies of a service, use the

clause of

the

statement to create a route to a specific copy of the service.

Service Broker routing uses the Service Broker identifier to ensure that all messages for a

conversation are delivered to the same database. The

statement

opens a conversation with a destination service. If a conversation is successfully opened, the

acknowledgment message from the destination service contains the Service Broker identifier

for the destination database. Service Broker then routes all messages for the conversation to

the specified database.

Service Broker identifiers can be specified in the

clause of the

statement to control the type of routing to be performed:

To route conversations to a specific copy of a service, specify a

service_broker_guid

. For

example, you could have three copies of a service in three databases on the network: a

development database, a test database, and a production database. The

statements in each system should specify

service_broker_guid

to ensure that

all messages go to the correct database.

To let Service Broker balance conversation loads across multiple copies of a service, don't

specify

service_broker_guid

. Service Broker will alternatively pick among the routes with

the same service name as is specified in the

clause of

.

```sql
service_broker_guid
sys.databases
BROKER_INSTANCE
CREATE ROUTE
BEGIN DIALOG CONVERSATION
TO SERVICE
BEGIN DIALOG
CONVERSATION
BEGIN DIALOG
CONVERSATION
TO SERVICE
BEGIN DIALOG
CONVERSATION
```
