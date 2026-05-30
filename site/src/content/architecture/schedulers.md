---
title: "Schedulers"
topic: "thread-task"
description: "What the actual available"
tags: ["thread-task", "architecture"]
pubDate: 2026-05-29
---

What the actual available

degree of parallelism (DOP)

in the system is, based on current

load. This may differ from estimated DOP, which is based on the server configuration for

max degree of parallelism (MAXDOP). For example, the server configuration for MAXDOP

may be 8 but the available DOP at runtime can be only 2, which affects query

performance. Memory pressure and lack of workers are two conditions which reduce

available DOP at runtime.

A

scheduler

, also known as SOS scheduler, manages worker threads that require processing

time to carry out work on behalf of tasks. Each scheduler is mapped to an individual processor

(CPU). The time a worker can remain active in a scheduler is called the OS quantum, with a

maximum of 4 ms. After its quantum time expires, a worker yields its time to other workers that

need to access CPU resources, and changes its state. This cooperation between workers to

maximize access to CPU resources is called

cooperative scheduling

, also known as non-

preemptive scheduling. In turn, the change in worker state is propagated to the task associated

with that worker, and to the request associated with the task. For more information about

worker states, see

sys.dm_os_workers

. For more information about schedulers, see

sys.dm_os_schedulers

.

In summary, a

request

may spawn one or more

tasks

to carry out units of work. Each task is

assigned to a

worker thread

who is responsible for completing the task. Each worker thread

must be scheduled (placed on a

scheduler

) for active execution of the task.

Consider the following scenario:

Worker 1 is a long-running task, for example a read query using read-ahead over disk-

based tables. Worker 1 finds its required data pages are already in Buffer Pool, so it

doesn't have to yield to wait for I/O operations, and can consume its full quantum before

yielding.

Worker 2 is doing shorter sub-millisecond tasks and therefore is required to yield before

its full quantum is exhausted.

７

Note

The

limit is set per task, not per request. This

means that during a parallel query execution, a single request can spawn multiple tasks up

to the MAXDOP limit, and each task will use one worker. For more information about

MAXDOP, see

.
