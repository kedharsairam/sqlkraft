---
title: "Lesson 1: Creating the Base Conversation Objects"
topic: "service-broker"
description: |
  09/04/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  In this lesson, learn how to build all the objects that enable a database to support a

  conversation in the database.

  Copy and paste t
tags:
  - "service-broker"
  - "lesson-1-creating-the-base-conversation-objects"
pubDate: 2025-12-01
---

09/04/2025

SQL Server

Azure SQL Managed Instance

In this lesson, learn how to build all the objects that enable a database to support a

conversation in the database.

Copy and paste the following code into a Query Editor window. Then, run it to ensure that

Service Broker is enabled in the

database, and switch context to the

database.

Copy and paste the following code into a Query Editor window. Then, run it to create the

message types for the conversation. Because Service Broker objects are often referenced across

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
AdventureWorks2022
AdventureWorks2022
USE master
;
GO
ALTER
DATABASE
AdventureWorks2022
SET
ENABLE_BROKER;
GO
USE
AdventureWorks2022;
GO
```
