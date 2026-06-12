---
title: "Operating system task scheduling"
topic: "thread-task"
description: ""
tags: ["thread-task","architecture"]
pubDate: "2026-05-29"
---

Threads are the smallest units of processing that are executed by an operating system, and

allow the application logic to be separated into several concurrent execution paths. Threads are

useful when complex applications have many tasks that can be performed at the same time.

When an operating system executes an instance of an application, it creates a unit called a

process to manage the instance. The process has a thread of execution. This is the series of

programming instructions performed by the application code. For example, if a simple

application has a single set of instructions that can be performed serially, that set of

instructions is handled as a single

task

, and there is just one execution path (or

thread

) through

the application. More complex applications may have several

tasks

that can be performed

concurrently instead of serially. An application can do this by starting separate processes for

each task, which is a resource-intensive operation, or start separate threads, which are relatively

less resource-intensive. Additionally, each thread can be scheduled for execution

independently from the other threads associated with a process.

Threads allow complex applications to make more effective use of a processor (CPU), even on

computers that have a single CPU. With one CPU, only one thread can execute at a time. If one

thread executes a long-running operation that doesn't use the CPU, such as a disk read or

write, another one of the threads can execute until the first operation is completed. By being

able to execute threads while other threads are waiting for an operation to be completed, an

application can maximize its use of the CPU. This is especially true for multi-user, disk I/O

intensive applications such as a database server. Computers that have multiple CPUs can

execute one thread per CPU at the same time. For example, if a computer has eight CPUs, it

can execute eight threads at the same time.

In the scope of SQL Server, a

request

is the logical representation of a query or batch. A request

also represents operations required by system threads, such as checkpoint or log writer.

Requests exist in various states throughout their lifetime and can accumulate waits when

resources required to execute the request aren't available, such as

locks

or

latches. For more

information about request states, see

sys.dm_exec_requests.

task scheduling
