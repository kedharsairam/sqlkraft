---
title: "Lesson 1: Creating the Databases"
topic: "service-broker"
description: "09/04/2025 In this lesson, you learn to create the databases and enable the trustworthy option. Copy and paste the following code into a Query Ed"
tags: ["service-broker","lesson-1-creating-the-databases"]
pubDate: 2025-12-01
---

In this lesson, you learn to create the databases and enable the trustworthy option.

Copy and paste the following code into a Query Editor window, then run it to create the

databases for this tutorial. By default, new databases have the

option set

to on. Setting the

option in the

lets you start conversations in

that database that reference target services in the.

```sql
ENABLE_BROKER
TRUSTWORTHY
InitiatorDB
TargetDB
USE master
;
GO
IF EXISTS (
SELECT
*
FROM sys.databases
WHERE name
= N
'TargetDB'
)
DROP
DATABASE
TargetDB;
GO
CREATE
DATABASE
TargetDB;
GO
IF EXISTS (
SELECT
*
FROM sys.databases
WHERE name
= N
'InitiatorDB'
)
DROP
DATABASE
InitiatorDB;
GO
CREATE
DATABASE
InitiatorDB;
GO
ALTER
DATABASE
InitiatorDB
SET
TRUSTWORTHY
ON
;
GO
```
