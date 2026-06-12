---
title: "Avoid the use of SQL Trace and SQL Server Profiler"
topic: "query-processing"
description: "The performance of index operations such as creating or rebuilding indexes can be improved"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

The performance of index operations such as creating or rebuilding indexes can be improved

on computers that have many CPUs by temporarily setting the recovery model of the database

to either the bulk-logged or simple recovery model. These index operations can generate

significant log activity and log contention can affect the best degree of parallelism (DOP)

choice made by SQL Server.

In addition to adjusting the

server configuration option,

consider adjusting the parallelism for index operations using the

MAXDOP option. For more

information, see

Configure Parallel Index Operations. For more information and guidelines

about adjusting the max degree of parallelism server configuration option, see

Configure the

max degree of parallelism server configuration option.

dynamically configures the

server configuration option at

startup. SQL Server uses the number of available CPUs and the system architecture to

determine this server configuration during startup, using a documented

formula.

This option is an advanced option, and should be changed only by an experienced database

professional.

If you suspect that there is a performance problem, it is probably not the availability of worker

threads. The cause is more likely something like I/O that is causing the worker threads to wait.

It is best to find the root cause of a performance issue before you change the max worker

threads setting. However, if you need to manually set the maximum number of worker threads,

this configuration value must always be set to a value of at least seven times the number of

CPUs that are present on the system. For more information, see

Configure the max worker

threads.

We recommend that you don't use SQL Trace and SQL Profiler in a production environment.

The overhead for running these tools also increases as the number of CPUs increases. If you

must use SQL Trace in a production environment, limit the number of trace events to a

minimum. Carefully profile and test each trace event under load, and avoid using combinations

of events that significantly affect performance.

）

Important

### Extended Events

### Quick Start:

### Extended events in SQL Server

### SSMS XEvent Profiler
