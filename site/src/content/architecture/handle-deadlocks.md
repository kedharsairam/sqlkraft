---
title: "Handle deadlocks"
topic: "locking"
description: "SQL Profiler has an event that presents a graphical depiction of the tasks and resources"
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

SQL Profiler has an event that presents a graphical depiction of the tasks and resources

involved in a deadlock. The following example shows the output from SQL Profiler when the

deadlock graph event is turned on.

The SQL Profiler and SQL Trace features are deprecated and replaced by Extended Events.

Extended Events has a smaller performance overhead, and is more configurable than SQL

Trace. Consider using the

Extended Events deadlock event

instead of tracing deadlocks in SQL

Profiler.

For more information about the deadlock event, see

Lock:Deadlock Event Class. For more

information about SQL Profiler deadlock graphs, see

Save deadlock graphs (SQL Server

Profiler).

Extended Events provides equivalents of SQL Trace event classes. For more information, see

View the Extended Events Equivalents to SQL Trace Event Classes. Extended Events is

recommended over SQL Trace.

When an instance of the Database Engine chooses a transaction as a deadlock victim, it

terminates the current batch, rolls back the transaction, and returns error 1205 to the

application. The returned message is structured as follows:

Because any application submitting Transact-SQL queries can be chosen as the deadlock victim,

applications should have an error handler that can handle error 1205. If an application doesn't

handle the error, the application can proceed unaware that its transaction has been rolled back.

Implementing an error handler that catches error 1205 allows an application to handle

deadlocks and take remedial action (for example, automatically resubmitting the query that

```sql
Your transaction (process ID #.) was deadlocked on {lock | communication buffer |
thread} resources with another process and has been chosen as the deadlock victim. Rerun your transaction.
```
