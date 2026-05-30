---
title: "Restrictions"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  This article discusses the restrictions associated with code executing in the SQL Server process

  through context and regular connections.

  When develo
tags:
  - "clr-integration"
  - "restrictions"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

This article discusses the restrictions associated with code executing in the SQL Server process

through context and regular connections.

When developing your application, take into account the following restrictions that apply to

context connections:

You can have only one context connection open at a given time for a given connection. If

you have multiple statements running concurrently in separate connections, each one of

them can get their own context connection. The restriction doesn't affect concurrent

requests from different connections; it only affects a given request on a given connection.

Multiple Active Result Sets (MARS) isn't supported in a context connection.

The

class doesn't operate in a context connection.

Update batching in a context connection isn't supported

can't be used with commands that execute against a context

connection.

Canceling commands that are running against the context connection isn't supported.

The

method silently ignores the request.

No other connection string keywords can be used when you use

.

The

property returns null if the connection string for the

is

, instead of the name of the instance of SQL

Server.

Setting the

property has no effect when the command is

executed against a context connection.

```sql
SqlBulkCopy
SqlNotificationRequest
SqlCommand.Cancel
context
connection=true
SqlConnection.DataSource
SqlConnection
context connection=true
SqlCommand.CommandTimeout
```
