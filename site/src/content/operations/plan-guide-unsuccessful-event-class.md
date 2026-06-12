---
title: "Plan Guide Unsuccessful Event Class"
topic: "event-classes"
description: |
  Article

  •

  07/25/2023

  Applies to:

  SQL Server

  The Plan Guide Unsuccessful event class indicates that SQL Server could not produce an

  execution plan for a query or batch that contained a plan guide
tags:
  - "event-classes"
  - "plan-guide-unsuccessful-event-class"
pubDate: 2025-12-01
---

Article

•

07/25/2023

SQL Server

The Plan Guide Unsuccessful event class indicates that SQL Server could not produce an

execution plan for a query or batch that contained a plan guide. Instead, the plan was

compiled without using the plan guide. The event fires when the following conditions are true:

The batch/module in the plan guide definition matches the batch that is being executed.

The query in the plan guide definition matches the query that is being executed.

The hints in the plan guide definition, including the

hint, were not applied

successfully to the query or batch. That is, the compiled query plan could not honor the

specified hints and the plan was compiled without using the plan guide.

An invalid plan guide might cause this event to fire. Validate the plan guide that is used by the

query or batch by using the

sys.fn_validate_plan_guide

function, and correct the error that is

reported by this function.

This event is included in the SQL Server Profiler Tuning template.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values that are

passed by the application instead of the

displayed name of the program.

10

Yes

ClientProcessID

ID assigned by the host computer to the process

where the client application is running. This data

column is populated if the client provides the

client process ID.

9

Yes

７

Note

This event class is not available in Azure SQL Database.

ﾉ

Expand table

```cmd
USE PLAN
```
