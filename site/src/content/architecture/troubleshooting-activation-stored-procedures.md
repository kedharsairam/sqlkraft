---
title: "Troubleshooting Activation Stored Procedures"
topic: "service-broker"
description: "09/11/2025 Activated stored procedures run on a background session. Therefore, the techniques for troubleshooting an activation stored procedure"
tags: ["service-broker","troubleshooting-activation-stored-procedures"]
pubDate: "2025-12-01"
---

Activated stored procedures run on a background session. Therefore, the techniques for

troubleshooting an activation stored procedure differ slightly those used for troubleshooting

stored procedures that are part of an interactive session.

If activated stored procedures don't run successfully, use the

utility to look for

configuration errors in the associated services. For more information, see

ssbdiagnose utility

(Service Broker).

If the activated stored procedure produces incorrect results or doesn't read from the queue,

check the SQL Server error log for errors and messages that help locate the problem. Activated

stored procedures aren't associated with any application. Information normally returned to the

calling application is instead put in the SQL Server error log. This includes errors, messages,

and the output of

and

statements.

To troubleshoot an activation stored procedure, you can turn off activation on the queue, and

then run the stored procedure from SQL Server Management Studio or the

sqlcmd

utility. If

you run the stored procedure from an interactive session, you can see any errors that are

returned by the stored procedure.

However, you might see different results if the security context and database settings are

different in the interactive session than when the stored procedure is activated by the Database

Engine. Before you run the procedure, do the following:

```sql
PRINT
RAISERROR
```
