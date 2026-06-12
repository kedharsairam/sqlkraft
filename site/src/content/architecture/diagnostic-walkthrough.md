---
title: "Diagnostic walkthrough"
topic: "query-processing"
description: "sys.dm_os_spinlock_stats"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Query the

sys.dm_os_spinlock_stats

DMV to look for a high number of spins and

backoff events over periods of time.

Starting with SQL Server 2025 (17.x) Preview, query the

sys.dm_os_wait_stats

and

sys.dm_exec_session_wait_stats

DMVs using the

wait type. Requires

trace flag 8134. For more information, see

SPINLOCK_EXT.

SQL Server

Used to track call stacks for spinlocks that are experiencing a high number of spins.

In some cases, memory dumps of the SQL Server process and the Windows

Debugging tools. In general, this level of analysis is done when the Microsoft Support

teams are engaged.

The general technical process for diagnosing SQL Server Spinlock contention is:

1.

: Determine that there's contention that might be spinlock related.

2.

: Capture statistics from

to find the spinlock type

experiencing the most contention.

3.

: Obtain debug symbols for sqlservr.exe (sqlservr.pdb) and place the symbols in the

same directory as the SQL Server service.exe file (sqlservr.exe) for the instance of SQL

Server.\ In order to see the call stacks for the backoff events, you must have symbols for

the particular version of SQL Server that you're running. Symbols for SQL Server are

available on the Microsoft Symbol Server. For more information about how to download

symbols from the Microsoft Symbol Server, see

Debugging with symbols.

4.

: Use SQL Server Extended Events to trace the backoff events for the spinlock types

of interest. The events to capture are

and.

Extended Events provide the ability to track the backoff events and capture the call stack for

those operation(s) most prevalently trying to obtain the spinlock. By analyzing the call stack, it's

possible to determine what type of operation is contributing to contention for any particular

spinlock.

The following walkthrough shows how to use the tools and techniques to diagnose a spinlock

contention problem in a real world scenario. This walkthrough is based on a customer

engagement running a benchmark test to simulate approximately 6,500 concurrent users on an

8 socket, 64 physical core server with 1 TB of memory.

`SPINLOCK_EXT`

`sys.dm_os_spinlock_stats`

`spinlock_backoff`

`spinlock_backoff_warning`
