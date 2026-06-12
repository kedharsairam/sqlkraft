---
title: "Performance when latch contention is resolved"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

On a busy high-concurrency system, it's normal to see active contention on structures that are

frequently accessed and protected by latches and other control mechanisms in SQL Server. It's

considered problematic when the contention and wait time associated with acquiring latch for

a page is enough to reduce resource (CPU) utilization, which hinders throughput.

In the following diagram, the blue line represents the throughput in SQL Server, as measured

by Transactions per second; the black line represents average page latch wait time. In this case,

each transaction performs an

into a clustered index with a sequentially increasing

leading value, such as when populating an

column of data type bigint. As the number

of CPUs increase to 32 it's evident that the overall throughput has decreased and the page

latch wait time has increased to approximately 48 milliseconds as evidenced by the black line.

This inverse relationship between throughput and page latch wait time is a common scenario

that is easily diagnosed.

As the following diagram illustrates, SQL Server is no longer bottle-necked on page latch waits

and throughput is increased by 300% as measured by transactions per second. This was

accomplished with the

technique described

`INSERT`

`IDENTITY`
