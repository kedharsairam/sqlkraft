---
title: "Lesson 1: Creating the Conversation Objects"
topic: "service-broker"
description: "09/04/2025 In this lesson, you learn to build all the objects that enable a database to support a conversation in the database. Copy and paste t"
tags: ["service-broker","lesson-1-creating-the-conversation-objects"]
pubDate: "2025-12-01"
---

In this lesson, you learn to build all the objects that enable a database to support a

conversation in the database.

Copy and paste the following code into a Query Editor window. Then, run it to ensure

that Service Broker is enabled in the AdventureWorks2008R2 database, and switch

context to the database.

Copy and paste the following code into a Query Editor window, then run it to create the

message types for the conversation. Because Service Broker objects are often referenced

across multiple instances of the Database Engine, most Service Broker objects are given

names in a URI format. This helps ensure that they are unique across multiple computers.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
AdventureWorks2022
USE master
;
GO
ALTER
DATABASE
AdventureWorks2008R2
SET
ENABLE_BROKER;
GO
USE
AdventureWorks2008R2;
GO
```
