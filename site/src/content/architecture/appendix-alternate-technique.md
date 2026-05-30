---
title: "Appendix: Alternate technique"
topic: "query-processing"
description: "Using the technique above we were able to confirm that the contention was occurring on a"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Using the technique above we were able to confirm that the contention was occurring on a

clustered index with a sequentially increasing key value on the table which by far received the

highest number of inserts. This type of contention isn't uncommon for indexes with a

sequentially increasing key value such as datetime, identity or an application-generated

.

To resolve this issue, we used

hash partitioning with a computed column

and observed a 690%

performance improvement. The following table summarizes the performance of the application

before and after implementing hash partitioning with a computed column. The CPU utilization

increases broadly in line with throughput as expected after the latch contention bottleneck was

removed:

Business Transactions/Sec

36

249

Average Page Latch Wait Time

36 milliseconds

0.6 milliseconds

Latch Waits/Sec

9,562

2,873

SQL Processor Time

24%

78%

SQL Batch Requests/sec

12,368

47,045

As can be seen from the previous table, correctly identifying and resolving performance issues

caused by excessive page latch contention can have a positive effect on overall application

performance.

ﾉ

Expand table

### char

```sql
TransactionID
```
