---
title: "Lesson 4: Dropping the Conversation Objects"
topic: "service-broker"
description: ""
tags: ["service-broker","lesson-4-dropping-the-conversation-objects"]
pubDate: 2025-12-01
---

In this lesson, you learn to drop the objects that enabled a database to support a conversation

using an internal activation stored procedure.

Copy and paste the following code into a Query Editor window, then run it to switch context to

the

database.

Copy and paste the following code into a Query Editor window, then run it to drop the objects

that were used to support the conversation.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
AdventureWorks2022
AdventureWorks2022
USE
AdventureWorks2022;
GO
IF EXISTS (
SELECT
*
FROM sys.objects
WHERE name
= N
'TargetActiveProc'
)
DROP
PROCEDURE
TargetActiveProc;
IF EXISTS (
SELECT
*
FROM sys.services
WHERE name
= N
'//AWDB/InternalAct/TargetService'
)
DROP
SERVICE [//AWDB/InternalAct/TargetService];
```
