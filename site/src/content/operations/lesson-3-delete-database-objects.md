---
title: "Lesson 3: Delete database objects"
topic: "configuration"
description: "This short lesson removes the objects that you created in Le"
tags: ["configuration","lesson-3-delete-database-objects"]
pubDate: 2025-12-01
---

Analytics Platform System (PDW)

This short lesson removes the objects that you created in Lesson 1 and Lesson 2, and then

drops the database.

Before you delete objects, make sure you are in the correct database:

Use the

statement to remove execute permission for

on the stored procedure:

1. Use the

statement to remove permission for

to access the

database:

2. Use the

statement to remove permission for

to access this instance of SQL

Server 2005 (9.x):

７

Note

The

learning path provides more in-depth

content, along with practical examples.

```cmd
REVOKE
Mary
DROP
Mary
TestData
```
