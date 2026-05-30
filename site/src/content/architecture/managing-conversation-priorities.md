---
title: "Managing Conversation Priorities"
topic: "service-broker"
description: |
  09/10/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker conversation priorities let you specify which conversations to prioritize so that

  their messages aren't blocked by larg
tags:
  - "service-broker"
  - "managing-conversation-priorities"
pubDate: 2025-12-01
---

09/10/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker conversation priorities let you specify which conversations to prioritize so that

their messages aren't blocked by large numbers of messages from less important

conversations.

Conversation priorities are always active for

statements. The

database option must be on to make conversation priorities active

for

statements. By default, this option is off for all databases.

An administrator can enable conversation priorities for

statements in a database by using

the following statement:

SQL

An administrator can turn off conversation priorities for

statements by using the

following statement:

SQL

Conversation priorities are specified by using the

,

, and

statements. For more information, see

Conversation

priorities

.

```sql
RECEIVE
SEND
SEND
SEND
CREATE BROKER PRIORITY
ALTER BROKER
PRIORITY
DROP BROKER PRIORITY
ALTER
DATABASE
MyDatabase
SET
HONOR_BROKER_PRIORITY
ON
;
ALTER
DATABASE
MyDatabase
SET
HONOR_BROKER_PRIORITY
OFF
;
```
