---
title: "Indicators of latch contention"
topic: "io-fundamentals"
description: "3."
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

3. Alleviate the contention using one of the techniques described in

Handling Latch

Contention for Different Table Patterns.

As stated previously, latch contention is only problematic when the contention and wait time

associated with acquiring page latches prevents throughput from increasing when CPU

resources are available. Determining an acceptable amount of contention requires a holistic

approach that considers performance and throughput requirements together with available I/O

and CPU resources. This section walks you through determining the impact of latch contention

on workload as follows:

1. Measure overall wait times during a representative test.

2. Rank them in order.

3. Determine the proportion of wait times that are related to latches.

Cumulative wait information is available from the

DMV. The most

common type of latch contention is buffer latch contention, observed as an increase in wait

times for latches with a

of. Non-buffer latches are grouped under the

wait type. As the following diagram illustrates, you should first take a cumulative look

at system waits using the

DMV to determine the percentage of the

overall wait time caused by buffer or non-buffer latches. If you encounter non-buffer latches,

the

DMV must also be examined.

The following diagram describes the relationship between the information returned by the

and

DMVs.

For more information about the

DMV, see

sys.dm_os_wait_stats

in SQL

Server help.

## Average page latch wait time consistently increases with throughput

## MSSQL%InstanceName%\Wait Statistics\Page Latch Waits\Average Wait Time

## Percentage of total wait time spent on latch wait types during peak load

For more information about the

DMV, see

sys.dm_os_latch_stats

in SQL

Server help.

The following measures of latch wait time are indicators that excessive latch contention is

affecting application performance:

: If average page

latch wait times consistently increase with throughput and if average buffer latch wait

times also increase above expected disk response times, you should examine current

waiting tasks using the

DMV. Averages can be misleading if

analyzed in isolation so it's important to look at the system live when possible to

understand workload characteristics. In particular, check whether there are high waits on

and/or

requests on any pages. Follow these steps to

diagnose increasing average page latch wait times with throughput:

Use the sample scripts

Query sys.dm_os_waiting_tasks Ordered by Session ID

or

Calculate Waits Over a Time Period

to look at current waiting tasks and measure

average latch wait time.

Use the sample script

Query Buffer Descriptors to Determine Objects Causing Latch

Contention

to determine the index and underlying table on which the contention is

occurring.

Measure average page latch wait time with the Performance Monitor counter

or by

running the

DMV.

: If the average

latch wait time as a percentage of overall wait time increases in line with application load,

then latch contention might be affecting performance and should be investigated.

Measure page latch waits and non-page latch waits with the

, Wait Statistics

object

performance counters. Then compare the values for these performance counters to

performance counters associated with CPU, I/O, memory, and network throughput. For

example, transactions/sec and batch requests/sec are two good measures of resource

utilization.

７

Note

To calculate the average wait time for a particular wait type (returned by

as

), divide total wait time (returned as

)

by the number of waiting tasks (returned as

).

## non-production environment

## Throughput doesn't increase, and in some case decreases, as application load increases

## and the number of CPUs available to SQL Server increases

## CPU Utilization doesn't increase as application workload increases

## Calculate Waits Over a Time Period

`sys.dm_os_wait_stats`

`wait_type`

```sql
PAGELATCH_*
```

```sql
LATCH*
```

`sys.dm_os_wait_stats`

`sys.dm_os_latch_stats`

`sys.dm_os_wait_stats`

`sys.dm_os_latch_stats`

`sys.dm_os_wait_stats`

`sys.dm_os_latch_stats`

`sys.dm_os_waiting_tasks`

`PAGELATCH_EX`

`PAGELATCH_SH`

`sys.dm_os_wait_stats`

`sys.dm_os_wait_stats`

```sql
wt_:type
```

`wait_time_ms`

`waiting_tasks_count`
