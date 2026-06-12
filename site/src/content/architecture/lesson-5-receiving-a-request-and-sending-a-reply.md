---
title: "Lesson 5: Receiving a Request and Sending a Reply"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  In this lesson, you learn how to receive a request message from the target queue and send a

  reply message to the initiator service. Ru
tags:
  - "service-broker"
  - "lesson-5-receiving-a-request-and-sending-a-reply"
pubDate: 2025-12-01
---

09/11/2025

SQL Server

Azure SQL Managed Instance

In this lesson, you learn how to receive a request message from the target queue and send a

reply message to the initiator service. Run these steps from a copy of Management Studio

that's running on the same computer as the target instance of the Database Engine.

Copy and paste the following code into a Query Editor window, then run it to switch

context to the

database where you receive the request message and send a

reply message back to the.

Copy and paste the following code into a Query Editor window. Then, run it to receive the

reply message from the

and send a reply message back to the initiator.

The

statement retrieves the request message, then the following

statement displays the text so that you can verify that it's the same message that was sent

in the previous step. The

statement tests whether the received message is a request

message type, and if a

statement is used to send a reply message back to the

initiator. The

statement is used to end the target side of the

conversation. The final

statement displays the text of the reply message.

```sql
RECEIVE
SELECT
IF
SEND
END CONVERSATION
SELECT
USE
InstTargetDB;
GO
DECLARE
@RecvReqDlgHandle
AS
UNIQUEIDENTIFIER;
DECLARE
@RecvReqMsg
AS
NVARCHAR (100);
DECLARE
@RecvReqMsgName
AS sysname;
```
