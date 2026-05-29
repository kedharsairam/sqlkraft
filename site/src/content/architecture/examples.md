---
title: 'Examples'
topic: 'query-processing'
description: 'Some of the more common causes for increased CPU consumption include:'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Some of the more common causes for increased CPU consumption include:

Queries that become more expensive over time due to growth of the underlying data

resulting in the need to perform additional logical reads of memory-resident data.

Changes in query plans resulting in suboptimal execution.

In the following example, there's a nearly linear relationship between CPU consumption and

throughput as measured by transactions per second. It's normal to see some divergence here

because overhead is incurred as any workload increases. As illustrated here, this divergence

becomes significant. There's also a precipitous drop in throughput once CPU consumption

reaches 100%.

When measuring the number of spins at 3-minute intervals we can see a more exponential

than linear increase in spins, which indicates that spinlock contention might be problematic.

It's critical to rule out other more common causes of high CPU when troubleshooting

these types of problems.

Even if each of the preceding conditions is true it's still possible that the root cause of high

CPU consumption lies elsewhere. In fact, in the vast majority of the cases increased CPU is

due to reasons other than spinlock contention.


