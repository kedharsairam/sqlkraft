---
title: "Lesson 2: Creating an Internal Activation Procedure"
topic: "service-broker"
description: "09/04/2025 In this lesson, you learn to create a stored procedure to process messages from a Service Broker queue. You also learn how to specify"
tags: ["service-broker","lesson-2-creating-an-internal-activation-procedure"]
pubDate: "2025-12-01"
---

In this lesson, you learn to create a stored procedure to process messages from a Service

Broker queue. You also learn how to specify that the procedure is activated anytime there are

messages in the queue.

Copy and paste the following code into a Query Editor window, then run it to switch context to

the

database.

Copy and paste the following code into a Query Editor window, then run it to create a stored

procedure. When it runs, the stored procedure keeps receiving messages as long as there are

messages in the queue. If the receive times out without returning a message, the stored

procedure ends. If the received message was a request message, the stored procedure returns

a reply message. If the received message is an

message, the stored procedure ends

the target side of the conversation. If the received message is and

message, it rolls back

the transaction.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
AdventureWorks2022
EndDialog
Error
AdventureWorks2022
USE
AdventureWorks2022;
GO
```
