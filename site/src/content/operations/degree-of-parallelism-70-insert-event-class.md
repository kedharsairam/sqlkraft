---
title: "Degree of Parallelism (7.0 Insert) Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","degree-of-parallelism-70-insert-event-class"]
pubDate: "2025-12-01"
---

The

event class occurs each time SQL Server executes a

SELECT, INSERT, UPDATE, or DELETE statement.

When this event class is included in a trace, the amount of entailed overhead may significantly

impede performance if these events occur frequently. To minimize overhead incurred, limit use

of this event class to traces that briefly monitor specific problems.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

Number of CPUs used to complete the process

based on the following values:

0x00000000, indicates a serial plan running in

serial.

0x01000000, indicates a parallel plan running in

serial.

> = 0x02000000 indicates a parallel plan

running in parallel.

2

No

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

process ID is provided by the client.

9

Yes

ﾉ

Expand table
