---
title: "Querying Queues"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Sometimes it might be necessary to inspect the content of a queue as a whole. You might want
  
  to know how many messages the queue conta
tags:
  - "service-broker"
  - "querying-queues"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Sometimes it might be necessary to inspect the content of a queue as a whole. You might want

to know how many messages the queue contains, or you might want to ensure that the

application has processed all of the messages for a service that you're about to take offline.

You might need to find out why messages aren't being processed by an application.

To get this information, use the name of the queue as the source table of a

statement.

A

statement on a queue has the same format as a

statement on a view or a

table.

Following is an example

statement to find out the number of messages in the queue

:

SQL

The following

statement lets the administrator learn whether the queue

contains any messages for the service

:

SQL

７

Note

Service Broker is designed to allow multiple queue readers to efficiently receive messages

from a queue. However, a

statement on a queue might cause blocking. When

using a

statement on a queue, specify the

hint to avoid blocking

applications that use the queue. For a description of the columns in a queue, see

.

```sql
SELECT
SELECT
SELECT
SELECT
SELECT
SELECT
SELECT
NOLOCK
SELECT
COUNT
(*)
FROM
dbo.ExpenseQueue
WITH
(NOLOCK);
IF EXISTS (
SELECT
*
FROM
dbo.ExpenseQueue
WITH
(NOLOCK)
WHERE
service_name =
'//Adventure-Works.com/AccountsPayable/Expenses'
)
PRINT
'The queue contains messages for '
+
'//Adventure-
Works.com/AccountsPayable/Expenses'
;
ELSE
```