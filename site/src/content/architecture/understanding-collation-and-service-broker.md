---
title: "Understanding Collation and Service Broker"
topic: "service-broker"
description: "09/11/2025 Service Broker is designed to let services and applications communicate easily and efficiently in instances with different collation c"
tags: ["service-broker","understanding-collation-and-service-broker"]
pubDate: 2025-12-01
---

Service Broker is designed to let services and applications communicate easily and efficiently in

instances with different collation configurations. The database that hosts a service that sends a

message might not use the same collation as the database that hosts the service that receives

the message. Therefore, Service Broker uses a consistent collation for names, regardless of the

collation of the database that hosts the service. To remove collation information from the

communication process, Service Broker uses a byte-by-byte comparison to match service

names, contract names, and message type names. By matching names as sequences of bytes,

Service Broker makes it simple for services to exchange messages correctly without the extra

overhead of exchanging collation information.

The byte-by-byte match is effectively a binary comparison that doesn't consider the current

collation. For this reason, many broker services find it convenient to follow the

recommendations in

Name Service Broker objects. An application that follows these guidelines

and treats all names as case-sensitive should function correctly regardless of differences in

collation between the database that hosts the target service and the database that hosts the

initiating service.

Queues use a consistent collation regardless of the default collation of the SQL Server instance

or the default collation of the database that hosts the queue. If a queue is the target of a

statement that includes a

statement with another table in the database, such as a

table used to maintain state, you might be required to explicitly specify the collation for the

comparison.

For example, an application that uses message retention might need to preserve some

messages for a conversation before the application ends the conversation. The following

Transact-SQL code sample saves all messages for a given conversation that have a message

type name in the table

:

```sql
SELECT
JOIN
AuditedMessageTypes
IF @messageTypeName = 'https://schemas.microsoft.com/SQL/ServiceBroker/EndDialog'
BEGIN
INSERT
INTO dbo.AuditRecord
SELECT q.message_type_name,
q.message_body
FROM dbo.ApplicationQueue
AS q
```
