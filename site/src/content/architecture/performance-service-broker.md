---
title: "Performance (Service Broker)"
topic: "service-broker"
description: ""
tags: ["service-broker","performance-service-broker"]
pubDate: "2025-12-01"
---

The performance of a Service Broker application is generally determined by two factors:

The number of messages arriving within a specified period of time

The speed at which the application processes each message

Monitoring these two factors is the key to understanding the performance of the application.

Service Broker provides a set of performance counters that provide information on its activities.

Service Broker also logs serious errors to the SQL Server error log and the Windows Application

event log. For more information, see the following articles:

Service Broker Related Dynamic Management Views (Transact-SQL)

, Broker Statistics object

Broker Event Category

Usually, tuning a stored procedure that uses Service Broker is no different from tuning any

other stored procedure. However, there are a further considerations.

First, use the

clause. Messages seldom arrive at predictable intervals. Even in a service

where messages arrive at roughly the same rate that the stored procedure processes the

messages, there might be times when no messages are available. Therefore, the procedure

should use a

clause with a

statement or with a

statement. Without

, these statements return immediately when there are no available

messages on the queue. Depending on the implementation of the stored procedure, the

procedure might then loop back through the statement, consuming resources needlessly, or

the procedure might exit only to be reactivated shortly thereafter, consuming more resources

than simply continuing to run.

You allow for the unpredictability in timing by using the

clause with the

or

statement. If your application runs continuously as a background

service, you don't specify a timeout in the

statement. If your application is activated by

Service Broker or runs as a scheduled job, you specify a short timeout; for example, 500

milliseconds. An application that uses the

statement gracefully handles unpredictable

intervals between messages. Likewise, an activated application that exits after a short timeout

doesn't consume resources when there are no messages to process.

```sql
WAITFOR
WAITFOR
RECEIVE
GET CONVERSATION GROUP
WAITFOR
WAITFOR
RECEIVE
GET CONVERSATION GROUP
WAITFOR
WAITFOR
```
