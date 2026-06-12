---
name: "sys.events"
title: "sys.events"
category: "compatibility"
description: "The name of a predefined group of Transact-SQL or SQL Trace event types. An event notification can fire after execution of any event that belongs to an event group. For a list of DDL event groups, the Transact-SQL events they cover, and the scope at which they can be DDL Event Groups also acts as a macro, when the statement finishes, by adding the event types it covers to the Specifies the target"
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: "CREATE EVENT NOTIFICATION"
---

## Description

## Syntax

```sql
CREATE EVENT NOTIFICATION
```

## Permissions

## Remarks

The name of a predefined group of Transact-SQL or SQL Trace event types. An event

notification can fire after execution of any event that belongs to an event group. For a list of

DDL event groups, the Transact-SQL events they cover, and the scope at which they can be

defined, see

DDL Event Groups

event_group

also acts as a macro, when the

statement finishes, by

adding the event types it covers to the

catalog view.

Specifies the target service that receives the event instance data. SQL Server opens one or

more conversations to the target service for the event notification. This service must honor the

same SQL Server Events message type and contract that is used to send the message.

The conversations remain open until the event notification is dropped. Certain errors could

cause the conversations to close earlier. Ending some or all conversations explicitly might

prevent the target service from receiving more messages.

Specifies a service broker instance against which

broker_service

is resolved. The value for a

specific service broker can be acquired by querying the

column of the

catalog view. Use

to specify the service broker instance in

the current database.

is a case-insensitive string literal.

Service Broker includes a message type and contract specifically for event notifications.

Therefore, a Service Broker initiating service doesn't have to be created because one already

exists that specifies the following contract name:

The target service that receives event notifications must honor this preexisting contract.

This option isn't available in a contained database.
