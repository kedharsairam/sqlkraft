---
title: "Read data damage and wear leveling"
topic: "query-processing"
description: "A newly formatted drive usually holds all zeros."
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

A newly formatted drive usually holds all zeros. An erased block of a solid-state device is all

s,

making a raw read of an erased block all

characters. However, it's unusual for a user to read

an erased block during normal I/O operations.

A technique used in the past is to write a known pattern to the entire drive. Then as database

activity executes against that same drive, incorrect behavior (stale read, lost write, or read of

incorrect offset) can be detected when the pattern unexpectedly appears.

This technique doesn't work well on solid-state storage. The erasure and RMW activities for

writes destroy the pattern. The solid-state storage garbage collection (GC) activity, wear leveling,

proportional/set-aside list blocks, and other optimizations tend to cause writes to acquire

different physical locations, unlike spinning media's sector reuse.

The firmware used in solid-state storage tends to be complex when compared to spinning media

counterparts. Many drives use multiple processing cores to handle incoming requests and

garbage collection activities. Make sure you keep your solid-state device firmware up to date to

avoid known problems.

A common garbage collection (GC) approach for solid-state storage helps prevent repeated, read

data damage. When reading the same cell repeatedly, it's possible the electron activity can leak

and cause damage to neighboring cells. Solid-state storage protects the data with various levels

of error correction code (ECC) and other mechanisms.

One such mechanism relates to wear leveling. Solid-state storage keeps track of the read and

write activity on the storage device. The garbage collection can determine hot spots or locations

wearing faster than other locations. For example, the GC determines that a block is in a read-only

state and needs to move. This movement is generally to a block with more wear, so the original

block can be used for writes. This process helps balance the wear on the drive, but it moves read-

only data to a location that has more wear and mathematically increases the failure chances, even

if slightly.

Another side effect of wear leveling can occur with SQL Server. Suppose you execute

DBCC

CHECKDB

, and it reports an error. If you run it a second time, there's a small chance that

## Recommendations:

```sql
1
```

```sql
0xFF
```

`DBCC`
