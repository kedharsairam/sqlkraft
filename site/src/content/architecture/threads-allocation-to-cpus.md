---
title: "Threads allocation to CPUs"
topic: "thread-task"
description: ""
tags: ["thread-task","architecture"]
pubDate: 2026-05-29
---

A worker thread can only remain active in the scheduler during its quantum (4 ms) and must

yield its scheduler after that quantum has elapsed, so that a worker thread assigned to another

task may become active. When a worker's quantum expires and is no longer active, the

respective task is placed in a FIFO queue in a RUNNABLE state, until it moves to a RUNNING

state again, assuming the task doesn't require access to resources that aren't available at the

moment, such as a latch or lock, in which case the task would be placed in a SUSPENDED state

instead of RUNNABLE, until such time those resources are available.

In summary, a parallel request spawns multiple tasks. Each task must be assigned to a single

worker thread. Each worker thread must be assigned to a single scheduler. Therefore, the

number of schedulers in use can't exceed the number of parallel tasks per branch, which is set

by the MaxDOP configuration or query hint. The coordinating thread doesn't contribute to the

MaxDOP limit.

By default, each instance of SQL Server starts each thread, and the operating system distributes

threads from instances of SQL Server among the processors (CPUs) on a computer, based on

load. If process affinity has been enabled at the operating system level, then the operating

system assigns each thread to a specific CPU. In contrast, the SQL Server Database Engine

assigns SQL Server

worker threads

to

schedulers

that distribute the threads evenly among the

CPUs, in a round-robin fashion.

To carry out multitasking, for example when multiple applications access the same set of CPUs,

the operating system sometimes moves worker threads among different CPUs. Although

efficient from an operating system point of view, this activity can reduce SQL Server

performance under heavy system loads, as each processor cache is repeatedly reloaded with

data. Assigning CPUs to specific threads can improve performance under these conditions by

eliminating processor reloads and reducing thread migration across CPUs (thereby reducing

context switching); such an association between a thread and a processor is called processor

affinity. If affinity has been enabled, the operating system assigns each thread to a specific

CPU.

schedulers are available. However, the worker thread assigned to the parent task may be

placed in a different NUMA node from other tasks.



Tip

For the output of the DMV seen above, all active tasks are in SUSPENDED state. More

detail on waiting tasks is available by querying the

DMV.

## lightweight pooling

## affinity mask option
