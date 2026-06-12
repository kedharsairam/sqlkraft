---
title: "SqlTriggerContext Object"
topic: "clr-integration"
description: |
  SqlTriggerContext object

  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  The .NET Framework common language runtime (CLR)

  class provides

  context information about the trigger. This contextual info
tags:
  - "clr-integration"
  - "sqltriggercontext-object"
pubDate: 2025-12-01
---

SqlTriggerContext object

Article

•

12/30/2024

SQL Server

The.NET Framework common language runtime (CLR)

class provides

context information about the trigger. This contextual information includes the type of action

that caused the trigger to fire, which columns were modified in an

operation, and, with

a data definition language (DDL) trigger, an XML

structure that describes the

triggering operation.

For more information and examples of how to use the

class, see

CLR

triggers

and

Microsoft.SqlServer.Server.SqlTriggerContext.

CLR triggers

EVENTDATA (Transact-SQL)

```sql
SqlTriggerContext
UPDATE
EventData
SqlTriggerContext
```
