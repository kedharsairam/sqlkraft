---
title: "Lesson 3: Dropping the Conversation Objects"
topic: "service-broker"
description: "09/11/2025 In this lesson, you learn to drop the objects that enabled a database to support a conversation in the database. Copy and paste the f"
tags: ["service-broker","lesson-3-dropping-the-conversation-objects"]
pubDate: "2025-12-01"
---

In this lesson, you learn to drop the objects that enabled a database to support a conversation

in the database.

Copy and paste the following code into a Query Editor window, then run it to switch

context to the AdventureWorks2008R2 database.

Copy and paste the following code into a Query Editor window, then run it to drop the

objects that were used to support the conversation.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
AdventureWorks2022
USE
AdventureWorks2008R2;
GO
IF EXISTS (
SELECT
*
FROM sys.services
WHERE name
= N
'//AWDB/1DBSample/TargetService'
)
DROP
SERVICE [//AWDB/1DBSample/TargetService];
IF EXISTS (
SELECT
*
FROM sys.service_queues
WHERE name
= N
'TargetQueue1DB'
)
DROP
QUEUE TargetQueue1DB;
```
